import argparse
import subprocess
import os
import sys

WORKSPACE_DIR = r"c:\Users\shashank\Desktop\New folder (4)"
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "Scriptoutput")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

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
# PARAMETERIZED FREECAD SCRIPT
# ============================================================================
SCRIPT_TEMPLATE = '''
"""
FreeCAD script - Parameterized Stepped Revolution Component
"""

import FreeCAD as App
import Part
import Sketcher
import Mesh
import MeshPart

OUTPUT_PATH = r"{output_path}"
OUTPUT_FORMAT = "{output_format}"

def create_stepped_revolution():
    """Create a stepped revolution component with custom dimensions"""
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

    # -- User Custom Dimensions --
    x1 = {x1}
    x2 = {x2}
    x3 = {x3}
    x4 = {x4}

    y1 = {y1}
    y2 = {y2}
    y3 = {y3}
    y4 = {y4}
    y5 = {y5}

    V = App.Vector

    segments = [
        (V(0,   y1,  0), V(0,   y2,  0)),  # 0: Left face: start at inner bore Y1, up to Y2 
        (V(0,   y2,  0), V(x1,  y2,  0)),  # 1: First shelf 
        (V(x1,  y2,  0), V(x1,  y5,  0)),  # 2: Step up 
        (V(x1,  y5,  0), V(x2,  y5,  0)),  # 3: Second shelf 
        (V(x2,  y5,  0), V(x2,  y4,  0)),  # 4: Step down 
        (V(x2,  y4,  0), V(x3,  y4,  0)),  # 5: Third shelf 
        (V(x3,  y4,  0), V(x3,  y3,  0)),  # 6: Step down 
        (V(x3,  y3,  0), V(x4,  y3,  0)),  # 7: Fourth shelf 
        (V(x4,  y3,  0), V(x4,  y1,  0)),  # 8: Right face down to inner bore Y1 
        (V(x4,  y1,  0), V(0,   y1,  0)),  # 9: Inner bore surface back to start
    ]

    for p1, p2 in segments:
        sketch.addGeometry(Part.LineSegment(p1, p2), False)
    doc.recompute()

    # -- Close the polygon (coincident constraints) --
    n = len(segments)
    for i in range(n):
        sketch.addConstraint(Sketcher.Constraint('Coincident', i, 2, (i + 1) % n, 1))
    doc.recompute()

    # -- Horizontal / vertical direction constraints --
    for i in [0, 2, 4, 6, 8]:
        sketch.addConstraint(Sketcher.Constraint('Vertical', i))
    for i in [1, 3, 5, 7, 9]:
        sketch.addConstraint(Sketcher.Constraint('Horizontal', i))
    doc.recompute()

    sketch.Visibility = False
    doc.recompute()

    # -- Revolution (360 around H_Axis / Base X axis in XY plane) --
    rev = body.newObject('PartDesign::Revolution', 'Revolution')
    rev.Profile = (sketch, [''])
    rev.ReferenceAxis = (sketch, ['H_Axis'])
    rev.Angle = 360.0
    rev.Reversed = 0
    rev.Midplane = 0
    rev.Type = 0
    rev.UpToFace = None
    sketch.Visibility = False
    doc.recompute()

    print("=" * 50)
    print("Parameterized SteppedRevolution created successfully.")
    print("=" * 50)

    return doc


def export_model(doc):
    """Export the model to GLB/GLTF format"""
    print("Exporting to " + OUTPUT_FORMAT.upper() + "...")
    
    shapes = []
    for obj in doc.Objects:
        if hasattr(obj, 'Shape') and obj.Shape.Solids:
            shapes.append(obj.Shape)
    
    if not shapes:
        print("No shapes found to export!")
        return False
    
    if len(shapes) > 1:
        compound = Part.makeCompound(shapes)
    else:
        compound = shapes[0]
    
    mesh = MeshPart.meshFromShape(
        Shape=compound,
        LinearDeflection=0.1,
        AngularDeflection=0.5,
        Relative=False
    )
    
    # Save as STL
    stl_path = OUTPUT_PATH.replace('.glb', '.stl').replace('.gltf', '.stl')
    mesh.write(stl_path)
    print("STL saved: " + stl_path)
    
    # Save as OBJ
    obj_path = OUTPUT_PATH.replace('.glb', '.obj').replace('.gltf', '.obj')
    mesh.write(obj_path)
    print("OBJ saved: " + obj_path)
    
    # Try GLB/GLTF
    try:
        mesh.write(OUTPUT_PATH)
        print(OUTPUT_FORMAT.upper() + " saved: " + OUTPUT_PATH)
    except Exception as e:
        print("Direct " + OUTPUT_FORMAT.upper() + " export not available")
        print("Use Blender to convert STL/OBJ to GLB/GLTF")
    
    # Save FreeCAD document
    fcstd_path = OUTPUT_PATH.replace('.glb', '.FCStd').replace('.gltf', '.FCStd')
    doc.saveAs(fcstd_path)
    print("FreeCAD file saved: " + fcstd_path)
    
    return True

# Run
doc = create_stepped_revolution()
export_model(doc)
'''

