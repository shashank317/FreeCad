"""
FreeCAD script – Stepped Revolution Component
Cleaned and reconstructed from console log.

Profile is a closed staircase polygon revolved 360° around the Y-axis (V_Axis).

Key dimensions (from final setDatum constraints in original session):
  Radii (X mm): 0 | 13 | 33 | 100.5 | 160.5
  Heights (Y mm): 0 | 20 | 25 | 32.5 | 45 | 50

Run via FreeCAD Python console or macro editor:
    exec(open('c:/Users/shashank/Desktop/New folder (4)/claude.py').read())
"""

import FreeCAD as App
import Part
import Sketcher
import PartDesignGui


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

    # ── Document & Body ─────────────────────────────────────────────────────
    body = doc.addObject('PartDesign::Body', 'Body')
    body.Label = 'Body'
    doc.recompute()

    # ── Sketch on XY Plane ──────────────────────────────────────────────────
    sketch = body.newObject('Sketcher::SketchObject', 'Profile')
    sketch.AttachmentSupport = (doc.getObject('XY_Plane'), [''])
    sketch.MapMode = 'FlatFace'
    doc.recompute()

    # ── Profile geometry ────────────────────────────────────────────────────
    # Closed staircase polygon. X = radius, Y = height.
    # Reading counterclockwise from origin:
    #
    #        Y
    #   50 ──┤ ██
    #   45 ──┤ ████████
    #   32.5─┤ ████████████████
    #   25 ──┤ █
    #   20 ──┤ ████████████████████
    #    0 ──┼─────────────────────── X
    #        0  13  33     100.5  160.5

    V = App.Vector

    segments = [
        (V(0,     0,    0), V(0,     25,   0)),  # 0  – axis left, y: 0 → 25
        (V(0,     25,   0), V(13,    25,   0)),  # 1  – shelf @ y=25, w=13
        (V(13,    25,   0), V(13,    50,   0)),  # 2  – step up, y: 25 → 50
        (V(13,    50,   0), V(33,    50,   0)),  # 3  – shelf @ y=50, w=20
        (V(33,    50,   0), V(33,    45,   0)),  # 4  – step down, y: 50 → 45
        (V(33,    45,   0), V(100.5, 45,   0)),  # 5  – shelf @ y=45, w=67.5
        (V(100.5, 45,   0), V(100.5, 32.5, 0)),  # 6  – step down, y: 45 → 32.5
        (V(100.5, 32.5, 0), V(160.5, 32.5, 0)),  # 7  – shelf @ y=32.5, w=60
        (V(160.5, 32.5, 0), V(160.5, 20,   0)),  # 8  – outer wall, y: 32.5 → 20
        (V(160.5, 20,   0), V(0,     20,   0)),  # 9  – base @ y=20, back to axis
        (V(0,     20,   0), V(0,     0,    0)),  # 10 – axis right, y: 20 → 0
    ]

    for p1, p2 in segments:
        sketch.addGeometry(Part.LineSegment(p1, p2), False)
    doc.recompute()

    # ── Close the polygon (coincident constraints) ──────────────────────────
    n = len(segments)
    for i in range(n):
        sketch.addConstraint(Sketcher.Constraint('Coincident', i, 2, (i + 1) % n, 1))
    doc.recompute()

    # ── Lock origin ─────────────────────────────────────────────────────────
    sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))
    doc.recompute()

    # ── Horizontal / vertical direction constraints ─────────────────────────
    for i in [0, 2, 4, 6, 8, 10]:
        sketch.addConstraint(Sketcher.Constraint('Vertical', i))
    for i in [1, 3, 5, 7, 9]:
        sketch.addConstraint(Sketcher.Constraint('Horizontal', i))
    doc.recompute()

    # ── Dimensional constraints ─────────────────────────────────────────────
    # Y shelf heights
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 1,  1,  25.0))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 3,  1,  50.0))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 5,  1,  45.0))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 7,  1,  32.5))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 9,  1,  20.0))

    # X step radii
    sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 1,  2,  13.0))
    sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 3,  2,  33.0))
    sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 5,  2,  100.5))
    sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 7,  2,  160.5))
    doc.recompute()

    sketch.Visibility = False
    doc.recompute()

    # ── Revolution (360° around H_Axis / Base X axis in XY plane) ─────────
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

    print(f"\n{'='*50}")
    print("SteppedRevolution created successfully.")
    print(f"{'='*50}")
    print("  Radii (X mm): 0 | 13 | 33 | 100.5 | 160.5")
    print("  Heights (Y mm): 0 | 20 | 25 | 32.5 | 45 | 50")
    print(f"{'='*50}")

    return doc


if __name__ == "__main__":
    create_stepped_revolution()