import maya.cmds as cmds
from utils import libraries as lib
from utils import utilities as util
from utils import skeleton as skel

def skinToRightBone():
    
    right_leg = ['femur_R', 'patella_R', 'tibia_R', 'talus_03_R', 'talus_02_R', 'calcaneus_R', 'talus_01_R',
                'talus_05_R', 'talus_04_R',
                'metatarsal_R', 'medial_sesamoid_07_R', 'medial_sesamoid_02_R', 'medial_sesamoid_06_R',
                'medial_sesamoid_01_R',
                'medial_sesamoid_04_R', 'medial_sesamoid_09_R', 'medial_sesamoid_05_R', 'medial_sesamoid_08_R',
                'medial_sesamoid_03_R',
                'long_pastern_B_02_R', 'long_pastern_B_01_R', 'short_pastern_B_02_R', 'short_pastern_B_01_R',
                'coffin_bone_B_01_R'
        , 'coffin_bone_B_02_R']
    for i in range(28):
        if i < 2:
            cmds.skinCluster(lib.project_Name + '_r_leg_02_jj', right_leg[i], n=right_leg[i] + '_cluster', tsb=True, bm=0,
                             sm=0, nw=1)
        elif i > 1 and i < 5:
            cmds.skinCluster(lib.project_Name + '_r_leg_03_jj', right_leg[i], n=right_leg[i] + '_cluster', tsb=True, bm=0,
                             sm=0, nw=1)
        elif i >= 5 and i < 13:
            cmds.skinCluster(lib.project_Name + '_r_leg_04_jj', right_leg[i], n=right_leg[i] + '_cluster', tsb=True, bm=0,
                             sm=0, nw=1)
        elif i >= 13 and i < 23:
            cmds.skinCluster(lib.project_Name + '_r_leg_05_jj', right_leg[i], n=right_leg[i] + '_cluster', tsb=True, bm=0,
                             sm=0,
                             nw=1)
        elif i >= 23 and i < 25:
            cmds.skinCluster(lib.project_Name + '_r_leg_06_jj', right_leg[i], n=right_leg[i] + '_cluster', tsb=True, bm=0,
                             sm=0,
                             nw=1)
            
    cmds.select(d=True)
            
