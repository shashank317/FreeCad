import FreeCAD as App
import Part
import Sketcher

# Create new document
doc = App.newDocument("SteppedShaft")

# Create Body
body = doc.addObject("PartDesign::Body", "Body")

# Create Sketch on XZ Plane
sketch = body.newObject("Sketcher::SketchObject", "Sketch")
sketch.Support = (body.Origin.OriginFeatures[3], [''])  # XZ Plane
sketch.MapMode = "FlatFace"

doc.recompute()

# -------------------------
# Create Construction Axis
# -------------------------
centerline = Part.LineSegment(App.Vector(0, 0, 0), App.Vector(0, 120, 0))
sketch.addGeometry(centerline, True)
sketch.addConstraint(Sketcher.Constraint('Vertical', 0))

# -------------------------
# Profile Geometry (Right side only)
# -------------------------

geo = []

# Step 1
geo.append(Part.LineSegment(App.Vector(0,0,0), App.Vector(25,0,0)))
geo.append(Part.LineSegment(App.Vector(25,0,0), App.Vector(25,20,0)))

# Step 2
geo.append(Part.LineSegment(App.Vector(25,20,0), App.Vector(40,20,0)))
geo.append(Part.LineSegment(App.Vector(40,20,0), App.Vector(40,50,0)))

# Step 3
geo.append(Part.LineSegment(App.Vector(40,50,0), App.Vector(30,50,0)))
geo.append(Part.LineSegment(App.Vector(30,50,0), App.Vector(30,80,0)))

# Close Profile
geo.append(Part.LineSegment(App.Vector(30,80,0), App.Vector(0,80,0)))
geo.append(Part.LineSegment(App.Vector(0,80,0), App.Vector(0,0,0)))

sketch.addGeometry(geo, False)

# -------------------------
# Constraints
# -------------------------

# Horizontal constraints
sketch.addConstraint(Sketcher.Constraint('Horizontal', 1))
sketch.addConstraint(Sketcher.Constraint('Horizontal', 3))
sketch.addConstraint(Sketcher.Constraint('Horizontal', 5))
sketch.addConstraint(Sketcher.Constraint('Horizontal', 7))

# Vertical constraints
sketch.addConstraint(Sketcher.Constraint('Vertical', 2))
sketch.addConstraint(Sketcher.Constraint('Vertical', 4))
sketch.addConstraint(Sketcher.Constraint('Vertical', 6))
sketch.addConstraint(Sketcher.Constraint('Vertical', 8))

# Coincident constraints (connect profile)
for i in range(1,8):
    sketch.addConstraint(Sketcher.Constraint('Coincident', i, 2, i+1, 1))

# Coincident to axis bottom
sketch.addConstraint(Sketcher.Constraint('Coincident', 8, 2, 1, 1))

doc.recompute()

# -------------------------
# Revolution
# -------------------------

revolve = body.newObject("PartDesign::Revolution", "Revolution")
revolve.Profile = sketch
revolve.ReferenceAxis = (sketch, ['Edge1'])  # centerline
revolve.Angle = 360

doc.recompute()

print("Component Created Successfully")