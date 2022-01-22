#
import maya.cmds as cmds
project_Name = "Ciervo"
#project name declaration

def LocatorPlacement(locName,x,y,z):
    proxyLoc = cmds.spaceLocator(n=locName)
    cmds.setAttr(proxyLoc[0]+'.translateX',x)
    cmds.setAttr(proxyLoc[0]+'.translateY',y)
    cmds.setAttr(proxyLoc[0]+'.translateZ',z)

#locators attributes and creates joints from it...

def jointAttr(locatorName):
    xatrr = cmds.getAttr(locatorName + '.tx')
    yattr = cmds.getAttr(locatorName + '.ty')
    zattr = cmds.getAttr(locatorName + '.tz')
    AttrList=[xatrr,yattr,zattr]
    return AttrList

#Lock attributes...

def AttrlockAndHide(ctrlName,t,r,s):
    if t==1:
        cmds.setAttr(ctrlName + '.tx', l=1, k=0, cb=0)
        cmds.setAttr(ctrlName + '.ty', l=1, k=0, cb=0)
        cmds.setAttr(ctrlName + '.tz', l=1, k=0, cb=0)
    if r == 1:
        cmds.setAttr(ctrlName + '.rx', l=1, k=0, cb=0)
        cmds.setAttr(ctrlName + '.ry', l=1, k=0, cb=0)
        cmds.setAttr(ctrlName + '.rz', l=1, k=0, cb=0)
    if s == 1:
        cmds.setAttr(ctrlName + '.sx', l=1, k=0, cb=0)
        cmds.setAttr(ctrlName + '.sy', l=1, k=0, cb=0)
        cmds.setAttr(ctrlName + '.sz', l=1, k=0, cb=0)

    cmds.setAttr(ctrlName + '.visibility', l=1, k=0, cb=0)


