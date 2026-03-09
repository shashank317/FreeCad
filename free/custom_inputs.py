"""
FreeCAD Stepped Revolution Component with GLTF Export - Dynamic Parameters

This script opens FreeCAD, generates the component with dynamic dimensions, and exports to GLTF.

Usage:
    python custom_inputs.py --roller-diameter 160.5 --bearing-width 20 --shaft-diameter 26 --overall-height 50 --base-width 100.5
    python custom_inputs.py --output custom_model.gltf --roller-diameter 160.5 ...
"""

import subprocess
import os
import sys

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))

def find_freecad():
    possible_paths = [
        r"C:\Program Files\FreeCAD 1.0\bin\FreeCAD.exe",
        r"C:\Program Files\FreeCAD 0.21\bin\FreeCAD.exe",
        r"C:\Program Files\FreeCAD 0.20\bin\FreeCAD.exe",
        r"C:\Program Files\FreeCAD\bin\FreeCAD.exe",
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

def find_freecadcmd():
    possible_paths = [
        r"C:\Program Files\FreeCAD 1.0\bin\FreeCADCmd.exe",
        r"C:\Program Files\FreeCAD 0.21\bin\FreeCADCmd.exe",
        r"C:\Program Files\FreeCAD 0.20\bin\FreeCADCmd.exe",
        r"C:\Program Files\FreeCAD\bin\FreeCADCmd.exe",
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

# ============================================================================
# DYNAMIC SCRIPT TEMPLATE
# ============================================================================
SCRIPT_TEMPLATE = '''
"""
FreeCAD script - Stepped Revolution Component
Dynamically generated with custom dimensions.
"""

import FreeCAD as App
import Part
import Sketcher
import Mesh
import MeshPart

OUTPUT_PATH = r"{output_path}"
OUTPUT_FORMAT = "{output_format}"

def create_stepped_revolution():
    """Create a stepped revolution component"""

    try:
        doc = App.ActiveDocument
        if doc is None:
            doc = App.newDocument('SteppedRevolution')
    except:
        doc = App.newDocument('SteppedRevolution')

    App.setActiveDocument(doc.Name)

    print("Creating Stepped Revolution component...")

    # -- Document & Body --
    body = doc.addObject('PartDesign::Body', 'Body')
    body.Label = 'Body'
    doc.recompute()

    # -- Sketch on XY Plane --
    sketch = body.newObject('Sketcher::SketchObject', 'Profile')
    sketch.AttachmentSupport = (doc.getObject('XY_Plane'), [''])
    sketch.MapMode = 'FlatFace'
    doc.recompute()

    V = App.Vector

    # Profile geometry (dynamic points based on input)
    segments = [
        (V(0,     0,    0), V(0,     {y1}, 0)),
        (V(0,     {y1}, 0), V({x1},  {y1}, 0)),
        (V({x1},  {y1}, 0), V({x1},  {y2}, 0)),
        (V({x1},  {y2}, 0), V({x2},  {y2}, 0)),
        (V({x2},  {y2}, 0), V({x2},  {y3}, 0)),
        (V({x2},  {y3}, 0), V({x3},  {y3}, 0)),
        (V({x3},  {y3}, 0), V({x3},  {y4}, 0)),
        (V({x3},  {y4}, 0), V({x4},  {y4}, 0)),
        (V({x4},  {y4}, 0), V({x4},  {y5}, 0)),
        (V({x4},  {y5}, 0), V(0,     {y5}, 0)),
        (V(0,     {y5}, 0), V(0,     0,    0)),
    ]

    for p1, p2 in segments:
        sketch.addGeometry(Part.LineSegment(p1, p2), False)
    doc.recompute()

    # Close polygon
    n = len(segments)
    for i in range(n):
        sketch.addConstraint(Sketcher.Constraint('Coincident', i, 2, (i + 1) % n, 1))
    
    # Lock origin
    sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))
    doc.recompute()

    # Horizontal / vertical constraints
    for i in [0, 2, 4, 6, 8, 10]:
        sketch.addConstraint(Sketcher.Constraint('Vertical', i))
    for i in [1, 3, 5, 7, 9]:
        sketch.addConstraint(Sketcher.Constraint('Horizontal', i))
    doc.recompute()

    # Dimensional Constraints (Using exact coordinates)
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 1, 1, {y1}))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 3, 1, {y2}))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 5, 1, {y3}))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 7, 1, {y4}))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 9, 1, {y5}))

    sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 1, 2, {x1}))
    sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 3, 2, {x2}))
    sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 5, 2, {x3}))
    sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 7, 2, {x4}))
    
    doc.recompute()
    sketch.Visibility = False
    doc.recompute()

    # Revolution
    rev = body.newObject('PartDesign::Revolution', 'Revolution')
    rev.Profile = (sketch, [''])
    rev.ReferenceAxis = (sketch, ['H_Axis'])
    rev.Angle = 360.0
    doc.recompute()

    print("SteppedRevolution created successfully with custom dimensions.")
    return doc

def export_model(doc):
    """Export the model to GLTF format using ImportGui"""
    print("Exporting to " + OUTPUT_FORMAT.upper() + "...")
    
    # Save FreeCAD document first
    fcstd_path = OUTPUT_PATH.replace('.glb', '.FCStd').replace('.gltf', '.FCStd')
    doc.saveAs(fcstd_path)
    print("FreeCAD file saved: " + fcstd_path)

    body = doc.getObject('Body')
    if not body:
        print("Error: Body object not found for export.")
        return False

    import ImportGui
    __objs__ = [body]
    if hasattr(ImportGui, "exportOptions"):
        options = ImportGui.exportOptions(OUTPUT_PATH)
        ImportGui.export(__objs__, OUTPUT_PATH, options)
    else:
        ImportGui.export(__objs__, OUTPUT_PATH)
    del __objs__
    print(OUTPUT_FORMAT.upper() + " successfully saved: " + OUTPUT_PATH)
    return True

doc = create_stepped_revolution()
export_model(doc)
import os
os._exit(0)
'''

def generate_script(output_path, output_format, d_shaft, w_bearing, w_base, h_overall, d_roller):
    if output_path is None:
        output_path = os.path.join(WORKSPACE_DIR, "custom_stepped_revolution." + output_format)
    
    x1 = max(1.0, d_shaft / 2.0)
    x2 = max(x1 + 5.0, x1 + 20.0)               
    x3 = max(x2 + 5.0, w_base / 2.0)            
    x4 = max(x3 + 5.0, d_roller / 2.0)
    
    y5 = max(5.0, h_overall / 2.5)
    y1 = max(y5 + 5.0, h_overall / 2.0)
    y4 = max(y1 + 5.0, w_bearing)
    y3 = max(y4 + 5.0, h_overall - 5.0)
    y2 = max(y3 + 5.0, h_overall)

    return SCRIPT_TEMPLATE.format(
        output_path=output_path.replace("\\", "/"),
        output_format=output_format,
        x1=x1, x2=x2, x3=x3, x4=x4,
        y1=y1, y2=y2, y3=y3, y4=y4, y5=y5
    )


def run_freecad_script(script_content, use_gui=False):
    # Always use FreeCAD.exe (GUI) since ImportGui needs it for GLTF export
    freecad_exe = find_freecad()
    
    if freecad_exe is None:
        print("ERROR: FreeCAD not found!")
        return False
    
    script_path = os.path.join(WORKSPACE_DIR, "_temp_script.py")
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    try:
        # Use Popen so we can kill FreeCAD GUI after it finishes exporting.
        # FreeCAD.exe GUI won't exit on its own even with os._exit(0) in the script.
        proc = subprocess.Popen(
            [freecad_exe, script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        
        # Wait up to 120 seconds for the process to finish on its own
        try:
            stdout, stderr = proc.communicate(timeout=120)
        except subprocess.TimeoutExpired:
            # FreeCAD GUI is likely still open — kill it
            proc.kill()
            stdout, stderr = proc.communicate()
        
        print("--- FreeCAD Output ---")
        print(stdout)
        if stderr:
            print("--- FreeCAD Errors ---")
            print(stderr)
        
        # Check if export was successful by looking at stdout
        if "successfully saved" in stdout:
            return True
        return proc.returncode == 0
    except Exception as e:
        print("Error: " + str(e))
        return False

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="FreeCAD Stepped Revolution with Custom Dimensions")
    parser.add_argument("--output", "-o", type=str, default=None, help="Output file path")
    parser.add_argument("--format", "-f", choices=["glb", "gltf"], default="gltf", help="Output format")
    parser.add_argument("--gui", action="store_true", help="Open FreeCAD GUI")
    
    # Custom Dimensions
    parser.add_argument("--roller-diameter", type=float, required=True, help="Roller Diameter (D)")
    parser.add_argument("--bearing-width", type=float, required=True, help="Bearing Width (B)")
    parser.add_argument("--shaft-diameter", type=float, required=True, help="Shaft Diameter (d)")
    parser.add_argument("--overall-height", type=float, required=True, help="Overall Height (H)")
    parser.add_argument("--base-width", type=float, required=True, help="Base Width (W)")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Generating Model with Dimensions:")
    print("  Roller Diameter: ", args.roller_diameter)
    print("  Bearing Width:   ", args.bearing_width)
    print("  Shaft Diameter:  ", args.shaft_diameter)
    print("  Overall Height:  ", args.overall_height)
    print("  Base Width:      ", args.base_width)
    print("=" * 60)
    
    script = generate_script(
        output_path=args.output,
        output_format=args.format,
        d_shaft=args.shaft_diameter,
        w_bearing=args.bearing_width,
        w_base=args.base_width,
        h_overall=args.overall_height,
        d_roller=args.roller_diameter
    )
    
    run_freecad_script(script, use_gui=args.gui)
    print("Process complete.")

if __name__ == "__main__":
    main()
