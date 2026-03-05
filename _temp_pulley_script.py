
"""
Stepped Shaft/Pulley Generator Script - Run inside FreeCAD
Based on claude.py pattern with GLB/GLTF export
"""
import FreeCAD as App
import Part
import Sketcher
import Mesh
import MeshPart
import os

OUTPUT_PATH = r"c:\\Users\\shashank\\Desktop\\New folder (4)\\stepped_shaft.glb"
OUTPUT_FORMAT = "glb"


def create_stepped_shaft():
    """Create a stepped shaft/pulley component"""

    try:
        doc = App.ActiveDocument
        if doc is None:
            doc = App.newDocument('SteppedShaft')
    except:
        doc = App.newDocument('SteppedShaft')

    App.setActiveDocument(doc.Name)

    print("Creating Stepped Shaft/Pulley component...")

    # -- Document & Body --
    body = doc.addObject('PartDesign::Body', 'Body')
    body.Label = 'Body'
    doc.recompute()

    # -- Sketch on XY Plane --
    sketch = body.newObject('Sketcher::SketchObject', 'Profile')
    sketch.AttachmentSupport = (doc.getObject('XY_Plane'), [''])
    sketch.MapMode = 'FlatFace'
    doc.recompute()

    # -- Profile geometry --
    # Stepped shaft profile. X = radius, Y = height.
    # Step 1: radius=25, height=0-20
    # Step 2: radius=40, height=20-50
    # Step 3: radius=30, height=50-80
    # Revolution around Y-axis (V_Axis)

    V = App.Vector

    segments = [
        (V(0,   0,  0), V(25,  0,  0)),   # 0  - bottom, x: 0 -> 25
        (V(25,  0,  0), V(25, 20,  0)),   # 1  - step 1 wall, y: 0 -> 20
        (V(25, 20,  0), V(40, 20,  0)),   # 2  - shelf @ y=20, x: 25 -> 40
        (V(40, 20,  0), V(40, 50,  0)),   # 3  - step 2 wall, y: 20 -> 50
        (V(40, 50,  0), V(30, 50,  0)),   # 4  - shelf @ y=50, x: 40 -> 30
        (V(30, 50,  0), V(30, 80,  0)),   # 5  - step 3 wall, y: 50 -> 80
        (V(30, 80,  0), V(0,  80,  0)),   # 6  - top, x: 30 -> 0
        (V(0,  80,  0), V(0,   0,  0)),   # 7  - axis, y: 80 -> 0
    ]

    for p1, p2 in segments:
        sketch.addGeometry(Part.LineSegment(p1, p2), False)
    doc.recompute()

    # -- Close the polygon (coincident constraints) --
    n = len(segments)
    for i in range(n):
        sketch.addConstraint(Sketcher.Constraint('Coincident', i, 2, (i + 1) % n, 1))
    doc.recompute()

    # -- Lock origin --
    sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))
    doc.recompute()

    # -- Horizontal / vertical direction constraints --
    for i in [1, 3, 5, 7]:
        sketch.addConstraint(Sketcher.Constraint('Vertical', i))
    for i in [0, 2, 4, 6]:
        sketch.addConstraint(Sketcher.Constraint('Horizontal', i))
    doc.recompute()

    # -- Dimensional constraints --
    # Y heights
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 1, 2, 20.0))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 3, 2, 50.0))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 5, 2, 80.0))

    # X radii
    sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 0, 2, 25.0))
    sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 2, 2, 40.0))
    sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 4, 2, 30.0))
    doc.recompute()

    sketch.Visibility = False
    doc.recompute()

    # -- Revolution (360 around V_Axis / Y-axis) --
    rev = body.newObject('PartDesign::Revolution', 'Revolution')
    rev.Profile = (sketch, [''])
    rev.ReferenceAxis = (sketch, ['V_Axis'])
    rev.Angle = 360.0
    rev.Reversed = 0
    rev.Midplane = 0
    rev.Type = 0
    rev.UpToFace = None
    sketch.Visibility = False
    doc.recompute()

    print("=" * 50)
    print("SteppedShaft created successfully.")
    print("=" * 50)
    print("  Step 1: radius=25mm, height=20mm (0-20mm)")
    print("  Step 2: radius=40mm, height=30mm (20-50mm)")
    print("  Step 3: radius=30mm, height=30mm (50-80mm)")
    print("=" * 50)

    return doc


def export_model(doc):
    """Export the model to GLB/GLTF format"""
    
    print("Exporting to " + OUTPUT_FORMAT.upper() + "...")
    
    # Get all shapes from bodies
    shapes = []
    for obj in doc.Objects:
        if hasattr(obj, 'Shape') and obj.Shape.Solids:
            shapes.append(obj.Shape)
    
    if not shapes:
        print("No shapes found to export!")
        return False
    
    # Combine all shapes
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
    
    # Save as STL (widely supported)
    stl_path = OUTPUT_PATH.replace('.glb', '.stl').replace('.gltf', '.stl')
    mesh.write(stl_path)
    print("STL saved: " + stl_path)
    
    # Save as OBJ
    obj_path = OUTPUT_PATH.replace('.glb', '.obj').replace('.gltf', '.obj')
    mesh.write(obj_path)
    print("OBJ saved: " + obj_path)
    
    # Try to save as GLB/GLTF directly
    try:
        mesh.write(OUTPUT_PATH)
        print(OUTPUT_FORMAT.upper() + " saved: " + OUTPUT_PATH)
    except Exception as e:
        print("Direct " + OUTPUT_FORMAT.upper() + " export not available: " + str(e))
        print("Use Blender or online converter to convert STL/OBJ to GLB/GLTF")
    
    # Save FreeCAD document
    fcstd_path = OUTPUT_PATH.replace('.glb', '.FCStd').replace('.gltf', '.FCStd')
    doc.saveAs(fcstd_path)
    print("FreeCAD file saved: " + fcstd_path)
    
    return True


# Run the creation and export
doc = create_stepped_shaft()
export_model(doc)