def generate_script(dims, output_path=None, output_format="glb"):
    if output_path is None:
        filename = "stepped_revolution_custom." + output_format
        output_path = os.path.join(OUTPUT_DIR, filename)

    return SCRIPT_TEMPLATE.format(
        output_path=output_path.replace("\\", "\\\\"),
        output_format=output_format,
        x1=dims['x1'],
        x2=dims['x2'],
        x3=dims['x3'],
        x4=dims['x4'],
        y1=dims['y1'],
        y2=dims['y2'],
        y3=dims['y3'],
        y4=dims['y4'],
        y5=dims['y5']
    )


def run_freecad_script(script_content, use_gui=False):
    if use_gui:
        freecad_exe = find_freecad()
    else:
        freecad_exe = find_freecadcmd()
        if freecad_exe is None:
            freecad_exe = find_freecad()
    
    if freecad_exe is None:
        print("ERROR: FreeCAD not found!")
        return False
    
    print("Using FreeCAD: " + freecad_exe)
    
    script_path = os.path.join(WORKSPACE_DIR, "_temp_custom_script.py")
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print("Script saved to: " + script_path)
    
    try:
        if use_gui:
            subprocess.Popen([freecad_exe, script_path])
            print("FreeCAD GUI launched.")
        else:
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
    except Exception as e:
        print("Error: " + str(e))
        return False


def main():
    parser = argparse.ArgumentParser(description="FreeCAD Parameterized Stepped Revolution Generator")
    parser.add_argument("--output", "-o", type=str, default=None, help="Output file path (default uses Scriptoutput folder)")
    parser.add_argument("--format", "-f", choices=["glb", "gltf"], default="glb", help="Output format")
    parser.add_argument("--gui", action="store_true", help="Open FreeCAD GUI")
    parser.add_argument("--interactive", "-i", action="store_true", help="Force interactive terminal prompt for inputs")

    # The 4 lateral (X) dimensions mapping
    parser.add_argument("--x1", type=float, default=None, help="Inner-most X radius")
    parser.add_argument("--x2", type=float, default=None, help="Second X radius")
    parser.add_argument("--x3", type=float, default=None, help="Third X radius")
    parser.add_argument("--x4", type=float, default=None, help="Outer-most X radius")

    # The 5 vertical (Y) dimensions mapping
    parser.add_argument("--y1", type=float, default=None, help="First Y height")
    parser.add_argument("--y2", type=float, default=None, help="Second Y height")
    parser.add_argument("--y3", type=float, default=None, help="Third Y height")
    parser.add_argument("--y4", type=float, default=None, help="Fourth Y height")
    parser.add_argument("--y5", type=float, default=None, help="Full Y height")

    args = parser.parse_args()

    dims = {}
    
    # Check if any argument is missing or if interactive flag is set
    needs_input = args.interactive or any(getattr(args, var) is None for var in ['x1', 'x2', 'x3', 'x4', 'y1', 'y2', 'y3', 'y4', 'y5'])
    
    if needs_input:
        print("=" * 60)
        print("Please enter the custom dimensions for the component.")
        print("Press Enter to use the default value shown in brackets.")
        print("=" * 60)
        
        def get_input(prompt_text, default_val):
            val = input(f"{prompt_text} [{default_val}]: ").strip()
            if not val:
                return default_val
            try:
                return float(val)
            except ValueError:
                print("Invalid input! Using default.")
                return default_val
        
        print("\n--- X Radii (from inner to outer) ---")
        dims['x1'] = get_input("Inner-most X radius (x1)", 13.0)
        dims['x2'] = get_input("Second X radius (x2)", 33.0)
        dims['x3'] = get_input("Third X radius (x3)", 100.5)
        dims['x4'] = get_input("Outer-most X radius (x4)", 160.5)
        
        print("\n--- Y Heights (from base to top) ---")
        dims['y1'] = get_input("First Y height (y1)", 20.0)
        dims['y2'] = get_input("Second Y height (y2)", 25.0)
        dims['y3'] = get_input("Third Y height (y3)", 32.5)
        dims['y4'] = get_input("Fourth Y height (y4)", 45.0)
        dims['y5'] = get_input("Full Y height (y5)", 50.0)
        
        print("\n")
    else:
        dims = {
            'x1': args.x1,
            'x2': args.x2,
            'x3': args.x3,
            'x4': args.x4,
            'y1': args.y1,
            'y2': args.y2,
            'y3': args.y3,
            'y4': args.y4,
            'y5': args.y5
        }
    
    print("=" * 60)
    print("Generating Parameterized Stepped Revolution")
    print(f"X Radii: {dims['x1']} | {dims['x2']} | {dims['x3']} | {dims['x4']}")
    print(f"Y Heights: {dims['y1']} | {dims['y2']} | {dims['y3']} | {dims['y4']} | {dims['y5']}")
    print("=" * 60)
    
    script = generate_script(dims, output_path=args.output, output_format=args.format)
    run_freecad_script(script, use_gui=args.gui)

if __name__ == "__main__":
    main()
