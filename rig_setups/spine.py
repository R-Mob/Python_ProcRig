import maya.cmds as cmds
import maya.mel as mel
from utils import libraries as lib
from utils import utilities as util
from utils import skeleton as skel

def ribbonSystemSpine():
    temp1 = cmds.getAttr('spine_7_LOC_C'+'.tz')
    temp2 = cmds.getAttr('spine_01_LOC_C' + '.tz')
    temp = temp2-temp1
    if temp<0:
        temp = -temp

    cmds.nurbsPlane(p=(0,0,0),ax=(0,0,1),w=temp,lr=0.025,d=3,u=6,v=1,ch=1,n="spine_proxyRibbon")
    mel.eval('createHair 7 1 2 0 0 1 0 5 0 1 2 1;')
    cmds.delete("hairSystem1")
    cmds.delete("pfxHair1")
    cmds.delete("nucleus1")
    cmds.rename("hairSystem1Follicles","Spine_folicle_grp")

    a = cmds.ls('curve*', sl=0)
    for i in range(0,7):
        cmds.delete(a[i])

    rename = cmds.ls("spine_proxyRibbonFollicle*")
    for j in range(0,7):
        cmds.rename(rename[j],"SpineFollicle_01")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_01")),n="folicle_01_jj")
    cmds.parent("folicle_01_jj","SpineFollicle_01")
    
    cmds.joint(p=(lib.jointAttr("SpineFollicle_02")),n="folicle_02_jj")
    cmds.parent("folicle_02_jj","SpineFollicle_02")
    
    cmds.joint(p=(lib.jointAttr("SpineFollicle_03")),n="folicle_03_jj")
    cmds.parent("folicle_03_jj","SpineFollicle_03")
    
    cmds.joint(p=(lib.jointAttr("SpineFollicle_04")),n="folicle_04_jj")
    cmds.parent("folicle_04_jj","SpineFollicle_04")
    
    cmds.joint(p=(lib.jointAttr("SpineFollicle_05")),n="folicle_05_jj")
    cmds.parent("folicle_05_jj","SpineFollicle_05")
    
    cmds.joint(p=(lib.jointAttr("SpineFollicle_06")),n="folicle_06_jj")
    cmds.parent("folicle_06_jj","SpineFollicle_06")
    
    cmds.joint(p=(lib.jointAttr("SpineFollicle_07")),n="folicle_07_jj")
    cmds.parent("folicle_07_jj","SpineFollicle_07")

    cmds.select(d=1)

def ribbonSystemPlacement():
    cmds.select("spine_proxyRibbon")
    cmds.lattice(dv = (7,2,2),oc=1,ldv = (7,2,2) ,ol =1,n="temp_spine")
    cmds.setAttr('temp_spineLattice'+'.rx',-90)
    cmds.setAttr('temp_spineLattice' + '.ry', 90)
    
    lib.LocatorPlacement('proxy_LOC_C_1', 0, 139, -64.74)
    lib.LocatorPlacement('proxy_LOC_C_2', 0, 139.77, -44)
    lib.LocatorPlacement('proxy_LOC_C_3', 0, 138.27, -28.7)
    lib.LocatorPlacement('proxy_LOC_C_4', 0, 136.77, -14.48)
    lib.LocatorPlacement('proxy_LOC_C_5', 0, 133, 4.27)
    lib.LocatorPlacement('proxy_LOC_C_6', 0, 130.8, 25.8)
    lib.LocatorPlacement('proxy_LOC_C_7', 0, 127, 51.9)

    cmds.select('temp_spineLattice.pt[0][0:1][1]', 'temp_spineLattice.pt[0][0:1][0]',r=1)
    cmds.move(0,127 , -6.419998,r=1)

    cmds.select('temp_spineLattice.pt[1][0:1][1]', 'temp_spineLattice.pt[1][0:1][0]',r=1)
    cmds.move(0,130.800003 ,  -13.080001,r=1)

    cmds.select('temp_spineLattice.pt[2][0:1][1]', 'temp_spineLattice.pt[2][0:1][0]',r=1)
    cmds.move(0,133 ,-15.17,r=1)

    cmds.select('temp_spineLattice.pt[3][0:1][1]', 'temp_spineLattice.pt[3][0:1][0]',r=1)
    cmds.move(0,136.770004 ,-14.48 ,r=1)

    cmds.select('temp_spineLattice.pt[4][0:1][1]', 'temp_spineLattice.pt[4][0:1][0]',r=1)
    cmds.move(0,138.270004 ,-9.260001 ,r=1)

    cmds.select('temp_spineLattice.pt[5][0:1][1]', 'temp_spineLattice.pt[5][0:1][0]',r=1)
    cmds.move(0,139.770004, -5.12 ,r=1)

    cmds.select('temp_spineLattice.pt[6][0:1][1]', 'temp_spineLattice.pt[6][0:1][0]',r=1)
    cmds.move(0,139, -6.419998 ,r=1)

    a = cmds.ls('proxy_*')
    cmds.delete(a)

    cmds.delete("spine_proxyRibbon",ch=1)
    cmds.xform("spine_proxyRibbon",cp=1)

    
























