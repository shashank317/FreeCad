
"""
FreeCAD Assembly script – SteppedRevolution + SteppedTubeWithBoss
Simple positioning approach (no formal joints – just App::Link placements).

Update the 3 paths below before running.
"""

import FreeCAD as App

# ── UPDATE THESE PATHS ─────────────────────────────────────────────────────────
PART1_PATH = r"C:\Users\shashank\Desktop\New folder (4)\A!.FCStd"
PART2_PATH = r"C:\Users\shashank\Desktop\New folder (4)\B!.FCStd"
ASSEMBLY_PATH  = r"C:/Users/shashank/Desktop/New folder (4)/AM.FCStd"
# ──────────────────────────────────────────────────────────────────────────────

V = App.Vector
R = App.Rotation

# ── 1. Create assembly doc and SAVE IT FIRST ──────────────────────────────────
doc = App.newDocument("AM")
App.setActiveDocument(doc.Name)
doc.saveAs(ASSEMBLY_PATH)
doc.recompute()

# ── 2. Open part documents ─────────────────────────────────────────────────────
doc1 = App.openDocument(PART1_PATH)
doc2 = App.openDocument(PART2_PATH)
App.setActiveDocument(doc.Name)

# ── 3. Create a Part container for the assembly ───────────────────────────────
asm = doc.addObject('App::Part', 'Assembly')
doc.recompute()

# ── 4. Link Part1 – grounded at origin ────────────────────────────────────────
link1 = doc.addObject('App::Link', 'SteppedRevolution')
link1.LinkedObject = doc1.getObject('Body')
link1.Placement    = App.Placement(V(0, 0, 0), R())
asm.addObject(link1)
doc.recompute()

# ── 5. Link Part2 – position as needed ────────────────────────────────────────
# Adjust placement to align with Part1
# Part1 revolves around X-axis (H_Axis), Part2 also around X-axis
# Offset Part2 to sit adjacent or coaxial as designed
link2 = doc.addObject('App::Link', 'SteppedTubeWithBoss')
link2.LinkedObject = doc2.getObject('Body')
link2.Placement    = App.Placement(
    V(0, 0, 0),      # Adjust X/Y/Z offset as needed
    R()              # No rotation needed if both use same axis orientation
)
asm.addObject(link2)
doc.recompute()

# ── 6. Save ────────────────────────────────────────────────────────────────────
doc.save()

print("=" * 50)
print("Assembly saved → AM.FCStd")
print("  Part1: SteppedRevolution")
print("  Part2: SteppedTubeWithBoss")
print()
print("Adjust link2.Placement manually in FreeCAD to")
print("position Part2 relative to Part1 as needed.")
print("=" * 50)