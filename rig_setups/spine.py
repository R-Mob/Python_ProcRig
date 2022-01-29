import maya.cmds as cmds
import maya.mel as mel
from utils import libraries as lib
from utils import utilities as util
from utils import skeleton as skel

def skinToSpine():
    spine = ['sacrum_C', 'thoriac_vertibrae_C19_C', 'thoriac_vertibrae_C18_C', 'thoriac_vertibrae_C17_C',
             'thoriac_vertibrae_C16_C', 'thoriac_vertibrae_C15_C', 'thoriac_vertibrae_C14_C',
             'thoriac_vertibrae_C13_C', 'thoriac_vertibrae_C12_C', 'thoriac_vertibrae_C11_C', 'thoriac_vertibrae_C10_C',
             'rib_13_L', 'rib_12_L','rib_11_L', 'rib_10_L','sternocostal_13_L' ,'sternocostal_12_L','sternocostal_11_L',
             'sternocostal_10_L','sternocostal_13_R' ,'sternocostal_12_R','sternocostal_11_R',
             'sternocostal_10_R',
             'rib_13_R', 'rib_12_R', 'rib_11_R', 'rib_10_R', 'thoriac_vertibrae_C09_C','thoriac_vertibrae_C08_C',
             'thoriac_vertibrae_C07_C', 'thoriac_vertibrae_C06_C', 'rib_09_L', 'rib_08_L', 'rib_07_L', 'rib_06_L','rib_09_R', 'rib_08_R',
             'rib_07_R', 'rib_06_R','sternocostal_09_L' ,'sternocostal_08_L','sternocostal_07_L',
             'sternocostal_06_L','sternocostal_09_R' ,'sternocostal_08_R','sternocostal_07_R',
             'sternocostal_06_R','sternum_09_C' ,'sternum_08_C' ,'sternum_07_C' ,'sternum_06_C' ,'thoriac_vertibrae_C05_C',
             'thoriac_vertibrae_C04_C', 'thoriac_vertibrae_C03_C',
             'thoriac_vertibrae_C02_C', 'thoriac_vertibrae_C01_C', 'rib_05_L', 'rib_04_L', 'rib_03_L', 'rib_02_L',
             'rib_01_L', 'rib_05_R', 'rib_04_R', 'rib_03_R', 'rib_02_R', 'rib_01_R','sternocostal_05_L','sternocostal_04_L',
             'sternocostal_03_L','sternocostal_02_L','sternocostal_01_L','sternocostal_05_R','sternocostal_04_R',
             'sternocostal_03_R','sternocostal_02_R','sternocostal_01_R','sternum_05_C','sternum_04_C','sternum_03_C',
             'sternum_02_C','sternum_01_C']
    for i in range(81):

        if i < 1:
            cmds.skinCluster(lib.project_Name + '_c_spine_01_jj', spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 0 and i < 4:
            cmds.skinCluster(lib.project_Name + '_c_spine_02_jj', spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 3 and i < 7:
            cmds.skinCluster(lib.project_Name + '_c_spine_03_jj', spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 6 and i < 27:
            cmds.skinCluster(lib.project_Name + '_c_spine_04_jj', spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 26 and i < 51:
            cmds.skinCluster(lib.project_Name + '_c_spine_05_jj', spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 50 and i < 81:
            cmds.skinCluster(lib.project_Name + '_c_spine_06_jj', spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)

    cmds.select(d=1)



def ribbonSystemSpine():
    #length of spine ribbon..
    temp1 = cmds.getAttr('spine_7_LOC_C'+'.tz')
    temp2 = cmds.getAttr('spine_01_LOC_C' + '.tz')
    temp = temp2-temp1
    if temp<0:
        temp = -temp
    #nurbs plane creation..
    cmds.nurbsPlane(p=(0,0,0),ax=(0,0,1),w=temp,lr=0.025,d=3,u=12,v=1,ch=1,n="spine_proxyRibbon")
    #creating nhairs and deleting extra components..
    mel.eval('createHair 13 1 2 0 0 1 0 5 0 1 2 1;')
    cmds.delete("hairSystem1")
    cmds.delete("pfxHair1")
    cmds.delete("nucleus1")
    cmds.rename("hairSystem1Follicles","Spine_folicle_grp")

    a = cmds.ls('curve*', sl=0)
    for i in range(0,13):
        cmds.delete(a[i])

    rename = cmds.ls("spine_proxyRibbonFollicle*")
    for j in range(0,13):
        cmds.rename(rename[j],"SpineFollicle_01")

    #creating jj joints inside folicles..
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

    cmds.joint(p=(lib.jointAttr("SpineFollicle_07")), n="folicle_07_jj")
    cmds.parent("folicle_07_jj", "SpineFollicle_07")
    
    cmds.joint(p=(lib.jointAttr("SpineFollicle_08")),n="folicle_08_jj")
    cmds.parent("folicle_08_jj","SpineFollicle_08")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_09")), n="folicle_09_jj")
    cmds.parent("folicle_09_jj", "SpineFollicle_09")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_10")), n="folicle_10_jj")
    cmds.parent("folicle_10_jj", "SpineFollicle_10")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_11")), n="folicle_11_jj")
    cmds.parent("folicle_11_jj", "SpineFollicle_11")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_12")), n="folicle_12_jj")
    cmds.parent("folicle_12_jj", "SpineFollicle_12")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_13")), n="folicle_13_jj")
    cmds.parent("folicle_13_jj", "SpineFollicle_13")

    cmds.select(d=1)

def ribbonSystemPlacement():
    #creating lattice and placing it..
    cmds.select("spine_proxyRibbon")
    cmds.lattice(dv = (7,2,2),oc=1,ldv = (14,2,2) ,ol =1,n="temp_spine")
    cmds.setAttr('temp_spineLattice'+'.rx',-90)
    cmds.setAttr('temp_spineLattice' + '.ry', 90)
    
    lib.LocatorPlacement('proxy_LOC_C_1', 0, 139, -64.74)
    lib.LocatorPlacement('proxy_LOC_C_2', 0, 139.77, -44)
    lib.LocatorPlacement('proxy_LOC_C_3', 0, 138.27, -28.7)
    lib.LocatorPlacement('proxy_LOC_C_4', 0, 136.77, -14.48)
    lib.LocatorPlacement('proxy_LOC_C_5', 0, 133, 4.27)
    lib.LocatorPlacement('proxy_LOC_C_6', 0, 130.8, 25.8)
    lib.LocatorPlacement('proxy_LOC_C_7', 0, 127, 51.9)

    cmds.select('temp_spineLattice.pt[0][0:1][0]', 'temp_spineLattice.pt[0][0:1][1]',r=1)
    cmds.move(0,127 , -6.419998,r=1)

    cmds.select('temp_spineLattice.pt[1][0:1][0]', 'temp_spineLattice.pt[1][0:1][1]',r=1)
    cmds.move(0,130.800003 ,  -13.080001,r=1)

    cmds.select('temp_spineLattice.pt[2][0:1][0]', 'temp_spineLattice.pt[2][0:1][1]',r=1)
    cmds.move(0,133 ,-15.17,r=1)

    cmds.select('temp_spineLattice.pt[3][0:1][0]', 'temp_spineLattice.pt[3][0:1][1]',r=1)
    cmds.move(0,136.770004 ,-14.48 ,r=1)

    cmds.select('temp_spineLattice.pt[4][0:1][0]', 'temp_spineLattice.pt[4][0:1][1]',r=1)
    cmds.move(0,138.270004 ,-9.260001 ,r=1)

    cmds.select('temp_spineLattice.pt[5][0:1][0]', 'temp_spineLattice.pt[5][0:1][1]',r=1)
    cmds.move(0,139.770004, -5.12 ,r=1)

    cmds.select('temp_spineLattice.pt[6][0:1][0]', 'temp_spineLattice.pt[6][0:1][1]',r=1)
    cmds.move(0,139, -6.419998 ,r=1)

    a = cmds.ls('proxy_*')
    cmds.delete(a)

    cmds.delete("spine_proxyRibbon",ch=1)
    cmds.xform("spine_proxyRibbon",cp=1)
    
    #creating ik curve...
    cmds.curve(p=[[0.0, 139.0, -64.74], [0.0, 139.018, -58.394], [0.0, 139.055, -45.702], [-0.0, 137.809, -29.089],
                  [-0.0, 135.849, -12.158], [-0.0, 133.264, 6.442], [-0.0, 130.39, 27.417], [-0.0, 128.13, 43.739],
                  [-0.0, 127.0, 51.9]],d=3,n='spine_ik_curve')
    cmds.delete("spine_ik_curve", ch=1)
    cmds.xform("spine_ik_curve", cp=1)
    #creating IKSpline Handle...
    cmds.ikHandle(sj =lib.project_Name+'_c_spine_01_jj', ee=lib.project_Name+'_c_spine_07_je',c='spine_ik_curve',ccv=0,
                  pcv=0 ,snc=0, n = lib.project_Name+'_spine_spIK',sol = 'ikSplineSolver')
    cmds.select(d=1)

    #creating control joints...
    cmds.joint(p=(lib.jointAttr('spine_01_LOC_C')), n=lib.project_Name + '_c_spine_01_jc')
    cmds.select(d=1)
    cmds.joint(p=(lib.jointAttr('spine_4_LOC_C')), n=lib.project_Name + '_c_spine_02_jc')
    cmds.select(d=1)
    cmds.joint(p=(lib.jointAttr('spine_7_LOC_C')), n=lib.project_Name + '_c_spine_03_jc')

    cmds.select(d=1)
    #skin bind jc to ikCurve...
    cmds.skinCluster(lib.project_Name + '_c_spine_01_jc',lib.project_Name + '_c_spine_02_jc',lib.project_Name + '_c_spine_03_jc',"spine_ik_curve", n='cluster_jc', tsb=True,bm=0, sm=0,nw=1)

    # skin bind jj to ribbon...
    cmds.skinCluster(lib.project_Name + '_c_spine_01_jj',lib.project_Name + '_c_spine_02_jj',lib.project_Name + '_c_spine_03_jj',lib.project_Name + '_c_spine_04_jj',lib.project_Name + '_c_spine_05_jj',lib.project_Name + '_c_spine_06_jj',lib.project_Name + '_c_spine_07_je',"spine_proxyRibbon", n='cluster_ribbon', tsb=True,bm=0, sm=0,nw=1)

    #spine controllers...

























