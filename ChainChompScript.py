import maya.cmds as cmds

cmds.polyTorus()
cmds.scale(0.5,0.5,1)

cmds.polyTorus()
cmds.scale(0.5,0.5,1)
cmds.rotate(0,0,90)
cmds.move(0,0,1.5)

cmds.polyTorus()
cmds.scale(0.5,0.5,1)
cmds.move(0,0,3)

cmds.polyTorus()
cmds.scale(0.5,0.5,1)
cmds.rotate(0,0,90)
cmds.move(0,0,4.5)

cmds.polyTorus()
cmds.scale(0.5,0.5,1)
cmds.move(0,.2,6)
cmds.rotate(-10,0,0)

cmds.polyTorus()
cmds.scale(0.5,0.5,1)
cmds.rotate(0,45,90)
cmds.move(0,.75,7.5)

cmds.polyTorus()
cmds.scale(0.5,0.5,1)
cmds.move(0,1.75,8.5)
cmds.rotate(-45,0,0)

cmds.polyTorus()
cmds.scale(0.75,0.75,0.75)
cmds.rotate(0,0,90)
cmds.move(0,2.55,9.4)

cmds.polyCylinder()
cmds.rotate(90)
cmds.scale(1.5,1,1.5)
cmds.move(0,2.55,10.5)

cmds.polySphere()
cmds.scale(2.5,2.5,2.5)
cmds.move(0,2.5,12)

cmds.polySphere()
cmds.move(1.8,3,12.5)

cmds.polySphere()
cmds.move(-1.8,3,12.5)

cmds.polyCone()
cmds.scale(.5,.5,.1)
cmds.move(0,2,14.5)
cmds.rotate(25)

cmds.duplicate()
cmds.move(.5,2,14.5)

cmds.duplicate()
cmds.move(-.5,2,14.5)

cmds.polyCone()
cmds.scale(.5,.5,.1)
cmds.move(0,3,14.5)
cmds.rotate(-195)

cmds.duplicate()
cmds.move(.5,3,14.5)

cmds.duplicate()
cmds.move(-.5,3,14.5)