def rightLegSetup():
    # ikHandle creation...
    # springIKHandle for driver joint...
    cmds.ikHandle(sj=lib.project_Name + '_r_leg_01_jc', ee=lib.project_Name + '_r_leg_04_jc', sol='ikSpringSolver',
                  n=lib.project_Name + '_leg_r_sprIK', ap=1, snc=1)
    # rpIKhandle for driven joint....
    cmds.ikHandle(sj=lib.project_Name + '_r_leg_02_jj', ee=lib.project_Name + '_r_leg_04_jj', sol='ikRPsolver',
                  n=lib.project_Name + '_leg_r_rpIK', ap=1)

    # scIkhandle for ankle,ball and toe joints...
    cmds.ikHandle(sj=lib.project_Name + '_r_leg_04_jj', ee=lib.project_Name + '_r_leg_05_jj', sol='ikSCsolver',
                  n=lib.project_Name + '_ankle_r_scIK', ap=1)

    cmds.ikHandle(sj=lib.project_Name + '_r_leg_05_jj', ee=lib.project_Name + '_r_leg_06_jj', sol='ikSCsolver',
                  n=lib.project_Name + '_ball_r_scIK', ap=1)

    cmds.ikHandle(sj=lib.project_Name + '_r_leg_06_jj', ee=lib.project_Name + '_r_leg_07_je', sol='ikSCsolver',
                  n=lib.project_Name + '_toe_r_scIK', ap=1)

    # reverse foot locator placement...

    lib.LocatorPlacement(lib.project_Name + '_root_r_LOC', -14.53, 15.7, -75.65)
    lib.createRenameAndParent(lib.project_Name + '_root_r_LOC', lib.project_Name + '_heel_r_LOC', 0, -15.718, 1.791)
    lib.createRenameAndParent(lib.project_Name + '_heel_r_LOC', lib.project_Name + '_ballTwist_r_LOC', 0, 2.468, 4.259)
    lib.createRenameAndParent(lib.project_Name + '_ballTwist_r_LOC', lib.project_Name + '_toe_r_LOC', 0, -2.45, 7.24)
    lib.createRenameAndParent(lib.project_Name + '_toe_r_LOC', lib.project_Name + '_outside_r_LOC', 4.881, 0.057, -7.24)
    lib.createRenameAndParent(lib.project_Name + '_outside_r_LOC', lib.project_Name + '_inside_r_LOC', -9.208, 0, 0)
    lib.createRenameAndParent(lib.project_Name + '_inside_r_LOC', lib.project_Name + '_ball_r_LOC', 4.327, 2.393, 0)
    lib.createRenameAndParent(lib.project_Name + '_inside_r_LOC', lib.project_Name + '_toeForward_r_LOC', 4.327, -0.057,7.24)
    lib.createRenameAndParent(lib.project_Name + '_ball_r_LOC', lib.project_Name + '_ankle_r_LOC', 0, 13.25, -6.05)

    cmds.select(d=True)
    cmds.group(n=lib.project_Name + '_leg_r_rpIK_rot', em=1)
    cmds.setAttr(lib.project_Name + '_leg_r_rpIK_rot' + '.tx', -14.53)
    cmds.setAttr(lib.project_Name + '_leg_r_rpIK_rot' + '.ty', 15.7)
    cmds.setAttr(lib.project_Name + '_leg_r_rpIK_rot' + '.tz', -75.65)

    cmds.parent(lib.project_Name + '_leg_r_rpIK_rot', lib.project_Name + '_ankle_r_LOC')
    cmds.parent(lib.project_Name + '_leg_r_rpIK', lib.project_Name + '_leg_r_rpIK_rot')
    cmds.parent(lib.project_Name + '_ankle_r_scIK', lib.project_Name + '_ball_r_scIK', lib.project_Name + '_leg_r_sprIK',
                lib.project_Name + '_ball_r_LOC')
    cmds.parent(lib.project_Name + '_toe_r_scIK', lib.project_Name +'_toeForward_r_LOC')

    cmds.parentConstraint(lib.project_Name + '_r_leg_03_jc', lib.project_Name + '_ankle_r_LOC', maintainOffset=1)

    cmds.select(d=True)

    # controls...
    # main ik control...
    lib.controlType('legIkctrl',lib.project_Name + '_r_leg_01_cc', 6.02,lib.project_Name + '_r_leg_01_cc_off')

    cmds.setAttr(lib.project_Name + '_r_leg_01_cc_off' + '.tx', -14.53)
    cmds.setAttr(lib.project_Name + '_r_leg_01_cc_off' + '.ty', 9.174)
    cmds.setAttr(lib.project_Name + '_r_leg_01_cc_off' + '.tz', -71.183)
    cmds.setAttr(lib.project_Name + '_r_leg_01_cc_off' + '.ry', -6)

    cmds.move(-14.53, 15.7, -75.650002,lib.project_Name + '_r_leg_01_cc' + '.scalePivot',
             lib.project_Name + '_r_leg_01_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=True)

    # ankle control...
    lib.controlType('curvedTwoArrow',lib.project_Name + '_r_ankle_01_cc', 3,lib.project_Name + '_r_ankle_01_cc_off')

    cmds.setAttr(lib.project_Name + '_r_ankle_01_cc_off' + '.tx', -14.53)
    cmds.setAttr(lib.project_Name + '_r_ankle_01_cc_off' + '.ty', 17.998)
    cmds.setAttr(lib.project_Name + '_r_ankle_01_cc_off' + '.tz', -70.617)

    cmds.setAttr(lib.project_Name + '_r_ankle_01_cc_off' + '.rx', 96)
    cmds.setAttr(lib.project_Name + '_r_ankle_01_cc_off' + '.ry', -24.542)
    cmds.setAttr(lib.project_Name + '_r_ankle_01_cc_off' + '.rz', -90)

    cmds.move(-14.53, 15.7, -75.650002,lib.project_Name + '_r_ankle_01_cc' + '.scalePivot',
             lib.project_Name + '_r_ankle_01_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=True)

    # ball control...
    lib.controlType('curvedTwoArrow',lib.project_Name + '_r_ball_01_cc', 3,lib.project_Name + '_r_ball_01_cc_off')

    cmds.setAttr(lib.project_Name + '_r_ball_01_cc_off' + '.tx', -15.108)
    cmds.setAttr(lib.project_Name + '_r_ball_01_cc_off' + '.ty', 4.735)
    cmds.setAttr(lib.project_Name + '_r_ball_01_cc_off' + '.tz', -64.594)

    cmds.setAttr(lib.project_Name + '_r_ball_01_cc_off' + '.rx', 96)
    cmds.setAttr(lib.project_Name + '_r_ball_01_cc_off' + '.ry', -24.542)
    cmds.setAttr(lib.project_Name + '_r_ball_01_cc_off' + '.rz', -90)

    cmds.move(-14.53, 2.45, -69.599998,lib.project_Name + '_r_ball_01_cc' + '.scalePivot',
             lib.project_Name + '_r_ball_01_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=True)

    # toe control...
    lib.controlType('curvedTwoArrow',lib.project_Name + '_r_toe_01_cc', 3,lib.project_Name + '_r_toe_01_cc_off')

    cmds.setAttr(lib.project_Name + '_r_toe_01_cc_off' + '.tx', -15.108)
    cmds.setAttr(lib.project_Name + '_r_toe_01_cc_off' + '.ty', 0)
    cmds.setAttr(lib.project_Name + '_r_toe_01_cc_off' + '.tz', -59.534)

    cmds.setAttr(lib.project_Name + '_r_toe_01_cc_off' + '.rx', 96)
    cmds.setAttr(lib.project_Name + '_r_toe_01_cc_off' + '.ry', 0)
    cmds.setAttr(lib.project_Name + '_r_toe_01_cc_off' + '.rz', -90)

    cmds.move(-14.53, 0, -62.360001,lib.project_Name + '_r_toe_01_cc' + '.scalePivot',
             lib.project_Name + '_r_toe_01_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=True)

    # heel control...
    lib.controlType('curvedFourArrow',lib.project_Name + '_r_heel_01_cc', 4.522,lib.project_Name + '_r_heel_01_cc_off')

    cmds.setAttr(lib.project_Name + '_r_heel_01_cc_off' + '.tx', -14.073)
    cmds.setAttr(lib.project_Name + '_r_heel_01_cc_off' + '.ty', 7.473)
    cmds.setAttr(lib.project_Name + '_r_heel_01_cc_off' + '.tz', -82.866)

    cmds.setAttr(lib.project_Name + '_r_heel_01_cc_off' + '.rx', -90)
    cmds.setAttr(lib.project_Name + '_r_heel_01_cc_off' + '.ry', -6)
    cmds.setAttr(lib.project_Name + '_r_heel_01_cc_off' + '.rz', 0)

    cmds.move(-14.53, -0.018, -73.859001,lib.project_Name + '_r_heel_01_cc' + '.scalePivot',
             lib.project_Name + '_r_heel_01_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=True)

    # attribute manager for locking and creating new attributes

    lib.AttrlockAndHide(lib.project_Name + '_r_leg_01_cc', 0, 0, 1)
    lib.AttrlockAndHide(lib.project_Name + '_r_ankle_01_cc', 1, 0, 1)
    lib.AttrlockAndHide(lib.project_Name + '_r_ball_01_cc', 1, 0, 1)
    lib.AttrlockAndHide(lib.project_Name + '_r_toe_01_cc', 1, 0, 1)
    lib.AttrlockAndHide(lib.project_Name+ '_r_heel_01_cc', 1, 0, 1)

    cmds.select(d=1)

    # Polevector for knee controls....

    lib.controlType('circledArrow', lib.project_Name + '_r_knee_01_pv', 2, lib.project_Name + '_r_knee_01_pv_off')

    cmds.setAttr(lib.project_Name + '_r_knee_01_pv_off' + '.tx', -34.038)
    cmds.setAttr(lib.project_Name + '_r_knee_01_pv_off' + '.ty', 89.358)
    cmds.setAttr(lib.project_Name + '_r_knee_01_pv_off' + '.tz', -10.349)

    cmds.setAttr(lib.project_Name + '_r_knee_01_pv_off' + '.rx', 90)
    cmds.setAttr(lib.project_Name + '_r_knee_01_pv_off' + '.ry', 0)
    cmds.setAttr(lib.project_Name + '_r_knee_01_pv_off' + '.rz', 90)

    cmds.poleVectorConstraint(lib.project_Name + '_r_knee_01_pv', lib.project_Name + '_leg_r_sprIK')
    # knee locating curve...

    lib.pointingCurve(lib.project_Name + '_r_knee_01_pv', lib.project_Name + '_r_leg_03_jj')
    cmds.select(d=1)
    # locking attributes for knee...
    lib.AttrlockAndHide(lib.project_Name + '_r_knee_01_pv', 0, 1, 1)

    # connecting attributes to controllers...
    cmds.parentConstraint(lib.project_Name + '_r_leg_01_cc', lib.project_Name + '_root_r_LOC', maintainOffset=1)

    # setting up alias name...
    cmds.aliasAttr('heel_swivel',lib.project_Name + '_r_heel_01_cc.rx')
    cmds.aliasAttr('heel_tilt',lib.project_Name + '_r_heel_01_cc.ry')
    cmds.aliasAttr('heel_twist',lib.project_Name + '_r_heel_01_cc.rz')

    cmds.aliasAttr('ankle_twist',lib.project_Name + '_r_ankle_01_cc.rx')
    cmds.aliasAttr('ankle_tilt',lib.project_Name + '_r_ankle_01_cc.ry')
    cmds.aliasAttr('ankle_lift',lib.project_Name + '_r_ankle_01_cc.rz')

    cmds.aliasAttr('ball_twist',lib.project_Name + '_r_ball_01_cc.rx')
    cmds.aliasAttr('ball_tilt',lib.project_Name + '_r_ball_01_cc.ry')
    cmds.aliasAttr('ball_lift',lib.project_Name + '_r_ball_01_cc.rz')

    cmds.aliasAttr('toe_twist',lib.project_Name + '_r_toe_01_cc.rx')
    cmds.aliasAttr('toe_tilt',lib.project_Name + '_r_toe_01_cc.ry')
    cmds.aliasAttr('toe_lift',lib.project_Name + '_r_toe_01_cc.rz')

    # create toeforward attribute..
    cmds.select(lib.project_Name + '_r_toe_01_cc')
    cmds.addAttr(ln="ToeForward", shortName='toeForward', dv=0, k=1, )

    # expressions for ..  [ when using different project name, it should be change in expressions manually ]
    # heel ctrl...
    cmds.expression(s='Ciervo_heel_r_LOC.rotateZ =  (Ciervo_r_heel_01_cc.rotateY)*-1;', n='heel_tilt_r')
    cmds.expression(s='Ciervo_heel_r_LOC.rotateY =  (Ciervo_r_heel_01_cc.rotateZ);', n='heel_twist_r')
    cmds.expression(s='Ciervo_heel_r_LOC.rotateX =  (Ciervo_r_heel_01_cc.rotateX);', n='heel_swivel_r')

    # ankle ctrl...
    cmds.expression(s='Ciervo_leg_r_rpIK_rot.rotateZ =  (Ciervo_r_ankle_01_cc.rotateY);', n='ankle_tilt_r')
    cmds.expression(s='Ciervo_leg_r_rpIK_rot.rotateY =  (Ciervo_r_ankle_01_cc.rotateX)*-1;', n='ankle_twist_r')
    cmds.expression(s='Ciervo_leg_r_rpIK_rot.rotateX =  (Ciervo_r_ankle_01_cc.rotateZ)*-1;', n='ankle_swivel_r')

    # ball ctrl...
    cmds.expression(s='Ciervo_ball_r_LOC.rotateZ =  (Ciervo_r_ball_01_cc.rotateY);', n='ball_tilt_r')
    cmds.expression(s='Ciervo_ball_r_LOC.rotateY =  (Ciervo_r_ball_01_cc.rotateX)*-1;', n='ball_twist_r')
    cmds.expression(s='Ciervo_ball_r_LOC.rotateX =  (Ciervo_r_ball_01_cc.rotateZ)*-1;', n='ball_swivel_r')

    # toe ctrl...
    # cmds.expression( s='Ciervo_toe_r_LOC.rotateZ =  (Ciervo_r_toe_01_cc.rotateY);',n = 'toe_tilt_l')
    cmds.expression(s='Ciervo_toe_r_LOC.rotateY =  (Ciervo_r_toe_01_cc.rotateX)*-1;', n='toe_twist_r')
    cmds.expression(s='Ciervo_toe_r_LOC.rotateX =  (Ciervo_r_toe_01_cc.rotateZ)*-1;', n='toe_swivel_r')

    cmds.expression(s='Ciervo_outside_r_LOC.rotateZ =min(0,Ciervo_r_toe_01_cc.rotateY);', n='toe_outside_r')
    cmds.expression(s='Ciervo_inside_r_LOC.rotateZ =max(0,Ciervo_r_toe_01_cc.rotateY);', n='toe_inside_r')
    cmds.expression(s='Ciervo_toeForward_r_LOC.translateY = (Ciervo_r_toe_01_cc.ToeForward);', n='toe_forward_r')

    cmds.select(d=1)

    # parenting leg joints...

    cmds.parent(lib.project_Name + '_r_ankle_01_cc_off', lib.project_Name + '_r_ball_01_cc')
    cmds.parent(lib.project_Name + '_r_ball_01_cc_off', lib.project_Name + '_r_toe_01_cc')
    cmds.parent(lib.project_Name + '_r_toe_01_cc_off', lib.project_Name + '_r_heel_01_cc')
    cmds.parent(lib.project_Name + '_r_heel_01_cc_off', lib.project_Name + '_r_leg_01_cc')

    cmds.select(d=1)
    # creating proxy_hip ctrl...
    lib.controlType('circle', 'hip_r_Ctrl', 1, lib.project_Name + '_hipCtrl_r_off')
    cmds.parentConstraint(lib.project_Name + '_r_leg_01_jj', lib.project_Name + '_hipCtrl_r_off', mo=0, sr=["x", "z", "y"],
                          n=lib.project_Name + 'tempConstraint')
    cmds.delete(lib.project_Name + 'tempConstraint')
    cmds.parentConstraint('hip_r_Ctrl', lib.project_Name + '_r_leg_01_jj', mo=1)
    lib.AttrlockAndHide('hip_r_Ctrl', 0, 0, 1)

    cmds.select(d=1)
    # parent leg components to it relevant project structure

    cmds.parent(lib.project_Name + '_root_r_LOC', lib.project_Name + '_CR_LOC')
    cmds.select(d=1)

    cmds.parent(lib.project_Name + '_r_knee_01_pvtempCurve', lib.project_Name + '_r_knee_01_pv_clusAHandle'
                , lib.project_Name + '_r_knee_01_pv_clusBHandle', lib.project_Name + '_CR_XTR')

    cmds.hide(lib.project_Name + '_r_knee_01_pv_clusAHandle')
    cmds.hide(lib.project_Name + '_r_knee_01_pv_clusBHandle')
    lib.AttrlockAndHide(lib.project_Name + '_r_knee_01_pvtempCurve', 1, 1, 1)

    cmds.parent(lib.project_Name + '_r_leg_01_cc_off', lib.project_Name + '_r_knee_01_pv_off', lib.project_Name + '_hipCtrl_r_off',
                lib.project_Name + '_CR_CC')

    cmds.select(d=1)


    
    








