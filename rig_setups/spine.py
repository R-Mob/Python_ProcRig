import maya.cmds as cmds
import maya.mel as mel
from utils import libraries as lib
from utils import utilities as util
from utils import skeleton as skel

def ribbonSystemSpine():
    temp1 = cmds.getAttr('spine_7_LOC_C'+'.tz')
    temp2 = cmds.getAttr('spine_01_LOC_C' + '.tz')
    temp = temp2-temp1

    cmds.nurbsPlane(p=(0,0,0),ax=(0,1,0),w=temp,lr=0.025,d=3,u=9,v=1,ch=1,n="spine_proxyRibbon")
    mel.eval('createHair 10 1 2 0 0 1 0 5 0 1 2 1;')
    cmds.delete("hairSystem1")
    cmds.delete("pfxHair1")
    cmds.delete("nucleus1")

    a = cmds.ls('curve*', sl=0)
    for i in range(0,10):
        cmds.delete(a[i])

    rename = cmds.ls("spine_proxyRibbonFollicle*")

    for j in range(0,10):
        cmds.rename(rename[j],"SpineFollicle_01")





