import maya.cmds as cmds
import maya.mel as mel
from utils import libraries as lib
from utils import utilities as util
from utils import skeleton as skel
name = "spine_"



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
    cmds.joint(p=(lib.jointAttr("SpineFollicle_01")),n=name+"folicle_01_jj")
    cmds.parent(name+"folicle_01_jj","SpineFollicle_01")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_02")),n=name+"folicle_02_jj")
    cmds.parent(name+"folicle_02_jj","SpineFollicle_02")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_03")),n=name+"folicle_03_jj")
    cmds.parent(name+"folicle_03_jj","SpineFollicle_03")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_04")),n=name+"folicle_04_jj")
    cmds.parent(name+"folicle_04_jj","SpineFollicle_04")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_05")),n=name+"folicle_05_jj")
    cmds.parent(name+"folicle_05_jj","SpineFollicle_05")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_06")),n=name+"folicle_06_jj")
    cmds.parent(name+"folicle_06_jj","SpineFollicle_06")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_07")), n=name+"folicle_07_jj")
    cmds.parent(name+"folicle_07_jj", "SpineFollicle_07")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_08")),n=name+"folicle_08_jj")
    cmds.parent(name+"folicle_08_jj","SpineFollicle_08")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_09")), n=name+"folicle_09_jj")
    cmds.parent(name+"folicle_09_jj", "SpineFollicle_09")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_10")), n=name+"folicle_10_jj")
    cmds.parent(name+"folicle_10_jj", "SpineFollicle_10")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_11")), n=name+"folicle_11_jj")
    cmds.parent(name+"folicle_11_jj", "SpineFollicle_11")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_12")), n=name+"folicle_12_jj")
    cmds.parent(name+"folicle_12_jj", "SpineFollicle_12")

    cmds.joint(p=(lib.jointAttr("SpineFollicle_13")), n=name+"folicle_13_jj")
    cmds.parent(name+"folicle_13_jj", "SpineFollicle_13")

    cmds.select(d=1)

def ribbonSystemPlacement():
    #creating lattice and placing it..
    cmds.select("spine_proxyRibbon")
    cmds.lattice(dv = (7,2,2),oc=1,ldv = (14,2,2) ,ol =1,n="temp_spine")
    cmds.setAttr('temp_spineLattice'+'.rx',-90)
    cmds.setAttr('temp_spineLattice' + '.ry', 90)
    cmds.select(d=1)
    lib.LocatorPlacement('proxy_LOC_C_1', 0, 139.778, -64.319)
    lib.LocatorPlacement('proxy_LOC_C_2',0, 147.222, -5.085)
    lib.LocatorPlacement('proxy_LOC_C_3', 0,133.587, 11.127)
    lib.LocatorPlacement('proxy_LOC_C_4',  0,134.148, 17.847)
    lib.LocatorPlacement('proxy_LOC_C_5',0, 135.571, 24.993)
    lib.LocatorPlacement('proxy_LOC_C_6', 0, 136.236,45.207)
    lib.LocatorPlacement('proxy_LOC_C_7',0, 132.777, 48.96)

    cmds.select('temp_spineLattice.pt[0][0:1][0]', 'temp_spineLattice.pt[0][0:1][1]',r=1)
    cmds.move(0,132.776993, -7.681,r=1)

    cmds.select('temp_spineLattice.pt[1][0:1][0]', 'temp_spineLattice.pt[1][0:1][1]',r=1)
    cmds.move(0,  136.236,7.447,r=1)

    cmds.select('temp_spineLattice.pt[2][0:1][0]', 'temp_spineLattice.pt[2][0:1][1]',r=1)
    cmds.move(0,135.571,6.113,r=1)

    cmds.select('temp_spineLattice.pt[3][0:1][0]', 'temp_spineLattice.pt[3][0:1][1]',r=1)
    cmds.move(0, 134.148, 17.847 ,r=1)

    cmds.select('temp_spineLattice.pt[4][0:1][0]', 'temp_spineLattice.pt[4][0:1][1]',r=1)
    cmds.move(0,133.587,30.007,r=1)

    cmds.select('temp_spineLattice.pt[5][0:1][0]', 'temp_spineLattice.pt[5][0:1][1]',r=1)
    cmds.move(0,147.222, 32.675 ,r=1)

    cmds.select('temp_spineLattice.pt[6][0:1][0]', 'temp_spineLattice.pt[6][0:1][1]',r=1)
    cmds.move(0, 139.778 ,-7.68,r=1)
    
    a = cmds.ls('proxy_*')
    cmds.delete(a)
    cmds.select(d=1)
    cmds.delete("spine_proxyRibbon",ch=1)
    cmds.xform("spine_proxyRibbon",cp=1)