#controls
def controlType( ctrlType,ctrlName,scale,parentGrpName):
    if ctrlType == 'circle':
        circleCtrl = cmds.circle(n = ctrlName)
        cmds.scale(scale,scale,scale,circleCtrl[0]+'.cv[0:7]')
        cmds.group(ctrlName,n=parentGrpName)
    #custom controllers
    elif ctrlType == 'headctrl':
        headCtrl = cmds.curve(p=[[19.262, -14.197, -25.073], [19.262, 26.259, -22.738], [10.449, -8.743, 25.073],
                                 [10.449, -26.259, 16.924], [19.262, -14.197, -25.073], [-19.262, -14.197, -25.073],
                                 [-10.449, -26.259, 16.924], [-10.449, -8.743, 25.073], [-19.262, 26.259, -22.738],
                                 [19.262, 26.259, -22.738], [10.449, -8.743, 25.073], [-10.449, -8.743, 25.073],
                                 [-10.449, -26.259, 16.924], [10.449, -26.259, 16.924], [19.262, -14.197, -25.073],
                                 [-19.262, -14.197, -25.073], [-19.262, 26.259, -22.738], [19.262, 26.259, -22.738],
                                 [19.262, -14.197, -25.073]], d=1, n=ctrlName)
        cmds.scale(scale, scale, scale, headCtrl + '.cv[0:18]')
        cmds.group(ctrlName, n=parentGrpName)

    elif ctrlType == 'neckctrl':
        neckCtrl = cmds.curve(
            p=[[18.12, 14.956, -19.068], [18.12, 26.738, -1.859], [15.853, -17.751, 19.068], [15.853, -26.738, 12.981],
               [18.12, 14.956, -19.068], [-18.12, 14.956, -19.068], [-15.853, -26.738, 12.981],
               [-15.853, -17.751, 19.068], [-18.12, 26.738, -1.859], [18.12, 26.738, -1.859], [15.853, -17.751, 19.068],
               [-15.853, -17.751, 19.068], [-15.853, -26.738, 12.981], [15.853, -26.738, 12.981],
               [18.12, 14.956, -19.068], [-18.12, 14.956, -19.068], [-18.12, 26.738, -1.859], [18.12, 26.738, -1.859],
               [18.12, 14.956, -19.068]], d=1, n=ctrlName)
        cmds.scale(scale, scale, scale, neckCtrl + '.cv[0:18]')
        cmds.group(ctrlName, n=parentGrpName)

    elif ctrlType == 'chestctrl':
        chestCtrl = cmds.curve(
        p=[[20.796, 32.941, -30.149], [21.737, 40.632, -1.271], [22.048, -29.792, 29.948], [32.144, -42.137, -22.31],
           [20.796, 32.941, -30.149], [-20.796, 32.941, -30.149], [-32.144, -42.137, -22.31],
           [-22.048, -29.792, 29.948], [-21.737, 40.632, -1.271], [21.737, 40.632, -1.271], [22.048, -29.792, 29.948],
           [-22.048, -29.792, 29.948], [-32.144, -42.137, -22.31], [32.144, -42.137, -22.31], [20.796, 32.941, -30.149],
           [-20.796, 32.941, -30.149], [-21.737, 40.632, -1.271], [21.737, 40.632, -1.271], [20.796, 32.941, -30.149]],
        d=1, n=ctrlName)
        cmds.scale(scale, scale, scale,chestCtrl+ '.cv[0:18]')
        cmds.group(ctrlName, n=parentGrpName)

    elif ctrlType == 'flankctrl':
        flankCtrl = cmds.curve(
            p=[[19.2, 36.081, -17.951], [19.2, 37.638, 15.2], [32.294, -37.638, 17.951], [27.881, -35.27, -10.146],
               [19.2, 36.081, -17.951], [-19.2, 36.081, -17.951], [-27.881, -35.27, -10.146],
               [-32.294, -37.638, 17.951], [-19.2, 37.638, 15.2], [19.2, 37.638, 15.2], [32.294, -37.638, 17.951],
               [-32.294, -37.638, 17.951], [-27.881, -35.27, -10.146], [27.881, -35.27, -10.146],
               [19.2, 36.081, -17.951], [-19.2, 36.081, -17.951], [-19.2, 37.638, 15.2], [19.2, 37.638, 15.2],
               [19.2, 36.081, -17.951]], d=1 , n = ctrlName)
        cmds.scale(scale, scale, scale, flankCtrl + '.cv[0:18]')
        cmds.group(ctrlName, n=parentGrpName)

    elif ctrlType == 'hipctrl':
        hipCtrl = cmds.curve(
            p=[[15.402, 29.487, -18.646], [17.358, 36.334, 16.723], [28.009, -36.334, 28.796],
               [24.03, -21.177, -28.796], [15.402, 29.487, -18.646], [-15.399, 29.487, -18.646],
               [-24.03, -21.177, -28.796], [-28.009, -36.334, 28.796], [-17.358, 36.334, 16.723],
               [17.358, 36.334, 16.723], [28.009, -36.334, 28.796], [-28.009, -36.334, 28.796],
               [-24.03, -21.177, -28.796], [24.03, -21.177, -28.796], [15.402, 29.487, -18.646],
               [-15.399, 29.487, -18.646], [-17.358, 36.334, 16.723], [17.358, 36.334, 16.723],
               [15.402, 29.487, -18.646]], d=1,n = ctrlName)
        cmds.scale(scale, scale, scale, hipCtrl + '.cv[0:18]')
        cmds.group(ctrlName, n=parentGrpName)


    elif ctrlType == 'legIkctrl':
        legctrl = cmds.curve(p=[[-0.871, 1.528, -0.081], [-1.26, -1.528, 1.609], [1.26, -1.528, 1.609], [0.871, 1.528, -0.081],
                 [-0.871, 1.528, -0.081], [-0.57, 1.528, -1.493], [-0.908, -1.528, -1.609], [-1.26, -1.528, 1.609],
                 [1.26, -1.528, 1.609], [0.908, -1.528, -1.609], [0.57, 1.528, -1.493], [0.871, 1.528, -0.081],
                 [-0.871, 1.528, -0.081], [-0.57, 1.528, -1.493], [0.57, 1.528, -1.493], [0.908, -1.528, -1.609],
                 [-0.908, -1.528, -1.609]], d=1,n= ctrlName)
        cmds.scale(scale,scale,scale, legctrl+'.cv[0:16]')
        cmds.group(ctrlName, n=parentGrpName)

    elif ctrlType == 'curvedTwoArrow':
        curvedtwoArrow = cmds.curve(p=[[0.0, -1.111, -2.426], [0.0, 0.773, -2.292], [0.0, -0.149, -2.089], [0.0, 0.379, -1.765],
                [0.0, 0.92, -0.955], [0.0, 1.111, -0.0], [0.0, 0.92, 0.955], [0.0, 0.379, 1.765], [0.0, -0.145, 2.093],
                [0.0, 0.773, 2.292], [0.0, -1.111, 2.426], [0.0, -0.197, 0.774], [0.0, -0.411, 1.745],
                [0.0, 0.058, 1.444], [0.0, 0.501, 0.782], [0.0, 0.656, -0.0], [0.0, 0.501, -0.782],
                [0.0, 0.058, -1.444], [0.0, -0.415, -1.738], [0.0, -0.197, -0.774], [0.0, -1.111, -2.426]], d=1 , n = ctrlName)
        cmds.scale(scale, scale, scale, curvedtwoArrow + '.cv[0:20]')
        cmds.group(ctrlName, n=parentGrpName)

    elif ctrlType == 'curvedFourArrow':
        curvedFourArrow = cmds.curve(p=[[1.992, -0.399, 0.0], [1.333, 0.167, 0.889], [1.333, 0.167, 0.444], [0.889, 0.335, 0.444],
                    [0.444, 0.399, 0.444], [0.444, 0.335, 0.889], [0.444, 0.167, 1.333], [0.889, 0.167, 1.333],
                    [0.0, -0.399, 1.992], [-0.889, 0.167, 1.333], [-0.444, 0.167, 1.333], [-0.444, 0.335, 0.889],
                    [-0.444, 0.399, 0.444], [-0.889, 0.335, 0.444], [-1.333, 0.167, 0.444], [-1.333, 0.167, 0.889],
                    [-1.992, -0.399, 0.0], [-1.333, 0.167, -0.889], [-1.333, 0.167, -0.444], [-0.889, 0.335, -0.444],
                    [-0.444, 0.399, -0.444], [-0.444, 0.335, -0.889], [-0.444, 0.167, -1.333], [-0.889, 0.167, -1.333],
                    [0.0, -0.399, -1.992], [0.889, 0.167, -1.333], [0.444, 0.167, -1.333], [0.444, 0.335, -0.889],
                    [0.444, 0.399, -0.444], [0.889, 0.335, -0.444], [1.333, 0.167, -0.444], [1.333, 0.167, -0.889],
                    [1.992, -0.399, 0.0]], d=1,n = ctrlName)
        cmds.scale(scale, scale, scale, curvedFourArrow + '.cv[0:32]')
        cmds.group(ctrlName, n=parentGrpName)



    elif ctrlType == 'circledArrow':
        circledArrow = cmds.curve(
            p=[[0.935, 0.0, -0.679], [1.099, 0.0, -0.357], [1.156, 0.0, 0.0], [1.099, 0.0, 0.357], [0.935, 0.0, 0.679],
               [0.679, 0.0, 0.935], [0.357, 0.0, 1.099], [0.357, -0.0, 1.323], [0.679, -0.0, 1.323], [0.0, 0.0, 2.0],
               [-0.679, 0.0, 1.323], [-0.357, 0.0, 1.323], [-0.357, 0.0, 1.099], [-0.679, 0.0, 0.935],
               [-0.935, 0.0, 0.679], [-1.099, 0.0, 0.357], [-1.156, 0.0, 0.0], [-1.099, 0.0, -0.357],
               [-0.935, 0.0, -0.679], [-0.679, 0.0, -0.935], [-0.357, 0.0, -1.099], [-0.357, 0.0, -1.353],
               [-0.679, 0.0, -1.353], [0.0, 0.0, -2.0], [0.679, -0.0, -1.353], [0.353, -0.0, -1.353],
               [0.357, 0.0, -1.099], [0.679, 0.0, -0.935], [0.935, 0.0, -0.679]], d=1,n = ctrlName)
        cmds.scale(scale, scale, scale, circledArrow + '.cv[0:28]')
        cmds.group(ctrlName, n=parentGrpName)


    elif ctrlType == 'circleFourArrow':
        circleFourArrow = cmds.curve(p=[[-2.117, 0.0, 0.0], [-1.486, 0.0, 0.671], [-1.486, 0.0, 0.353], [-1.094, 0.0, 0.357],
                 [-0.93, 0.0, 0.679], [-0.674, 0.0, 0.935], [-0.352, 0.0, 1.099], [-0.353, 0.0, 1.323],
                 [-0.666, 0.0, 1.323], [0.005, 0.0, 2.0], [0.684, 0.0, 1.323], [0.354, 0.0, 1.323], [0.362, 0.0, 1.099],
                 [0.684, 0.0, 0.935], [0.94, 0.0, 0.679], [1.104, 0.0, 0.357], [1.46, 0.0, 0.357], [1.46, 0.0, 0.671],
                 [2.117, 0.0, 0.001], [1.46, 0.0, -0.679], [1.46, 0.0, -0.357], [1.104, 0.0, -0.357],
                 [0.94, 0.0, -0.679], [0.684, 0.0, -0.935], [0.362, 0.0, -1.099], [0.362, 0.0, -1.357],
                 [0.684, 0.0, -1.357], [0.005, 0.0, -2.0], [-0.666, 0.0, -1.357], [-0.352, 0.0, -1.357],
                 [-0.352, 0.0, -1.099], [-0.674, 0.0, -0.935], [-0.93, 0.0, -0.679], [-1.094, 0.0, -0.357],
                 [-1.486, 0.0, -0.357], [-1.486, 0.0, -0.679], [-2.117, 0.0, 0.0]], d=1,n = ctrlName)
        cmds.scale(scale, scale, scale, circleFourArrow + '.cv[0:36]')
        cmds.group(ctrlName, n=parentGrpName)

    elif ctrlType == 'singleArrow':
        singleArrow = cmds.curve(p=[[-0.0, 0.0, -2.002], [1.601, -0.0, -0.4], [0.801, 0.0, -0.4], [0.801, 0.0, 2.002], [-0.801, 0.0, 2.002],
               [-0.801, -0.0, -0.4], [-1.601, 0.0, -0.4], [-0.0, 0.0, -2.002]], d=1,n = ctrlName)
        cmds.scale(scale, scale, scale, singleArrow + '.cv[0:7]')
        cmds.group(ctrlName, n=parentGrpName)


#locator parenting...

def createRenameAndParent(locName1,newName1,x1,y1,z1):
    temp1 = cmds.spaceLocator(locName1)
    cmds.rename(temp1, newName1)
    cmds.parent(newName1, locName1)
    cmds.setAttr(newName1 + '.tx', x1)
    cmds.setAttr(newName1 + '.ty', y1)
    cmds.setAttr(newName1 + '.tz', z1)

# knee locating curve...
def pointingCurve(ctrlname,jointname):
    cmds.curve(p=[[0.454, 0.0, 0.072], [1.037, 0.0, 0.072]], d=1 , n=ctrlname+'tempCurve')
    cmds.cluster(ctrlname+'tempCurve.cv[0]',n=ctrlname+'_clusA')
    cmds.cluster(ctrlname+'tempCurve.cv[1]', n=ctrlname+'_clusB')
    cmds.parentConstraint(jointname,ctrlname+'_clusAHandle',maintainOffset=0)
    cmds.parentConstraint(ctrlname,ctrlname + '_clusBHandle', maintainOffset=0)
