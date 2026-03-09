
"""
FreeCAD script - Parameterized Stepped Revolution Component
"""

import FreeCAD as App
import Part
import Sketcher
import Mesh
import MeshPart

OUTPUT_PATH = r"c:\\Users\\shashank\\Desktop\\New folder (4)\\Scriptoutput\\stepped_revolution_custom.glb"
OUTPUT_FORMAT = "glb"

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
    x1 = 15.0
    x2 = 40.0
    x3 = 120.0
    x4 = 180.0

    y1 = 25.0
    y2 = 30.0
    y3 = 35.0
    y4 = 50.0
    y5 = 55.0

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