def spineSetup():
    #creating ik curve...

    cmds.ikHandle(sj=lib.project_Name + '_c_spine_01_jj', ee=lib.project_Name + '_c_spine_07_je',ccv=1,
                  pcv=0, snc=0,scv=0, n=lib.project_Name + '_spine_spIK', sol='ikSplineSolver')
    cmds.rename("curve1","spine_ik_curve")
    cmds.select(d=1)
    #creating control joints...
    cmds.joint(p=(lib.jointAttr('spine_01_LOC_C')), n=lib.project_Name + '_c_spine_01_jc')
    cmds.select(d=1)
    cmds.joint(p=(lib.jointAttr('spine_4_LOC_C')), n=lib.project_Name + '_c_spine_02_jc')
    cmds.select(d=1)
    cmds.joint(p=(lib.jointAttr('spine_7_LOC_C')), n=lib.project_Name + '_c_spine_03_jc')


    #skin bind jc to ikCurve...
    cmds.skinCluster(lib.project_Name + '_c_spine_01_jc',lib.project_Name + '_c_spine_02_jc',lib.project_Name + '_c_spine_03_jc',"spine_ik_curve", n='cluster_jc', tsb=True,bm=0, sm=0,nw=1)
    
    # skin bind jj to ribbon...
    cmds.skinCluster(lib.project_Name + '_c_spine_01_jj',lib.project_Name + '_c_spine_02_jj',lib.project_Name + '_c_spine_03_jj',lib.project_Name + '_c_spine_04_jj',lib.project_Name + '_c_spine_05_jj',lib.project_Name + '_c_spine_06_jj',lib.project_Name + '_c_spine_07_je',"spine_proxyRibbon", n='cluster_ribbon', tsb=True,bm=0, sm=0,nw=1)
    cmds.select(d=1)
    #spine controllers...

    lib.controlType('hipctrl', lib.project_Name + '_c_hip_01_cc',1, lib.project_Name + '_c_hip_01_cc_off')

    cmds.setAttr(lib.project_Name + '_c_hip_01_cc_off' + '.tx', 0)
    cmds.setAttr(lib.project_Name + '_c_hip_01_cc_off' + '.ty',116.48)
    cmds.setAttr(lib.project_Name + '_c_hip_01_cc_off' + '.tz', -51.511)

    cmds.move(0 ,139.778 ,-64.319 , lib.project_Name + '_c_hip_01_cc' + '.scalePivot',
              lib.project_Name + '_c_hip_01_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=1)
    lib.controlType('flankctrl', lib.project_Name + '_c_flank_01_cc',1, lib.project_Name + '_c_flank_01_cc_off')

    cmds.setAttr(lib.project_Name + '_c_flank_01_cc_off' + '.tx', 0)
    cmds.setAttr(lib.project_Name + '_c_flank_01_cc_off' + '.ty',115.236)
    cmds.setAttr(lib.project_Name + '_c_flank_01_cc_off' + '.tz', -7.967)

    cmds.move( 0 ,141.182999, -14.534 , lib.project_Name + '_c_flank_01_cc' + '.scalePivot',
              lib.project_Name + '_c_flank_01_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=1)
    lib.controlType('chestctrl', lib.project_Name + '_c_chest_01_cc', 1, lib.project_Name + '_c_chest_01_cc_off')

    cmds.setAttr(lib.project_Name + '_c_chest_01_cc_off' + '.tx', 0)
    cmds.setAttr(lib.project_Name + '_c_chest_01_cc_off' + '.ty', 118.155)
    cmds.setAttr(lib.project_Name + '_c_chest_01_cc_off' + '.tz',39.346)
    cmds.setAttr(lib.project_Name + '_c_chest_01_cc_off' + '.rx', 3.534)

    cmds.move(0, 134.74144 ,27.218098 ,lib.project_Name + '_c_chest_01_cc' + '.scalePivot',
              lib.project_Name + '_c_chest_01_cc' + '.rotatePivot', absolute=True)

    cmds.select(d=1)

    lib.controlType('centralCtrl',lib.project_Name + '_c_global_01_cc',10,lib.project_Name + '_c_global_01_cc_off')
    cmds.setAttr(lib.project_Name + '_c_global_01_cc_off'+'.sz',4)
    cmds.setAttr(lib.project_Name + '_c_global_01_cc_off' + '.ty', 170)
    cmds.setAttr(lib.project_Name + '_c_global_01_cc_off' + '.tz', -19.133)

    cmds.parent('Ciervo_c_hip_01_cc_off', 'Ciervo_c_flank_01_cc_off', 'Ciervo_c_chest_01_cc_off',
                'Ciervo_c_global_01_cc')
    cmds.select(d=1)
    #connecting attributes...

    cmds.createNode('multiplyDivide', n='spine_twist_multi')
    cmds.connectAttr('Ciervo_c_spine_01_jc.rotateZ', 'spine_twist_multi.i1z')
    cmds.connectAttr('Ciervo_c_spine_01_jc.rotateZ', 'Ciervo_spine_spIK.roll')
    cmds.setAttr('spine_twist_multi'+'.i2z',-1)

    cmds.createNode('plusMinusAverage',n='spine_twist_pma')

    cmds.connectAttr('Ciervo_c_spine_03_jc.rotateZ','spine_twist_pma.input1D[0]')
    cmds.connectAttr('spine_twist_multi.output.outputZ','spine_twist_pma.input1D[1]')

    cmds.connectAttr('spine_twist_pma.output1D','Ciervo_spine_spIK.twist')

    # mid controllers attributes...
    cmds.expression(s='spine_folicle_01_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-0.1;', n='midC_1')
    cmds.expression(s='spine_folicle_02_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-0.1;', n='midC_2')
    
    cmds.expression(s='spine_folicle_03_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-0.2;', n='midC_3')
    cmds.expression(s='spine_folicle_04_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-0.2;', n='midC_4')
    
    cmds.expression(s='spine_folicle_05_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-0.4;', n='midC_5')
    cmds.expression(s='spine_folicle_06_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-0.4;', n='midC_6')
    
    cmds.expression(s='spine_folicle_07_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-0.5;', n='midC_7')
    cmds.expression(s='spine_folicle_08_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-0.6;', n='midC_8')
    
    cmds.expression(s='spine_folicle_09_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-0.8;', n='midC_9')
    cmds.expression(s='spine_folicle_10_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-1.0;', n='midC_10')
    
    cmds.expression(s='spine_folicle_11_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-0.8;', n='midC_11')
    cmds.expression(s='spine_folicle_12_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-0.6;', n='midC_12')
    
    cmds.expression(s='spine_folicle_13_jj.rotateX =  (Ciervo_c_spine_02_jc.rotateZ)*-0.5;', n='midC_13')

    # stretchy spline implementation...[added in nexct version if needed ]
    #connectAttr -force spine_ik_curveShape.worldSpace[0] spine_curve_qwk.inputCurve;

    #mid follow setup..
    cmds.spaceLocator(p=(0, 0, 0), n="world_space_locator")
    cmds.select("Ciervo_c_flank_01_cc")
    cmds.addAttr(ln="mid_follow", at="enum", en="both:world:chest:hip")
    cmds.setAttr("Ciervo_c_flank_01_cc.mid_follow", e=1, k=1)

    cmds.parentConstraint("Ciervo_c_hip_01_cc", "Ciervo_c_chest_01_cc", "world_space_locator",
                          "Ciervo_c_flank_01_cc_off", mo=1)

    cmds.createNode("condition", n="follow_both")
    cmds.createNode("condition", n="follow_hip")
    cmds.createNode("condition", n="follow_chest")
    cmds.createNode("condition", n="follow_world")

    cmds.connectAttr("Ciervo_c_flank_01_cc.mid_follow", "follow_both.firstTerm")
    cmds.connectAttr("Ciervo_c_flank_01_cc.mid_follow", "follow_hip.firstTerm")
    cmds.connectAttr("Ciervo_c_flank_01_cc.mid_follow", "follow_chest.firstTerm")
    cmds.connectAttr("Ciervo_c_flank_01_cc.mid_follow", "follow_world.firstTerm")

    cmds.connectAttr("follow_both.outColorR","Ciervo_c_flank_01_cc_off_parentConstraint1.Ciervo_c_chest_01_ccW1")  # chest
    cmds.connectAttr("follow_both.outColorG", "Ciervo_c_flank_01_cc_off_parentConstraint1.Ciervo_c_hip_01_ccW0")  # hip
    cmds.connectAttr("follow_both.outColorB","Ciervo_c_flank_01_cc_off_parentConstraint1.world_space_locatorW2")  # world

    #follow both attributes...

    cmds.setAttr("follow_both.colorIfTrueR",1)
    cmds.setAttr("follow_both.colorIfTrueG", 1)
    cmds.setAttr("follow_both.colorIfTrueB", 0)
    cmds.setAttr("follow_both.colorIfFalseR", 0)
    cmds.setAttr("follow_both.colorIfFalseG", 0)
    cmds.setAttr("follow_both.colorIfFalseB", 1)



    #world..
    cmds.setAttr("follow_world.secondTerm", 1)

    cmds.setAttr("follow_world.colorIfTrueR", 1)
    cmds.setAttr("follow_world.colorIfFalseR", 0)

    cmds.connectAttr("follow_world.outColorR","follow_both.colorIfFalseB")

    #chest..
    cmds.setAttr("follow_chest.secondTerm", 2)

    cmds.setAttr("follow_chest.colorIfTrueR", 1)
    cmds.setAttr("follow_chest.colorIfFalseR", 0)

    cmds.connectAttr("follow_chest.outColorR", "follow_both.colorIfFalseR")

    # hip
    cmds.setAttr("follow_hip.secondTerm", 3)

    cmds.setAttr("follow_hip.colorIfTrueR", 1)
    cmds.setAttr("follow_hip.colorIfFalseR", 0)

    cmds.connectAttr("follow_hip.outColorR", "follow_both.colorIfFalseG")

    #parenting jc to spine controls...
    cmds.parentConstraint(lib.project_Name +  '_c_chest_01_cc' ,lib.project_Name + '_c_spine_03_jc', maintainOffset=1)
    cmds.parentConstraint(lib.project_Name +  '_c_flank_01_cc',lib.project_Name + '_c_spine_02_jc',maintainOffset=1)
    cmds.parentConstraint(lib.project_Name + '_c_hip_01_cc', lib.project_Name + '_c_spine_01_jc',maintainOffset=1)
    cmds.select(d=1)
    #parenting to rig group...
    cmds.parent(lib.project_Name + '_c_global_01_cc_off',lib.project_Name + '_CR_CC')
    cmds.select(d=1)
    cmds.parent(lib.project_Name + '_c_spine_01_jc',lib.project_Name + '_CR_SKL')
    cmds.select(d=1)
    cmds.parent(lib.project_Name + '_c_spine_02_jc', lib.project_Name + '_CR_SKL')
    cmds.select(d=1)
    cmds.parent(lib.project_Name + '_c_spine_03_jc', lib.project_Name + '_CR_SKL')
    cmds.select(d=1)

    cmds.parent("world_space_locator",lib.project_Name + '_CR_LOC')
    cmds.select(d=1)

    cmds.parent(lib.project_Name + '_spine_spIK',lib.project_Name + '_CR_IK')
    cmds.select(d=1)

    cmds.parent('spine_proxyRibbon', lib.project_Name + '_CR_XTR')
    cmds.parent('Spine_folicle_grp', lib.project_Name + '_CR_XTR')
    cmds.parent('spine_ik_curve', lib.project_Name + '_CR_XTR')

    cmds.hide('spine_proxyRibbon')
    cmds.hide('Spine_folicle_grp')
    cmds.hide('spine_ik_curve')


def skinToSpine():



    spine = ['sacrum_C',#1

             'thoriac_vertibrae_C19_C', 'thoriac_vertibrae_C18_C', 'thoriac_vertibrae_C17_C',#3

             'thoriac_vertibrae_C16_C', 'thoriac_vertibrae_C15_C', 'thoriac_vertibrae_C14_C',#6

             'thoriac_vertibrae_C13_C', 'thoriac_vertibrae_C12_C', 'rib_13_L','rib_12_L','rib_13_R', 'rib_12_R',
             'sternocostal_13_L','sternocostal_12_L','sternocostal_13_R' ,'sternocostal_12_R',#16

             'thoriac_vertibrae_C11_C', 'thoriac_vertibrae_C10_C','rib_11_L', 'rib_10_L','rib_11_R', 'rib_10_R',
             'sternocostal_10_L','sternocostal_11_L','sternocostal_10_R','sternocostal_11_R',#26

             'thoriac_vertibrae_C09_C', 'thoriac_vertibrae_C08_C', 'rib_08_L', 'rib_09_L', 'rib_08_R', 'rib_09_R',
             'sternocostal_09_L', 'sternocostal_08_L','sternocostal_09_R' ,'sternocostal_08_R','sternum_09_C' ,
             'sternum_08_C', #38

             'thoriac_vertibrae_C07_C', 'rib_07_L','rib_07_R','sternum_07_C','sternocostal_07_L','sternocostal_07_R',#44

             'thoriac_vertibrae_C06_C', 'rib_06_L', 'rib_06_R', 'sternum_06_C','sternocostal_06_L','sternocostal_06_R', # 50

             'thoriac_vertibrae_C05_C', 'rib_05_L', 'rib_05_R', 'sternum_05_C','sternocostal_05_L','sternocostal_05_R',  # 56

             'thoriac_vertibrae_C04_C', 'rib_04_L', 'rib_04_R', 'sternum_04_C', 'sternocostal_04_L','sternocostal_04_R', # 62

             'thoriac_vertibrae_C03_C', 'rib_03_L', 'rib_03_R', 'sternum_03_C','sternocostal_03_L','sternocostal_03_R',  # 68

             'thoriac_vertibrae_C02_C', 'rib_02_L', 'rib_02_R', 'sternum_02_C','sternocostal_02_L','sternocostal_02_R',  # 74

             'thoriac_vertibrae_C01_C', 'rib_01_L', 'rib_01_R', 'sternum_01_C','sternocostal_01_L','sternocostal_01_R',  # 80
        ]

    for i in range(81):

        if i < 1:
            cmds.skinCluster(name+"folicle_13_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 0 and i < 4:
            cmds.skinCluster(name+"folicle_12_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 3 and i < 7:
            cmds.skinCluster(name+"folicle_11_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 6 and i < 17:
            cmds.skinCluster(name+"folicle_10_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 16 and i < 27:
            cmds.skinCluster(name+"folicle_09_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 26 and i < 39:
            cmds.skinCluster(name+"folicle_08_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 38 and i < 45:
            cmds.skinCluster(name + "folicle_07_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 44 and i < 51:
            cmds.skinCluster(name + "folicle_06_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 50 and i < 57:
            cmds.skinCluster(name + "folicle_05_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 56 and i < 63:
            cmds.skinCluster(name + "folicle_04_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 62 and i < 69:
            cmds.skinCluster(name + "folicle_03_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 68 and i < 75:
            cmds.skinCluster(name + "folicle_02_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)
        elif i > 74 and i < 81:
            cmds.skinCluster(name + "folicle_01_jj", spine[i], n=spine[i] + '_cluster', tsb=True, bm=0, sm=0,
                             nw=1)

    cmds.select(d=1)


























