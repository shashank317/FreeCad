
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
D = 14              # Nominal diameter (mm)
PITCH = 2.0             # Thread pitch (mm)
AF = 21.0         # Across flats - hex head (mm)
K = 8.4           # Head height (mm)
L = 70                # Shaft length (mm)
OUTPUT_PATH = r"c:\\Users\\shashank\\Desktop\\New folder (4)\\bolt_D14_L70.glb"
OUTPUT_FORMAT = "glb"

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
    
    print(f"Creating bolt: D={D}mm, L={L}mm...")
    
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
        print(f"Chamfer skipped: {e}")
    
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
        print(f"Thread helix skipped: {e}")
    
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
    
    print(f"Exporting to {format_type.upper()}...")
    
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
    print(f"Intermediate OBJ saved: {temp_obj}")
    
    # Try direct GLTF export if available
    try:
        if format_type.lower() == 'glb':
            mesh.write(output_path)
            print(f"GLB saved: {output_path}")
        else:
            mesh.write(output_path)
            print(f"GLTF saved: {output_path}")
    except Exception as e:
        print(f"Direct GLTF export not available: {e}")
        print(f"OBJ file saved at: {temp_obj}")
        print("Use an external converter (Blender, online tool) to convert OBJ to GLB/GLTF")
        
        # Also save as STL which is more widely supported
        stl_path = output_path.replace('.glb', '.stl').replace('.gltf', '.stl')
        mesh.write(stl_path)
        print(f"STL also saved: {stl_path}")
    
    # Save FreeCAD document
    fcstd_path = output_path.replace('.glb', '.FCStd').replace('.gltf', '.FCStd')
    doc.saveAs(fcstd_path)
    print(f"FreeCAD file saved: {fcstd_path}")
    
    return True


# Run the bolt creation
create_bolt()
