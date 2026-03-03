#!/usr/bin/env python3
"""
M14_bolt.py - M14 Hex Bolt Generator for FreeCAD (JIS B 1180)

Run inside FreeCAD Python console:
    exec(open('c:/Users/shashank/Desktop/CadAI/M16/M14_bolt.py').read())
"""

import FreeCAD as App
import Part
import Sketcher
import PartDesignGui
import ProfileLib.RegularPolygon
import math

# =============================================================================
# JIS B 1180 PARAMETERS - M14 (※21 New JIS)
# =============================================================================
D = 14             # Nominal diameter (mm)
PITCH = 2.0        # Thread pitch (mm)
AF = 21            # Across flats - hex head S (mm) - New JIS ※21
K = 8.62           # Head height max (mm)
L = 70             # Default shaft length (mm) - adjust as needed

# Thread geometry
if L <= 125:
    THREAD_LENGTH = 2 * D + 6
else:
    THREAD_LENGTH = 2 * D + 12

H = 0.866025 * PITCH
THREAD_DEPTH = 0.6134 * PITCH
RADIUS = D / 2
CHAMFER = 0.1 * D


def create_bolt():
    """Create M14 bolt with threads and hex head"""
    
    try:
        doc = App.ActiveDocument
        if doc is None:
            doc = App.newDocument('M14_Bolt')
    except:
        doc = App.newDocument('M14_Bolt')
    
    App.setActiveDocument(doc.Name)
    
    print("Creating M14 bolt...")
    
    # PART 1: Create Body
    body = doc.addObject('PartDesign::Body', 'Body')
    body.Label = 'M14_Shaft'
    doc.recompute()
    
    # PART 2: Cylinder Sketch
    sketch = body.newObject('Sketcher::SketchObject', 'Sketch')
    sketch.AttachmentSupport = (doc.getObject('YZ_Plane'), [''])
    sketch.MapMode = 'FlatFace'
    doc.recompute()
    
    geoList = [Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), RADIUS)]
    sketch.addGeometry(geoList, False)
    sketch.addConstraint(Sketcher.Constraint('Diameter', 0, D))
    sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))
    doc.recompute()
    
    # PART 3: Pad Cylinder
    pad = body.newObject('PartDesign::Pad', 'Pad')
    pad.Profile = (sketch, [''])
    pad.Length = L
    pad.ReferenceAxis = (sketch, ['N_Axis'])
    sketch.Visibility = False
    doc.recompute()
    
    # PART 4: Chamfer
    chamfer = body.newObject('PartDesign::Chamfer', 'Chamfer')
    chamfer.Base = (pad, ['Edge2'])
    chamfer.Size = CHAMFER
    pad.Visibility = False
    doc.recompute()
    
    # PART 5: Thread Profile
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
    
    # PART 6: SubtractiveHelix
    helix = body.newObject('PartDesign::SubtractiveHelix', 'SubtractiveHelix')
    helix.Profile = (thread_sketch, [''])
    helix.ReferenceAxis = (doc.getObject('X_Axis'), [''])
    helix.Pitch = PITCH
    helix.Height = THREAD_LENGTH
    helix.Turns = THREAD_LENGTH / PITCH
    thread_sketch.Visibility = False
    chamfer.Visibility = False
    doc.recompute()
    
    # PART 7: Hex Head Body
    hex_body = doc.addObject('PartDesign::Body', 'HexHead')
    hex_body.Label = 'M14_Head'
    doc.recompute()
    
    hex_sketch = hex_body.newObject('Sketcher::SketchObject', 'HexSketch')
    hex_sketch.AttachmentSupport = (doc.getObject('YZ_Plane001'), [''])
    hex_sketch.MapMode = 'FlatFace'
    doc.recompute()
    
    hex_radius = AF / math.sqrt(3)
    ProfileLib.RegularPolygon.makeRegularPolygon(hex_sketch, 6, App.Vector(0, 0, 0), App.Vector(hex_radius, 0, 0), False)
    hex_sketch.addConstraint(Sketcher.Constraint('Coincident', 6, 3, -1, 1))
    doc.recompute()
    
    # PART 8: Pad Hex Head
    hex_pad = hex_body.newObject('PartDesign::Pad', 'HexPad')
    hex_pad.Profile = (hex_sketch, [''])
    hex_pad.Length = K
    hex_pad.ReferenceAxis = (hex_sketch, ['N_Axis'])
    hex_sketch.Visibility = False
    doc.recompute()
    
    # PART 9: Position Head
    hex_body.Placement = App.Placement(App.Vector(L - K, 0, 0), App.Rotation(App.Vector(0, 0, 1), 0))
    doc.recompute()
    
    print(f"\n{'='*50}")
    print(f"✓ M14 BOLT CREATED (JIS B 1180 - New JIS ※21)")
    print(f"{'='*50}")
    print(f"  Diameter: {D}mm | Length: {L}mm")
    print(f"  Pitch: {PITCH}mm | Thread length: {THREAD_LENGTH}mm")
    print(f"  Hex flat: {AF}mm | Head height: {K}mm")
    print(f"{'='*50}")
    
    return doc


if __name__ == "__main__":
    create_bolt()
