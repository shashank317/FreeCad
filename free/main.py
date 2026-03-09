import os
import sys
import subprocess
import zipfile
import io
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="FreeCAD Model Generator")

# --------------- Serve index.html at root ---------------
STATIC_DIR = Path(__file__).resolve().parent / "static"


@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_file = STATIC_DIR / "index.html"
    return index_file.read_text(encoding="utf-8")


# --------------- Pydantic request model ---------------
class CADParams(BaseModel):
    roller_diameter: float
    bearing_width: float
    shaft_diameter: float
    overall_height: float
    base_width: float


# --------------- Constants ---------------
FREECAD_SCRIPT = str(Path(__file__).resolve().parent / "custom_input.py")
PYTHON_EXE = sys.executable  # Use the same Python that runs this server
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def _next_output_path() -> Path:
    """Return the next sequential filename like output/1.gltf, output/2.gltf, …
    Scans all file types (.gltf, .stl, .obj, .FCStd) to determine the next number."""
    existing = sorted(
        int(f.stem) for f in OUTPUT_DIR.iterdir()
        if f.is_file() and f.stem.isdigit()
    )
    next_num = (existing[-1] + 1) if existing else 1
    return OUTPUT_DIR / f"{next_num}.gltf"


# --------------- POST endpoint ---------------
@app.post("/api/generate-cad")
async def generate_cad(params: CADParams):
    output_path = _next_output_path()

    # Convert UI parameters to x/y coordinates for custom_input.py
    x1 = max(1.0, params.shaft_diameter / 2.0)
    x2 = max(x1 + 5.0, x1 + 20.0)
    x3 = max(x2 + 5.0, params.base_width / 2.0)
    x4 = max(x3 + 5.0, params.roller_diameter / 2.0)

    y1 = max(5.0, params.overall_height / 2.5)
    y2 = max(y1 + 5.0, params.overall_height / 2.0)
    y3 = max(y2 + 5.0, params.bearing_width)
    y4 = max(y3 + 5.0, params.overall_height - 5.0)
    y5 = max(y4 + 5.0, params.overall_height)

    command = [
        PYTHON_EXE,
        FREECAD_SCRIPT,
        "--x1", str(x1),
        "--x2", str(x2),
        "--x3", str(x3),
        "--x4", str(x4),
        "--y1", str(y1),
        "--y2", str(y2),
        "--y3", str(y3),
        "--y4", str(y4),
        "--y5", str(y5),
        "--output", str(output_path),
        "--format", "gltf",
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=300,
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="FreeCAD process timed out.")
    except FileNotFoundError:
        raise HTTPException(
            status_code=500,
            detail="FreeCAD executable not found. Check the installation path.",
        )

    print("=== subprocess GLTF return code: {} ===".format(result.returncode))

    # FreeCAD GUI may exit with non-zero code even after successful export.
    # Check if the output file exists before raising an error.
    gltf_path = output_path
    stl_path = output_path.with_suffix(".stl")
    obj_path = output_path.with_suffix(".obj")

    if gltf_path.exists():
        return JSONResponse({"url": f"/output/{gltf_path.name}"})
    elif stl_path.exists():
        return JSONResponse({"url": f"/output/{stl_path.name}"})
    elif obj_path.exists():
        return JSONResponse({"url": f"/output/{obj_path.name}"})
    else:
        raise HTTPException(
            status_code=500,
            detail=f"FreeCAD GLTF exited with code {result.returncode}.\nstdout: {result.stdout}\nstderr: {result.stderr}",
        )


# --------------- Download latest files endpoint ---------------
@app.get("/api/download-latest")
async def download_latest():
    """Download all files with the latest (highest) number as a zip."""
    # Find the highest numbered file
    existing = sorted(
        int(f.stem) for f in OUTPUT_DIR.iterdir()
        if f.is_file() and f.stem.isdigit()
    )
    
    if not existing:
        raise HTTPException(status_code=404, detail="No generated files found.")
    
    latest_num = existing[-1]
    
    # Collect all files with this number (different extensions)
    latest_files = [
        f for f in OUTPUT_DIR.iterdir()
        if f.is_file() and f.stem == str(latest_num)
    ]
    
    if not latest_files:
        raise HTTPException(status_code=404, detail="No files found for latest model.")
    
    # Create a zip file in memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in latest_files:
            zf.write(file_path, file_path.name)
    
    zip_buffer.seek(0)
    
    return StreamingResponse(
        zip_buffer,
        media_type="application/zip",
        headers={"Content-Disposition": f"attachment; filename=model_{latest_num}.zip"}
    )


@app.get("/api/latest-info")
async def latest_info():
    """Get info about the latest generated files."""
    existing = sorted(
        int(f.stem) for f in OUTPUT_DIR.iterdir()
        if f.is_file() and f.stem.isdigit()
    )
    
    if not existing:
        return JSONResponse({"available": False, "files": []})
    
    latest_num = existing[-1]
    latest_files = [
        f.name for f in OUTPUT_DIR.iterdir()
        if f.is_file() and f.stem == str(latest_num)
    ]
    
    return JSONResponse({
        "available": True,
        "number": latest_num,
        "files": latest_files
    })


# --------------- Serve output files (GLTF + BIN) ---------------
app.mount("/output", StaticFiles(directory=str(OUTPUT_DIR)), name="output")

# --------------- Serve other static assets (CSS, JS, etc.) ---------------
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
