Python 3.11.13 | packaged by conda-forge | (main, Jun  4 2025, 14:39:58) [MSC v.1943 64 bit (AMD64)] on win32
Type 'help', 'copyright', 'credits' or 'license' for more information.
>>> ### Begin command Std_New
>>> App.newDocument()
>>> # App.setActiveDocument("Unnamed")
>>> # App.ActiveDocument=App.getDocument("Unnamed")
>>> # Gui.ActiveDocument=Gui.getDocument("Unnamed")
>>> # Gui.activeDocument().activeView().viewDefaultOrientation()
>>> ### End command Std_New
>>> ### Begin command PartDesign_Body
>>> App.activeDocument().addObject('PartDesign::Body','Body')
>>> App.ActiveDocument.getObject('Body').Label = 'Body'
>>> # import PartDesignGui
>>> # Gui.activateView('Gui::View3DInventor', True)
>>> # Gui.activeView().setActiveObject('pdbody', App.activeDocument().Body)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection(App.ActiveDocument.Body)
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_Body
>>> # Gui.Selection.addSelection('Unnamed','Body')
>>> # Gui.runCommand('Std_OrthographicCamera',1)
>>> ### Begin command Std_New
>>> App.newDocument()
>>> # App.setActiveDocument("Unnamed1")
>>> # App.ActiveDocument=App.getDocument("Unnamed1")
>>> # Gui.ActiveDocument=Gui.getDocument("Unnamed1")
>>> # Gui.activeDocument().activeView().viewDefaultOrientation()
>>> ### End command Std_New
>>> # App.setActiveDocument("Unnamed")
>>> # App.ActiveDocument=App.getDocument("Unnamed")
>>> # Gui.ActiveDocument=Gui.getDocument("Unnamed")
>>> App.closeDocument("Unnamed1")
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('PartDesign_NewSketch',0)
>>> # Gui.Selection.addSelection('Unnamed','Body','Origin.XZ_Plane.',21.7928,-3.8743e-06,32.5)
>>> App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
>>> App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('XZ_Plane'),[''])
>>> App.getDocument('Unnamed').getObject('Sketch').MapMode = 'FlatFace'
>>> App.ActiveDocument.recompute()
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Sketch.')
>>> # import Show
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CreatePolyline',0)
>>> # Gui.runCommand('Sketcher_CreateLine',0)
>>> # Gui.runCommand('Sketcher_CreateLine',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(0.000000, 62.173054, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> constraintList = []
>>> constraintList.append(Sketcher.Constraint('Coincident', 0, 1, -1, 1))
>>> constraintList.append(Sketcher.Constraint('PointOnObject', 0, 2, -2))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
>>> del constraintList
>>> 
>>> # Gui.runCommand('Sketcher_CreateLine',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(0.000000, 62.173054, 0.000000),App.Vector(25.626390, 61.817532, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> constraintList = []
>>> constraintList.append(Sketcher.Constraint('Coincident', 1, 1, 0, 2))
>>> constraintList.append(Sketcher.Constraint('Horizontal', 1))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
>>> del constraintList
>>> 
>>> # Gui.runCommand('Sketcher_CreateLine',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(25.626390, 62.173054, 0.000000),App.Vector(25.981905, 104.835182, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> constraintList = []
>>> constraintList.append(Sketcher.Constraint('Coincident', 2, 1, 1, 2))
>>> constraintList.append(Sketcher.Constraint('Vertical', 2))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
>>> del constraintList
>>> 
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(25.626390, 104.835197, 0.000000),App.Vector(81.087143, 104.835182, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal', 3))
>>> 
>>> 
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(81.087143, 104.835182, 0.000000),App.Vector(80.731636, 90.969986, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> constraintList = []
>>> constraintList.append(Sketcher.Constraint('Coincident', 4, 1, 3, 2))
>>> constraintList.append(Sketcher.Constraint('Vertical', 4))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
>>> del constraintList
>>> 
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(81.087143, 90.969986, 0.000000),App.Vector(177.076935, 91.681023, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> constraintList = []
>>> constraintList.append(Sketcher.Constraint('Coincident', 5, 1, 4, 2))
>>> constraintList.append(Sketcher.Constraint('Horizontal', 5))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
>>> del constraintList
>>> 
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(177.076935, 90.969994, 0.000000),App.Vector(176.721420, 69.994438, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical', 6))
>>> 
>>> 
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(177.076935, 69.994446, 0.000000),App.Vector(262.401184, 70.705482, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal', 7))
>>> 
>>> 
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(262.401184, 69.994453, 0.000000),App.Vector(263.112213, 0.000000, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> constraintList = []
>>> constraintList.append(Sketcher.Constraint('PointOnObject', 8, 2, -1))
>>> constraintList.append(Sketcher.Constraint('Vertical', 8))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
>>> del constraintList
>>> 
>>> # Gui.runCommand('Sketcher_CreateLine',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(0.000000, 47.952339, 0.000000),App.Vector(263.112213, 48.307861, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> constraintList = []
>>> constraintList.append(Sketcher.Constraint('PointOnObject', 9, 1, 0))
>>> constraintList.append(Sketcher.Constraint('PointOnObject', 9, 2, 8))
>>> constraintList.append(Sketcher.Constraint('Horizontal', 9))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
>>> del constraintList
>>> 
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> App.ActiveDocument.recompute()
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.')
>>> App.getDocument('Unnamed').recompute()
>>> ### Begin command Sketcher_EditSketch
>>> # Gui.activeDocument().setEdit('Sketch')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> ### End command Sketcher_EditSketch
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_ConstrainTangent',0)
>>> # Gui.runCommand('Sketcher_Trimming',0)
>>> # Gui.runCommand('Sketcher_CompCurveEdition',0)
>>> App.getDocument('Unnamed').getObject('Sketch').trim(0,App.Vector(1.226388,17.764242,0))
>>> App.ActiveDocument.recompute()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> ### Begin command Sketcher_EditSketch
>>> # Gui.activeDocument().setEdit('Sketch')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> ### End command Sketcher_EditSketch
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CompCurveEdition',0)
>>> App.getDocument('Unnamed').getObject('Sketch').trim(8,App.Vector(263.112213,30.353939,0))
>>> # Gui.runCommand('Sketcher_Dimension',0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,0,2,14.220715)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',0,53.4465,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',0,1,0,2,14.220715)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,0,2,14.220715)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',0,1,0,2,14.220715)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',8,1,0,263.112213)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge9',263.112,51.704,0)
>>> App.getDocument('Unnamed').getObject('Sketch').setDatum(16,App.Units.Quantity('160.000000 mm'))
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Std_Undo',0)
>>> # Gui.runCommand('Sketcher_CompDimensionTools',0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',9,1,9,2,263.112213)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge10',131.556,47.9523,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',9,1,9,2,263.112213)) 
>>> App.getDocument('Unnamed').getObject('Sketch').setDatum(16,App.Units.Quantity('160.000000 mm'))
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,-1,1,91.027959)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex1',77.3735,47.9523,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,0,1,47.952339)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,-1,1,91.027959)) 
>>> # Gui.Selection.clearSelection()
>>> App.ActiveDocument.recompute()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> ### Begin command Sketcher_EditSketch
>>> # Gui.activeDocument().setEdit('Sketch')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> ### End command Sketcher_EditSketch
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Sketch').movePoint(0,1,App.Vector(-0.050763,40.366577,0),0)
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex1',-0.050763,-0.0110048,40.3666,False)
>>> App.ActiveDocument.recompute()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> ### Begin command Sketcher_EditSketch
>>> # Gui.activeDocument().setEdit('Sketch')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> ### End command Sketcher_EditSketch
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',81.0871,-0.00801184,99.2732,False)
>>> App.getDocument('Unnamed').getObject('Sketch').movePoint(4,0,App.Vector(-22.365151,-10.019310,0),1)
>>> App.getDocument('Unnamed').getObject('Sketch').movePoint(2,2,App.Vector(25.626390,94.815880,0),0)
>>> App.getDocument('Unnamed').getObject('Sketch').movePoint(6,1,App.Vector(177.076935,80.950684,0),0)
>>> App.getDocument('Unnamed').getObject('Sketch').movePoint(6,0,App.Vector(-72.614647,-0.435623,0),1)
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex13',104.462,-0.0140096,80.5151,False)
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',106.013,-0.00800965,80.9507,False)
>>> ### Begin command Sketcher_ConstrainCoincidentUnified
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject',6,1,4))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject',6,1,5))
>>> ### End command Sketcher_ConstrainCoincidentUnified
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',72.0869,-0.00800936,78.4916,False)
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Sketch').delGeometries([6])
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',186.122,-0.00800835,69.9945,False)
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Sketch').delGeometries([6])
>>> App.getDocument('Unnamed').getObject('Sketch').movePoint(5,2,App.Vector(90.052238,85.207718,0),0)
>>> App.getDocument('Unnamed').getObject('Sketch').movePoint(3,2,App.Vector(57.639561,96.887970,0),0)
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',29.315,-0.00801155,96.888,False)
>>> # Gui.Selection.clearSelection()
>>> App.ActiveDocument.recompute()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> ### Begin command Sketcher_EditSketch
>>> # Gui.activeDocument().setEdit('Sketch')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> ### End command Sketcher_EditSketch
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex6',25.6264,-0.0140113,94.8159,False)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex6',25.6264,-0.0140113,94.8159,False)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex7',25.6264,-0.0140116,96.888,False)
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex6',25.6264,-0.0140113,94.8159,False)
>>> ### Begin command Sketcher_ConstrainCoincidentUnified
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',3,1,2,2))
>>> ### End command Sketcher_ConstrainCoincidentUnified
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CreateLine',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(90.052238, 85.207718, 0.000000),App.Vector(89.949966, 71.303963, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> constraintList = []
>>> constraintList.append(Sketcher.Constraint('Coincident', 8, 1, 5, 2))
>>> constraintList.append(Sketcher.Constraint('Vertical', 8))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
>>> del constraintList
>>> 
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(90.052238, 71.303963, 0.000000),App.Vector(159.982025, 71.464218, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> constraintList = []
>>> constraintList.append(Sketcher.Constraint('Coincident', 9, 1, 8, 2))
>>> constraintList.append(Sketcher.Constraint('Horizontal', 9))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
>>> del constraintList
>>> 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex20',159.982,-0.0140085,71.304,False)
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex13',159.949,-0.0140083,69.9945,False)
>>> # Gui.Selection.removeSelection('Unnamed','Body','Sketch.Vertex13')
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex13',159.949,-0.0140083,69.9945,False)
>>> ### Begin command Sketcher_ConstrainCoincidentUnified
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',9,2,6,1))
>>> ### End command Sketcher_ConstrainCoincidentUnified
>>> # Gui.Selection.clearSelection()
>>> App.ActiveDocument.recompute()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> ### Begin command Sketcher_EditSketch
>>> # Gui.activeDocument().setEdit('Sketch')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> ### End command Sketcher_EditSketch
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Constraint15',84.0484,-0.00899428,-48.0113,False)
>>> App.getDocument('Unnamed').getObject('Sketch').setDatum(14,App.Units.Quantity('160.500000 mm'))
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CompDimensionTools',0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',8,1,8,2,13.903755)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge9',90.0522,77.4478,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',8,2,8,1,13.903755)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',8,1,8,2,13.903755)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',8,2,8,1,13.903755)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',8,1,8,2,13.903755)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Angle',0,2,8,1,0.008593)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',-0.0595849,55.2389,0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CompDimensionTools',0)
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',-0.104802,-0.00800596,49.9768,False)
>>> ### Begin command Sketcher_ConstrainVertical
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',0))
>>> ### End command Sketcher_ConstrainVertical
>>> # Gui.Selection.clearSelection()
>>> App.ActiveDocument.recompute()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> ### Begin command Sketcher_EditSketch
>>> # Gui.activeDocument().setEdit('Sketch')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> ### End command Sketcher_EditSketch
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CompDimensionTools',0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,0,2,21.806477)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',0,51.2698,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',0,1,0,2,21.806477)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,0,2,21.806477)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',8,1,0,90.052238)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge9',90.0522,76.0658,0)
>>> App.getDocument('Unnamed').getObject('Sketch').setDatum(22,App.Units.Quantity('100.500000 mm'))
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CompDimensionTools',0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,1,4,2,11.680252)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',57.6396,88.7143,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',4,2,4,1,11.680252)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,1,4,2,11.680252)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',-2,1,4,57.639561)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.V_Axis',0,72.5962,0)
>>> App.getDocument('Unnamed').getObject('Sketch').setDatum(23,App.Units.Quantity('33.000000 mm'))
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CompDimensionTools',0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,1,2,2,34.714916)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',25.6264,79.5305,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',2,1,2,2,34.714916)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,1,2,2,34.714916)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,2,25.626390)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',0,51.2698,0)
>>> App.getDocument('Unnamed').getObject('Sketch').setDatum(24,App.Units.Quantity('13.000000 mm'))
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CompDimensionTools',0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',9,1,9,2,60.000000)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge10',147.332,71.304,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',9,1,9,2,60.000000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',9,1,9,2,60.000000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',9,1,9,2,60.000000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',-1,1,9,71.303963)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.H_Axis',149.946,0,0)
>>> App.getDocument('Unnamed').getObject('Sketch').setDatum(25,App.Units.Quantity('32.500000 mm'))
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Sketch').movePoint(7,0,App.Vector(0.435623,-23.094339,0),1)
>>> App.ActiveDocument.recompute()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',55.2541,-1.01576e-05,85.2077)
>>> ### Begin command Sketcher_EditSketch
>>> # Gui.activeDocument().setEdit('Sketch')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> ### End command Sketcher_EditSketch
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CompDimensionTools',0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,1,5,2,67.500000)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',82.4187,85.2077,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',5,1,5,2,67.500000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,1,5,2,67.500000)) 
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CompDimensionTools',0)
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.H_Axis',98.5367,0,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,1,-1,85.207718)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',80.2406,85.2077,0)
>>> App.getDocument('Unnamed').getObject('Sketch').setDatum(26,App.Units.Quantity('45.000000 mm'))
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Sketch').movePoint(3,0,App.Vector(-0.697140,-19.071625,0),1)
>>> App.getDocument('Unnamed').getObject('Sketch').movePoint(5,0,App.Vector(1.728790,28.895744,0),1)
>>> App.ActiveDocument.recompute()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','',70.604,-5.36442e-06,45)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',33,-7.81784e-06,65.5808)
>>> ### Begin command Sketcher_EditSketch
>>> # Gui.activeDocument().setEdit('Sketch')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> ### End command Sketcher_EditSketch
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CompDimensionTools',0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1,3,2,20.000000)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',23,77.8163,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',3,1,3,2,20.000000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1,3,2,20.000000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',-1,1,3,77.816345)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.H_Axis',82.8543,0,0)
>>> App.getDocument('Unnamed').getObject('Sketch').setDatum(27,App.Units.Quantity('50.000000 mm'))
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,1,2,13.000000)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',5.74921,62.1731,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',1,1,1,2,13.000000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,1,2,13.000000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',-1,1,1,62.173054)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.H_Axis',-79.1971,0,0)
>>> App.getDocument('Unnamed').getObject('Sketch').setDatum(28,App.Units.Quantity('25.000000 mm'))
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',7,1,7,2,160.500000)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',58.0239,17.2722,0)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',7,1,7,2,160.500000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',7,1,7,2,160.500000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',-1,1,7,17.272238)) 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.H_Axis',-100.978,0,0)
>>> App.getDocument('Unnamed').getObject('Sketch').setDatum(29,App.Units.Quantity('20.000000 mm'))
>>> # Gui.Selection.clearSelection()
>>> ### Begin command Sketcher_LeaveSketch
>>> # Gui.activeDocument().resetEdit()
>>> App.ActiveDocument.recompute()
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> App.ActiveDocument.recompute()
>>> ### End command Sketcher_LeaveSketch
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.')
>>> ### Begin command PartDesign_Revolution
>>> App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Revolution','Revolution')
>>> App.getDocument('Unnamed').getObject('Revolution').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
>>> App.getDocument('Unnamed').getObject('Revolution').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'),['V_Axis'])
>>> App.getDocument('Unnamed').getObject('Revolution').Angle = 360.0
>>> App.getDocument('Unnamed').getObject('Revolution').Reversed = 1
>>> App.getDocument('Unnamed').getObject('Sketch').Visibility = False
>>> App.ActiveDocument.recompute()
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Revolution').ViewObject.ShapeAppearance)
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Revolution').ViewObject.LineColor)
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Revolution').ViewObject.PointColor)
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Revolution').ViewObject.Transparency)
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Revolution').ViewObject.DisplayMode)
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Revolution.')
>>> # Gui.Selection.clearSelection()
>>> ### End command PartDesign_Revolution
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Origin.X_Axis.',126.036,0,0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Origin.Y_Axis.',0,-202.501,0)
>>> App.getDocument('Unnamed').recompute()
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge10',56.1036,-2.38419e-06,20)
>>> ### Begin command PartDesign_Revolution
>>> App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Revolution','Revolution')
>>> App.getDocument('Unnamed').getObject('Revolution').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['Edge10',])
>>> App.getDocument('Unnamed').getObject('Revolution').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'),['V_Axis'])
>>> App.getDocument('Unnamed').getObject('Revolution').Angle = 360.0
>>> App.getDocument('Unnamed').getObject('Sketch').Visibility = False
>>> App.ActiveDocument.recompute()
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Revolution').ViewObject.ShapeAppearance)
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Revolution').ViewObject.LineColor)
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Revolution').ViewObject.PointColor)
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Revolution').ViewObject.Transparency)
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Revolution').ViewObject.DisplayMode)
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Revolution.')
>>> # Gui.Selection.clearSelection()
>>> ### End command PartDesign_Revolution
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Origin.X_Axis.',28.154,0,0)
>>> App.getDocument('Unnamed').recompute()
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> # Gui.runCommand('PartDesign_Revolution',0)
>>> # Gui.runCommand('PartDesign_Revolution',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body')
>>> # Gui.runCommand('PartDesign_Revolution',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.')
>>> ### Begin command PartDesign_Revolution
>>> App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Revolution','Revolution')
>>> App.getDocument('Unnamed').getObject('Revolution').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
>>> App.getDocument('Unnamed').getObject('Revolution').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'),['V_Axis'])
>>> App.getDocument('Unnamed').getObject('Revolution').Angle = 360.0
>>> App.getDocument('Unnamed').getObject('Revolution').Reversed = 1
>>> App.getDocument('Unnamed').getObject('Sketch').Visibility = False
>>> App.ActiveDocument.recompute()
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Revolution').ViewObject.ShapeAppearance)
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Revolution').ViewObject.LineColor)
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Revolution').ViewObject.PointColor)
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Revolution').ViewObject.Transparency)
>>> # App.getDocument('Unnamed').getObject('Revolution').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Revolution').ViewObject.DisplayMode)
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Revolution.')
>>> # Gui.Selection.clearSelection()
>>> ### End command PartDesign_Revolution
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Revolution').Angle = 360.000000
>>> App.getDocument('Unnamed').getObject('Revolution').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'), ['H_Axis'])
>>> App.getDocument('Unnamed').getObject('Revolution').Midplane = 0
>>> App.getDocument('Unnamed').getObject('Revolution').Reversed = 0
>>> App.getDocument('Unnamed').getObject('Revolution').Type = 0
>>> App.getDocument('Unnamed').getObject('Revolution').UpToFace = None
>>> App.getDocument('Unnamed').recompute()
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> App.getDocument('Unnamed').getObject('Sketch').Visibility = False
>>> ### Begin command Std_New
>>> App.newDocument()
>>> # App.setActiveDocument("Unnamed1")
>>> # App.ActiveDocument=App.getDocument("Unnamed1")
>>> # Gui.ActiveDocument=Gui.getDocument("Unnamed1")
>>> # Gui.activeDocument().activeView().viewDefaultOrientation()
>>> ### End command Std_New
>>> # App.setActiveDocument("Unnamed")
>>> # App.ActiveDocument=App.getDocument("Unnamed")
>>> # Gui.ActiveDocument=Gui.getDocument("Unnamed")
>>> # App.setActiveDocument("Unnamed1")
>>> # App.ActiveDocument=App.getDocument("Unnamed1")
>>> # Gui.ActiveDocument=Gui.getDocument("Unnamed1")
>>> 