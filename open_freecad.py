"""
FreeCAD Bolt Generator with GLB/GLTF Export

This script:
1. Opens FreeCAD (console mode or GUI)
2. Generates an M14-style hex bolt with customizable dimensions
3. Exports the result to GLB or GLTF format

Usage:
    python open_freecad.py                    # Generate with default dimensions
    python open_freecad.py --diameter 12 --length 50 --output bolt.glb
    
Run inside FreeCAD console:
    exec(open('c:/Users/shashank/Desktop/New folder (4)/open_freecad.py').read())
"""

import subprocess
import os
import sys
import tempfile
import json

# ============================================================================
# PATH CONFIGURATION
# ============================================================================
WORKSPACE_DIR = r"c:\Users\shashank\Desktop\New folder (4)"

def find_freecad():
    """Find FreeCAD installation path on Windows."""
    possible_paths = [
        r"C:\Program Files\FreeCAD 1.0\bin\FreeCAD.exe",
        r"C:\Program Files\FreeCAD 0.21\bin\FreeCAD.exe",
        r"C:\Program Files\FreeCAD 0.20\bin\FreeCAD.exe",
        r"C:\Program Files\FreeCAD 0.19\bin\FreeCAD.exe",
        r"C:\Program Files\FreeCAD\bin\FreeCAD.exe",
        r"C:\Program Files (x86)\FreeCAD 0.21\bin\FreeCAD.exe",
        r"C:\Program Files (x86)\FreeCAD 0.20\bin\FreeCAD.exe",
        r"C:\Program Files (x86)\FreeCAD\bin\FreeCAD.exe",
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    try:
        result = subprocess.run(["where", "FreeCAD"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip().split('\n')[0]
    except Exception:
        pass
    
    return None

def find_freecadcmd():
    """Find FreeCADCmd (console mode) path on Windows."""
    possible_paths = [
        r"C:\Program Files\FreeCAD 1.0\bin\FreeCADCmd.exe",
        r"C:\Program Files\FreeCAD 0.21\bin\FreeCADCmd.exe",
        r"C:\Program Files\FreeCAD 0.20\bin\FreeCADCmd.exe",
        r"C:\Program Files\FreeCAD 0.19\bin\FreeCADCmd.exe",
        r"C:\Program Files\FreeCAD\bin\FreeCADCmd.exe",
        r"C:\Program Files (x86)\FreeCAD 0.21\bin\FreeCADCmd.exe",
        r"C:\Program Files (x86)\FreeCAD 0.20\bin\FreeCADCmd.exe",
        r"C:\Program Files (x86)\FreeCAD\bin\FreeCADCmd.exe",
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    # Try finding from FreeCAD.exe path
    freecad_path = find_freecad()
    if freecad_path:
        freecadcmd_path = freecad_path.replace("FreeCAD.exe", "FreeCADCmd.exe")
        if os.path.exists(freecadcmd_path):
            return freecadcmd_path
    
    return None


# ============================================================================
# BOLT GENERATION SCRIPT (to be run inside FreeCAD)
# ============================================================================
BOLT_SCRIPT_TEMPLATE = '''
"""
Bolt Generator Script - Run inside FreeCAD
"""
import FreeCAD as App
import Part
import Sketcher
import Mesh
import MeshPart
import math
import os

# Parameters passed from external script
D = {diameter}              # Nominal diameter (mm)
PITCH = {pitch}             # Thread pitch (mm)
AF = {across_flats}         # Across flats - hex head (mm)
K = {head_height}           # Head height (mm)
L = {length}                # Shaft length (mm)
OUTPUT_PATH = r"{output_path}"
OUTPUT_FORMAT = "{output_format}"

# Thread geometry calculations
if L <= 125:
    THREAD_LENGTH = 2 * D + 6
else:
    THREAD_LENGTH = 2 * D + 12

H = 0.866025 * PITCH
THREAD_DEPTH = 0.6134 * PITCH
RADIUS = D / 2
CHAMFER = 0.1 * D


def create_bolt():
    """Create hex bolt with threads"""
    
    try:
        doc = App.ActiveDocument
        if doc is None:
            doc = App.newDocument('Bolt')
    except:
        doc = App.newDocument('Bolt')
    
    App.setActiveDocument(doc.Name)
    
    print(f"Creating bolt: D={{D}}mm, L={{L}}mm...")
    
    # Create Body for shaft
    body = doc.addObject('PartDesign::Body', 'Body')
    body.Label = 'BoltShaft'
    doc.recompute()
    
    # Cylinder Sketch
    sketch = body.newObject('Sketcher::SketchObject', 'Sketch')
    sketch.AttachmentSupport = (doc.getObject('YZ_Plane'), [''])
    sketch.MapMode = 'FlatFace'
    doc.recompute()
    
    geoList = [Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), RADIUS)]
    sketch.addGeometry(geoList, False)
    sketch.addConstraint(Sketcher.Constraint('Diameter', 0, D))
    sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))
    doc.recompute()
    
    # Pad Cylinder
    pad = body.newObject('PartDesign::Pad', 'Pad')
    pad.Profile = (sketch, [''])
    pad.Length = L
    pad.ReferenceAxis = (sketch, ['N_Axis'])
    sketch.Visibility = False
    doc.recompute()
    
    # Chamfer tip
    try:
        chamfer = body.newObject('PartDesign::Chamfer', 'Chamfer')
        chamfer.Base = (pad, ['Edge2'])
        chamfer.Size = CHAMFER
        pad.Visibility = False
        doc.recompute()
    except Exception as e:
        print(f"Chamfer skipped: {{e}}")
    
    # Thread Profile Sketch
    thread_sketch = body.newObject('Sketcher::SketchObject', 'ThreadSketch')
    thread_sketch.AttachmentSupport = (doc.getObject('XY_Plane'), [''])
    thread_sketch.MapMode = 'FlatFace'
    doc.recompute()
    
    top_y = RADIUS
    bot_y = RADIUS - THREAD_DEPTH
    crest_half = PITCH * 0.375
    root_half = PITCH * 0.125
    
    thread_sketch.addGeometry(Part.LineSegment(
        App.Vector(-crest_half, top_y, 0), App.Vector(crest_half, top_y, 0)), False)
    thread_sketch.addConstraint(Sketcher.Constraint('Horizontal', 0))
    
    thread_sketch.addGeometry(Part.LineSegment(
        App.Vector(crest_half, top_y, 0), App.Vector(root_half, bot_y, 0)), False)
    thread_sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
    
    thread_sketch.addGeometry(Part.LineSegment(
        App.Vector(root_half, bot_y, 0), App.Vector(-root_half, bot_y, 0)), False)
    thread_sketch.addConstraint(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
    thread_sketch.addConstraint(Sketcher.Constraint('Horizontal', 2))
    
    thread_sketch.addGeometry(Part.LineSegment(
        App.Vector(-root_half, bot_y, 0), App.Vector(-crest_half, top_y, 0)), False)
    thread_sketch.addConstraint(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
    thread_sketch.addConstraint(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
    thread_sketch.addConstraint(Sketcher.Constraint('Equal', 1, 3))
    doc.recompute()
    
    # Subtractive Helix for threads
    try:
        helix = body.newObject('PartDesign::SubtractiveHelix', 'SubtractiveHelix')
        helix.Profile = (thread_sketch, [''])
        helix.ReferenceAxis = (doc.getObject('X_Axis'), [''])
        helix.Pitch = PITCH
        helix.Height = THREAD_LENGTH
        helix.Turns = THREAD_LENGTH / PITCH
        thread_sketch.Visibility = False
        doc.recompute()
    except Exception as e:
        print(f"Thread helix skipped: {{e}}")
    
    # Hex Head Body
    hex_body = doc.addObject('PartDesign::Body', 'HexHead')
    hex_body.Label = 'BoltHead'
    doc.recompute()
    
    hex_sketch = hex_body.newObject('Sketcher::SketchObject', 'HexSketch')
    hex_sketch.AttachmentSupport = (doc.getObject('YZ_Plane001'), [''])
    hex_sketch.MapMode = 'FlatFace'
    doc.recompute()
    
    # Create hexagon
    hex_radius = AF / math.sqrt(3)
    try:
        import ProfileLib.RegularPolygon
        ProfileLib.RegularPolygon.makeRegularPolygon(hex_sketch, 6, App.Vector(0, 0, 0), App.Vector(hex_radius, 0, 0), False)
    except:
        # Manual hexagon if ProfileLib not available
        for i in range(6):
            angle1 = math.radians(60 * i)
            angle2 = math.radians(60 * (i + 1))
            p1 = App.Vector(hex_radius * math.cos(angle1), hex_radius * math.sin(angle1), 0)
            p2 = App.Vector(hex_radius * math.cos(angle2), hex_radius * math.sin(angle2), 0)
            hex_sketch.addGeometry(Part.LineSegment(p1, p2), False)
        for i in range(6):
            hex_sketch.addConstraint(Sketcher.Constraint('Coincident', i, 2, (i + 1) % 6, 1))
    
    hex_sketch.addConstraint(Sketcher.Constraint('Coincident', 6, 3, -1, 1))
    doc.recompute()
    
    # Pad Hex Head
    hex_pad = hex_body.newObject('PartDesign::Pad', 'HexPad')
    hex_pad.Profile = (hex_sketch, [''])
    hex_pad.Length = K
    hex_pad.ReferenceAxis = (hex_sketch, ['N_Axis'])
    hex_sketch.Visibility = False
    doc.recompute()
    
    # Position Head at end of shaft
    hex_body.Placement = App.Placement(App.Vector(L - K, 0, 0), App.Rotation(App.Vector(0, 0, 1), 0))
    doc.recompute()
    
    print("Bolt model created successfully!")
    
    # Export to mesh format
    export_to_gltf(doc, OUTPUT_PATH, OUTPUT_FORMAT)
    
    return doc


def export_to_gltf(doc, output_path, format_type):
    """Export document to GLB/GLTF format"""
    
    print(f"Exporting to {{format_type.upper()}}...")
    
    # Get all shapes from bodies
    shapes = []
    for obj in doc.Objects:
        if hasattr(obj, 'Shape') and obj.Shape.Solids:
            shapes.append(obj.Shape)
    
    if not shapes:
        print("No shapes found to export!")
        return False
    
    # Combine all shapes into one compound
    if len(shapes) > 1:
        compound = Part.makeCompound(shapes)
    else:
        compound = shapes[0]
    
    # Create mesh from shape
    mesh = MeshPart.meshFromShape(
        Shape=compound,
        LinearDeflection=0.1,
        AngularDeflection=0.5,
        Relative=False
    )
    
    # Export to intermediate OBJ file first
    temp_obj = output_path.replace('.glb', '.obj').replace('.gltf', '.obj')
    mesh.write(temp_obj)
    print(f"Intermediate OBJ saved: {{temp_obj}}")
    
    # Try direct GLTF export if available
    try:
        if format_type.lower() == 'glb':
            mesh.write(output_path)
            print(f"GLB saved: {{output_path}}")
        else:
            mesh.write(output_path)
            print(f"GLTF saved: {{output_path}}")
    except Exception as e:
        print(f"Direct GLTF export not available: {{e}}")
        print(f"OBJ file saved at: {{temp_obj}}")
        print("Use an external converter (Blender, online tool) to convert OBJ to GLB/GLTF")
        
        # Also save as STL which is more widely supported
        stl_path = output_path.replace('.glb', '.stl').replace('.gltf', '.stl')
        mesh.write(stl_path)
        print(f"STL also saved: {{stl_path}}")
    
    # Save FreeCAD document
    fcstd_path = output_path.replace('.glb', '.FCStd').replace('.gltf', '.FCStd')
    doc.saveAs(fcstd_path)
    print(f"FreeCAD file saved: {{fcstd_path}}")
    
    return True


# Run the bolt creation
create_bolt()
'''


def generate_bolt_script(diameter=14, pitch=2.0, across_flats=21, head_height=8.62, 
                         length=70, output_path=None, output_format="glb"):
    """Generate the FreeCAD script with custom parameters."""
    
    if output_path is None:
        output_path = os.path.join(WORKSPACE_DIR, f"bolt_D{diameter}_L{length}.{output_format}")
    
    script = BOLT_SCRIPT_TEMPLATE.format(
        diameter=diameter,
        pitch=pitch,
        across_flats=across_flats,
        head_height=head_height,
        length=length,
        output_path=output_path.replace("\\", "\\\\"),
        output_format=output_format
    )
    
    return script


def run_freecad_script(script_content, use_gui=False):
    """Run a script in FreeCAD (console or GUI mode)."""
    
    if use_gui:
        freecad_exe = find_freecad()
    else:
        freecad_exe = find_freecadcmd()
        if freecad_exe is None:
            freecad_exe = find_freecad()
    
    if freecad_exe is None:
        print("ERROR: FreeCAD not found!")
        print("Please install FreeCAD from: https://www.freecad.org/downloads.php")
        return False
    
    print(f"Using FreeCAD: {freecad_exe}")
    
    # Write script to temporary file
    script_path = os.path.join(WORKSPACE_DIR, "_temp_bolt_script.py")
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    print(f"Script saved to: {script_path}")
    
    # Run FreeCAD with the script
    try:
        if use_gui:
            # GUI mode: open FreeCAD and run script
            subprocess.Popen([freecad_exe, script_path])
            print("FreeCAD GUI launched. Script will run automatically.")
        else:
            # Console mode: run and wait
            print("Running FreeCAD in console mode...")
            result = subprocess.run(
                [freecad_exe, script_path],
                capture_output=True,
                text=True,
                timeout=300
            )
            print(result.stdout)
            if result.stderr:
                print("Errors:", result.stderr)
        
        return True
    except subprocess.TimeoutExpired:
        print("FreeCAD process timed out (5 minutes)")
        return False
    except Exception as e:
        print(f"Error running FreeCAD: {e}")
        return False


def open_freecad(file_path=None):
    """Open FreeCAD GUI, optionally with a file."""
    freecad_path = find_freecad()
    
    if freecad_path is None:
        print("FreeCAD not found. Please install FreeCAD or update the path.")
        print("You can download FreeCAD from: https://www.freecad.org/downloads.php")
        return False
    
    print(f"Found FreeCAD at: {freecad_path}")
    
    try:
        if file_path:
            subprocess.Popen([freecad_path, file_path])
            print(f"Opening FreeCAD with file: {file_path}")
        else:
            subprocess.Popen([freecad_path])
            print("Opening FreeCAD...")
        return True
    except Exception as e:
        print(f"Error opening FreeCAD: {e}")
        return False


def main():
    """Main entry point with argument parsing."""
    import argparse
    
    parser = argparse.ArgumentParser(description="FreeCAD Bolt Generator with GLB/GLTF Export")
    parser.add_argument("--diameter", "-d", type=float, default=14, help="Bolt diameter in mm (default: 14)")
    parser.add_argument("--pitch", "-p", type=float, default=2.0, help="Thread pitch in mm (default: 2.0)")
    parser.add_argument("--length", "-l", type=float, default=70, help="Bolt length in mm (default: 70)")
    parser.add_argument("--head-size", type=float, default=None, help="Hex head across-flats in mm (default: 1.5 * diameter)")
    parser.add_argument("--head-height", type=float, default=None, help="Head height in mm (default: 0.6 * diameter)")
    parser.add_argument("--output", "-o", type=str, default=None, help="Output file path")
    parser.add_argument("--format", "-f", choices=["glb", "gltf"], default="glb", help="Output format (default: glb)")
    parser.add_argument("--gui", action="store_true", help="Open FreeCAD GUI instead of console mode")
    parser.add_argument("--open-only", action="store_true", help="Just open FreeCAD without generating a bolt")
    
    args = parser.parse_args()
    
    if args.open_only:
        return open_freecad()
    
    # Calculate defaults based on diameter
    head_size = args.head_size if args.head_size else args.diameter * 1.5
    head_height = args.head_height if args.head_height else args.diameter * 0.6
    
    print("=" * 60)
    print("FreeCAD Bolt Generator")
    print("=" * 60)
    print(f"  Diameter:    {args.diameter} mm")
    print(f"  Length:      {args.length} mm")
    print(f"  Pitch:       {args.pitch} mm")
    print(f"  Head size:   {head_size} mm (across flats)")
    print(f"  Head height: {head_height} mm")
    print(f"  Format:      {args.format.upper()}")
    print("=" * 60)
    
    # Generate and run the script
    script = generate_bolt_script(
        diameter=args.diameter,
        pitch=args.pitch,
        across_flats=head_size,
        head_height=head_height,
        length=args.length,
        output_path=args.output,
        output_format=args.format
    )
    
    run_freecad_script(script, use_gui=args.gui)


if __name__ == "__main__":
    main()
