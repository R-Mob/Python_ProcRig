import maya.cmds as cmds
from utils import libraries as lib
from utils import utilities as util

def skinToLeftArm():
    left_arm = ['scapula_L', 'scapular_cartilage_L', 'humerus_L', 'radius_L', 'ulnar_carpal_05_L', 'ulnar_carpal_03_L',
                'ulnar_carpal_06_L',
                'ulnar_carpal_01_L', 'ulnar_carpal_02_L', 'ulnar_carpal_04_L', 'metacarpal_L', 'proximal_sesamoid_01_L',
                'proximal_sesamoid_08_L',
                'proximal_sesamoid_06_L', 'proximal_sesamoid_02_L', 'proximal_sesamoid_09_L', 'proximal_sesamoid_05_L',
                'proximal_sesamoid_07_L',
                'proximal_sesamoid_03_L', 'proximal_sesamoid_04_L', 'long_pastern_A_02_L', 'long_pastern_A_01_L',
                'short_pastern_A_01_L'
        , 'short_pastern_A_02_L', 'coffin_bone_A_02_L', 'coffin_bone_A_01_L']
    for i in range(28):

        if i < 2:
            cmds.skinCluster(lib.project_Name + '_l_shoulder_02_jj', left_arm[i], n=left_arm[i] + '_cluster', tsb=True,
                             bm=0, sm=0, nw=1)
        elif i == 2:
            cmds.skinCluster(lib.project_Name + '_l_arm_01_jj', left_arm[i], n=left_arm[i] + '_cluster', tsb=True, bm=0,
                             sm=0, nw=1)
        elif i > 2 and i < 7:
            cmds.skinCluster(lib.project_Name + '_l_arm_02_jj', left_arm[i], n=left_arm[i] + '_cluster', tsb=True, bm=0,
                             sm=0, nw=1)
        elif i > 6 and i < 14:
            cmds.skinCluster(lib.project_Name + '_l_arm_03_jj', left_arm[i], n=left_arm[i] + '_cluster', tsb=True, bm=0,
                             sm=0, nw=1)
        elif i > 13 and i < 24:
            cmds.skinCluster(lib.project_Name + '_l_arm_04_jj', left_arm[i], n=left_arm[i] + '_cluster', tsb=True, bm=0,
                             sm=0, nw=1)
        elif i > 23 and i < 26:
            cmds.skinCluster(lib.project_Name + '_l_arm_05_jj', left_arm[i], n=left_arm[i] + '_cluster', tsb=True, bm=0,
                             sm=0, nw=1)

def leftClavicleSetup():
    #clavicle setup...
    cmds.spaceLocator(p=(0,0,0),n='l_scapula_pos_loc')
    cmds.parentConstraint(lib.project_Name+'_l_shoulder_01_jj','l_scapula_pos_loc',mo = 0,n='temp_l_cons')
    cmds.delete('temp_l_cons')

    cmds.group('l_scapula_pos_loc',n='left_arm_setup')
    cmds.duplicate('l_scapula_pos_loc',n='l_scapula_up_loc')
    cmds.setAttr('l_scapula_up_loc'+'.tx',-19.143)
    cmds.setAttr('l_scapula_up_loc' + '.ty', 104.329)
    cmds.parent('l_scapula_up_loc','l_scapula_pos_loc')
    cmds.duplicate('l_scapula_up_loc',n='l_scapula_aim_loc')
    cmds.setAttr('l_scapula_aim_loc' + '.tx', 0)
    cmds.setAttr('l_scapula_aim_loc' + '.ty', 0)
    cmds.setAttr('l_scapula_aim_loc' + '.tz', 0)

    #bringing arm joints here...
    cmds.group(lib.project_Name+'_l_shoulder_01_jj',n='l_scapulaRotation_helper_grp')
    cmds.parent('l_scapulaRotation_helper_grp','l_scapula_aim_loc')

    cmds.select(d=1)

    #clavicle controller...
    #main shoulder
    lib.controlType('circleFourArrow', lib.project_Name + '_l_clavicle_01_cc', 4, lib.project_Name + '_l_clavicle_01_cc_off')

    cmds.setAttr(lib.project_Name+ '_l_clavicle_01_cc_off' + '.tx', 26.896)
    cmds.setAttr(lib.project_Name + '_l_clavicle_01_cc_off' + '.ty', 107.528)
    cmds.setAttr(lib.project_Name + '_l_clavicle_01_cc_off' + '.tz', 47.186)

    cmds.setAttr(lib.project_Name+ '_l_clavicle_01_cc_off' + '.rz', 90)
    cmds.setAttr(lib.project_Name + '_l_clavicle_01_cc_off' + '.rx', -25)

    cmds.select(d=True)

    #scapula 
    lib.controlType('singleArrow', lib.project_Name + '_l_clavicle_02_cc', 2.9, lib.project_Name + '_l_clavicle_02_cc_off')

    cmds.setAttr(lib.project_Name + '_l_clavicle_02_cc_off' + '.tx', 14.714)
    cmds.setAttr(lib.project_Name + '_l_clavicle_02_cc_off' + '.ty', 151.288)
    cmds.setAttr(lib.project_Name + '_l_clavicle_02_cc_off' + '.tz', 32.517)

    cmds.setAttr(lib.project_Name + '_l_clavicle_02_cc_off' + '.rx', 0)
    cmds.setAttr(lib.project_Name + '_l_clavicle_02_cc_off' + '.ry', 73)
    cmds.setAttr(lib.project_Name + '_l_clavicle_02_cc_off' + '.rz', -90)

    cmds.move(15.63, 109.339996 ,45.5, lib.project_Name + '_l_clavicle_02_cc' + '.scalePivot',
              lib.project_Name + '_l_clavicle_02_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=True)

    #connecting shoulder with controls...
    cmds.parent(lib.project_Name + '_l_clavicle_02_cc_off', lib.project_Name + '_l_clavicle_01_cc')
    cmds.parentConstraint(lib.project_Name + '_l_clavicle_02_cc',lib.project_Name +'_l_shoulder_02_jj',mo=1)
    cmds.aimConstraint(lib.project_Name + '_l_clavicle_01_cc','l_scapula_aim_loc',mo=1)
    cmds.select(d=1)

    lib.AttrlockAndHide(lib.project_Name + '_l_clavicle_01_cc',0,1,1)
    lib.AttrlockAndHide(lib.project_Name + '_l_clavicle_02_cc', 1, 0, 1)

    #parenting back to project structure...
    cmds.parent('left_arm_setup',lib.project_Name +'_CR_SKL')
    cmds.parent(lib.project_Name +'_l_clavicle_01_cc_off', lib.project_Name + '_CR_CC')

    cmds.select(d=1)

def leftArmSetup():
    # ikHandle creation...
    # springIKHandle for driver joint...
    cmds.ikHandle(sj=lib.project_Name + '_l_arm_01_jc', ee=lib.project_Name + '_l_arm_03_jc', sol='ikSpringSolver',
                  n=lib.project_Name + '_arm_l_sprIK_01', ap=1, snc=1)
    cmds.setAttr(lib.project_Name + '_arm_l_sprIK_01'+".twist",180)

    # rpIKhandle for driven joint....
    cmds.ikHandle(sj=lib.project_Name + '_l_arm_01_jj', ee=lib.project_Name + '_l_arm_03_jj', sol='ikRPsolver',
                  n=lib.project_Name + '_arm_l_rpIK', ap=1)

    # scIkhandle for ankle,ball and toe joints...
    cmds.ikHandle(sj=lib.project_Name + '_l_arm_03_jj', ee=lib.project_Name + '_l_arm_04_jj', sol='ikSCsolver',
                  n=lib.project_Name + '_ankle_arm_l_scIK', ap=1)

    cmds.ikHandle(sj=lib.project_Name + '_l_arm_04_jj', ee=lib.project_Name + '_l_arm_05_jj', sol='ikSCsolver',
                  n=lib.project_Name + '_ball_arm_l_scIK', ap=1)

    cmds.ikHandle(sj=lib.project_Name + '_l_arm_05_jj', ee=lib.project_Name + '_l_arm_06_je', sol='ikSCsolver',
                  n=lib.project_Name + '_toe_arm_l_scIK', ap=1)

    # reverse foot locator placement...
    lib.LocatorPlacement(lib.project_Name + '_root_arm_l_LOC', 14.22, 14.1, 33.58)
    lib.createRenameAndParent(lib.project_Name + '_root_arm_l_LOC', lib.project_Name + '_heel_arm_l_LOC', 0, -14.103, 1.791)
    lib.createRenameAndParent(lib.project_Name + '_heel_arm_l_LOC', lib.project_Name + '_ballTwist_arm_l_LOC', 0, 3.123, 3.809)
    lib.createRenameAndParent(lib.project_Name + '_ballTwist_arm_l_LOC', lib.project_Name + '_toe_arm_l_LOC', 0, -3.12, 7.58)
    lib.createRenameAndParent(lib.project_Name + '_toe_arm_l_LOC', lib.project_Name + '_outside_arm_l_LOC', 4.881, 0.057, -7.24)
    lib.createRenameAndParent(lib.project_Name + '_outside_arm_l_LOC', lib.project_Name + '_inside_arm_l_LOC', -9.208, 0, 0)
    lib.createRenameAndParent(lib.project_Name + '_inside_arm_l_LOC', lib.project_Name + '_ball_arm_l_LOC', 4.327, 3.063, -0.34)
    lib.createRenameAndParent(lib.project_Name + '_inside_arm_l_LOC', lib.project_Name + '_toeForward_arm_l_LOC', 4.327, 0,7.24)
    lib.createRenameAndParent(lib.project_Name + '_ball_arm_l_LOC', lib.project_Name + '_ankle_arm_l_LOC', 0, 10.98, -5.6)

    cmds.select(d=True)

    cmds.group(n=lib.project_Name +  '_arm_l_rpIK_rot', em=1)
    cmds.setAttr(lib.project_Name + '_arm_l_rpIK_rot' + '.tx', 14.22)
    cmds.setAttr(lib.project_Name + '_arm_l_rpIK_rot' + '.ty', 14.1)
    cmds.setAttr(lib.project_Name + '_arm_l_rpIK_rot' + '.tz',33.58)

    cmds.parent(lib.project_Name + '_arm_l_rpIK_rot', lib.project_Name + '_ankle_arm_l_LOC')
    cmds.parent(lib.project_Name + '_arm_l_rpIK', lib.project_Name + '_arm_l_rpIK_rot')
    cmds.parent(lib.project_Name + '_ankle_arm_l_scIK', lib.project_Name + '_ball_arm_l_scIK', lib.project_Name + '_arm_l_sprIK_01',
                lib.project_Name + '_ball_arm_l_LOC')
    cmds.parent(lib.project_Name + '_toe_arm_l_scIK', lib.project_Name + '_toeForward_arm_l_LOC')

    cmds.parentConstraint(lib.project_Name + '_l_arm_02_jc', lib.project_Name + '_ankle_arm_l_LOC', maintainOffset=1)

    #controls..
    # main ik control...
    lib.controlType('legIkctrl', lib.project_Name + '_l_arm_01_cc', 6.02, lib.project_Name + '_l_arm_01_cc_off')

    cmds.setAttr(lib.project_Name + '_l_arm_01_cc_off' + '.tx', 14.747)
    cmds.setAttr(lib.project_Name + '_l_arm_01_cc_off' + '.ty', 9.174)
    cmds.setAttr(lib.project_Name + '_l_arm_01_cc_off' + '.tz', 39.119)
    cmds.setAttr(lib.project_Name + '_l_arm_01_cc_off' + '.ry', 6)

    cmds.move(14.22, 14.1, 33.580002, lib.project_Name + '_l_arm_01_cc' + '.scalePivot',
              lib.project_Name + '_l_arm_01_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=True)

    # ankle control...
    lib.controlType('curvedTwoArrow', lib.project_Name + '_l_arm_ankle_01_cc', 3, lib.project_Name + '_l_arm_ankle_01_cc_off')

    cmds.setAttr(lib.project_Name + '_l_arm_ankle_01_cc_off' + '.tx', 14.22)
    cmds.setAttr(lib.project_Name + '_l_arm_ankle_01_cc_off' + '.ty', 18.036)
    cmds.setAttr(lib.project_Name + '_l_arm_ankle_01_cc_off' + '.tz', 38.613)

    cmds.setAttr(lib.project_Name + '_l_arm_ankle_01_cc_off' + '.rx', 84)
    cmds.setAttr(lib.project_Name + '_l_arm_ankle_01_cc_off' + '.ry', -24.542)
    cmds.setAttr(lib.project_Name + '_l_arm_ankle_01_cc_off' + '.rz', -90)

    cmds.move(14.22, 14.1, 33.580002, lib.project_Name + '_l_arm_ankle_01_cc' + '.scalePivot',
              lib.project_Name + '_l_arm_ankle_01_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=True)

    # ball control...
    lib.controlType('curvedTwoArrow', lib.project_Name + '_l_arm_ball_01_cc', 3, lib.project_Name + '_l_arm_ball_01_cc_off')

    cmds.setAttr(lib.project_Name + '_l_arm_ball_01_cc_off' + '.tx', 14.798)
    cmds.setAttr(lib.project_Name + '_l_arm_ball_01_cc_off' + '.ty', 4.773)
    cmds.setAttr(lib.project_Name + '_l_arm_ball_01_cc_off' + '.tz', 44.636)

    cmds.setAttr(lib.project_Name + '_l_arm_ball_01_cc_off' + '.rx', 84)
    cmds.setAttr(lib.project_Name + '_l_arm_ball_01_cc_off' + '.ry', -24.542)
    cmds.setAttr(lib.project_Name + '_l_arm_ball_01_cc_off' + '.rz', -90)

    cmds.move(14.22, 3.12, 39.18, lib.project_Name + '_l_arm_ball_01_cc' + '.scalePivot',
              lib.project_Name + '_l_arm_ball_01_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=True)

    # toe control...
    lib.controlType('curvedTwoArrow', lib.project_Name + '_l_arm_toe_01_cc', 3, lib.project_Name + '_l_arm_toe_01_cc_off')

    cmds.setAttr(lib.project_Name + '_l_arm_toe_01_cc_off' + '.tx', 15.896)
    cmds.setAttr(lib.project_Name + '_l_arm_toe_01_cc_off' + '.ty', 0)
    cmds.setAttr(lib.project_Name + '_l_arm_toe_01_cc_off' + '.tz', 49.581)

    cmds.setAttr(lib.project_Name + '_l_arm_toe_01_cc_off' + '.rx', 84)
    cmds.setAttr(lib.project_Name + '_l_arm_toe_01_cc_off' + '.ry', 0)
    cmds.setAttr(lib.project_Name + '_l_arm_toe_01_cc_off' + '.rz', -90)

    cmds.move(14.22, 0, 46.759998, lib.project_Name + '_l_arm_toe_01_cc' + '.scalePivot',
              lib.project_Name + '_l_arm_toe_01_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=True)

    # heel control...
    lib.controlType('curvedFourArrow', lib.project_Name + '_l_arm_heel_01_cc', 4.522, lib.project_Name + '_l_arm_heel_01_cc_off')

    cmds.setAttr(lib.project_Name + '_l_arm_heel_01_cc_off' + '.tx', 13.763)
    cmds.setAttr(lib.project_Name + '_l_arm_heel_01_cc_off' + '.ty', 9.019)
    cmds.setAttr(lib.project_Name + '_l_arm_heel_01_cc_off' + '.tz', 26.364)

    cmds.setAttr(lib.project_Name + '_l_arm_heel_01_cc_off' + '.rx', -90)
    cmds.setAttr(lib.project_Name + '_l_arm_heel_01_cc_off' + '.ry', 6)
    cmds.setAttr(lib.project_Name + '_l_arm_heel_01_cc_off' + '.rz', 0)

    cmds.move(14.22, -0.003, 35.370998, lib.project_Name + '_l_arm_heel_01_cc' + '.scalePivot',
              lib.project_Name + '_l_arm_heel_01_cc' + '.rotatePivot', absolute=True)
    cmds.select(d=True)

    # attribute manager for locking and creating new attributes

    lib.AttrlockAndHide(lib.project_Name + '_l_arm_01_cc', 0, 0, 1)
    lib.AttrlockAndHide(lib.project_Name + '_l_arm_ankle_01_cc', 1, 0, 1)
    lib.AttrlockAndHide(lib.project_Name + '_l_arm_ball_01_cc', 1, 0, 1)
    lib.AttrlockAndHide(lib.project_Name + '_l_arm_toe_01_cc', 1, 0, 1)
    lib.AttrlockAndHide(lib.project_Name + '_l_arm_heel_01_cc', 1, 0, 1)

    cmds.select(d=1)

    # parent arm joint to shoulder joint
    cmds.parent(lib.project_Name + '_l_arm_01_jj', lib.project_Name + '_l_shoulder_02_jj')


    # Polevector for knee controls....

    lib.controlType('circledArrow', lib.project_Name + '_l_arm_knee_01_pv', 2, lib.project_Name + '_l_arm_knee_01_pv_off')

    cmds.setAttr(lib.project_Name + '_l_arm_knee_01_pv_off' + '.tx', 5.245)
    cmds.setAttr(lib.project_Name + '_l_arm_knee_01_pv_off' + '.ty', 77.700)
    cmds.setAttr(lib.project_Name + '_l_arm_knee_01_pv_off' + '.tz', 8.818)

    cmds.setAttr(lib.project_Name + '_l_arm_knee_01_pv_off' + '.rx', 90)
    cmds.setAttr(lib.project_Name + '_l_arm_knee_01_pv_off' + '.ry', 0)
    cmds.setAttr(lib.project_Name + '_l_arm_knee_01_pv_off' + '.rz', 90)


    cmds.poleVectorConstraint(lib.project_Name +'_l_arm_knee_01_pv', lib.project_Name + '_arm_l_sprIK_01')

    # knee locating curve...

    lib.pointingCurve(lib.project_Name + '_l_arm_knee_01_pv', lib.project_Name + '_l_arm_02_jj')
    cmds.select(d=1)
    # locking attributes for knee...
    lib.AttrlockAndHide(lib.project_Name + '_l_arm_knee_01_pv', 0, 1, 1)

    # connecting attributes to controllers...
    cmds.parentConstraint(lib.project_Name + '_l_arm_01_cc', lib.project_Name + '_root_arm_l_LOC', maintainOffset=1)

    # setting up alias name...
    cmds.aliasAttr('heel_swivel', lib.project_Name + '_l_arm_heel_01_cc.rx')
    cmds.aliasAttr('heel_tilt', lib.project_Name + '_l_arm_heel_01_cc.ry')
    cmds.aliasAttr('heel_twist', lib.project_Name + '_l_arm_heel_01_cc.rz')

    cmds.aliasAttr('ankle_twist', lib.project_Name + '_l_arm_ankle_01_cc.rx')
    cmds.aliasAttr('ankle_tilt', lib.project_Name + '_l_arm_ankle_01_cc.ry')
    cmds.aliasAttr('ankle_lift', lib.project_Name + '_l_arm_ankle_01_cc.rz')

    cmds.aliasAttr('ball_twist', lib.project_Name + '_l_arm_ball_01_cc.rx')
    cmds.aliasAttr('ball_tilt', lib.project_Name + '_l_arm_ball_01_cc.ry')
    cmds.aliasAttr('ball_lift', lib.project_Name + '_l_arm_ball_01_cc.rz')

    cmds.aliasAttr('toe_twist', lib.project_Name + '_l_arm_toe_01_cc.rx')
    cmds.aliasAttr('toe_tilt', lib.project_Name + '_l_arm_toe_01_cc.ry')
    cmds.aliasAttr('toe_lift', lib.project_Name + '_l_arm_toe_01_cc.rz')
    
    #create toeforward attribute..
    cmds.select(lib.project_Name +  '_l_arm_toe_01_cc')
    cmds.addAttr(ln="ToeForward",shortName='toeForward', dv=0,k=1,)

    # expressions for front left arm

    # heel ctrl...
    cmds.expression(s='Ciervo_heel_arm_l_LOC.rotateY =  (Ciervo_l_arm_heel_01_cc.rotateZ);', n='heel_arm_twist_l')
    cmds.expression(s='Ciervo_heel_arm_l_LOC.rotateZ =  (Ciervo_l_arm_heel_01_cc.rotateY)*-1;', n='heel_arm_tilt_l')
    cmds.expression(s='Ciervo_heel_arm_l_LOC.rotateX =  (Ciervo_l_arm_heel_01_cc.rotateX);', n='heel_arm_swivel_l')

    # ankle ctrl...
    cmds.expression(s='Ciervo_arm_l_rpIK_rot.rotateX =  (Ciervo_l_arm_ankle_01_cc.rotateZ)*-1;', n='ankle_arm_tilt_l')
    cmds.expression(s='Ciervo_arm_l_rpIK_rot.rotateY =  (Ciervo_l_arm_ankle_01_cc.rotateX)*-1;', n='ankle_arm_twist_l')
    cmds.expression(s='Ciervo_arm_l_rpIK_rot.rotateZ =  (Ciervo_l_arm_ankle_01_cc.rotateY);', n='ankle_arm_swivel_l')

    # ball ctrl...
    cmds.expression(s='Ciervo_ball_arm_l_LOC.rotateX =  (Ciervo_l_arm_ball_01_cc.rotateZ)*-1;', n='ball_arm_tilt_l')
    cmds.expression(s='Ciervo_ball_arm_l_LOC.rotateZ =  (Ciervo_l_arm_ball_01_cc.rotateY);', n='ball_arm_twist_l')
    cmds.expression(s='Ciervo_ball_arm_l_LOC.rotateY =  (Ciervo_l_arm_ball_01_cc.rotateX)*-1;', n='ball_arm_swivel_l')

    # toe ctrl...

    cmds.expression(s='Ciervo_toe_arm_l_LOC.rotateY =  (Ciervo_l_arm_toe_01_cc.rotateX)*-1;', n='toe_arm_twist_l')
    cmds.expression(s='Ciervo_toe_arm_l_LOC.rotateX =  (Ciervo_l_arm_toe_01_cc.rotateZ)*-1;', n='toe_arm_swivel_l')

    cmds.expression(s='Ciervo_outside_arm_l_LOC.rotateZ =min(0,Ciervo_l_arm_toe_01_cc.rotateY);', n='toe_arm_outside_l')
    cmds.expression(s='Ciervo_inside_arm_l_LOC.rotateZ =max(0,Ciervo_l_arm_toe_01_cc.rotateY);', n='toe_arm_inside_l')
    cmds.expression(s='Ciervo_toeForward_arm_l_LOC.translateY = (Ciervo_l_arm_toe_01_cc.ToeForward);', n='toe_arm_forward_l')

    cmds.select(d=1)

    # creating arm hierarchy...
    cmds.parent(lib.project_Name + '_l_arm_ankle_01_cc_off', lib.project_Name + '_l_arm_ball_01_cc')
    cmds.parent(lib.project_Name + '_l_arm_ball_01_cc_off', lib.project_Name + '_l_arm_toe_01_cc')
    cmds.parent(lib.project_Name + '_l_arm_toe_01_cc_off', lib.project_Name + '_l_arm_heel_01_cc')
    cmds.parent(lib.project_Name + '_l_arm_heel_01_cc_off', lib.project_Name + '_l_arm_01_cc')

    cmds.select(d=1)

    # parent leg components to it relevant project structure

    cmds.parent( lib.project_Name+ '_root_arm_l_LOC',  lib.project_Name + '_CR_LOC')

    cmds.parent(lib.project_Name + '_l_arm_knee_01_pvtempCurve', lib.project_Name + '_l_arm_knee_01_pv_clusAHandle',lib.project_Name + '_l_arm_knee_01_pv_clusBHandle',lib.project_Name + '_CR_XTR')

    cmds.hide(lib.project_Name + '_l_arm_knee_01_pv_clusAHandle')
    cmds.hide(lib.project_Name + '_l_arm_knee_01_pv_clusBHandle')
    lib.AttrlockAndHide(lib.project_Name + '_l_arm_knee_01_pvtempCurve', 1, 1, 1)

    cmds.parent(lib.project_Name  + '_l_arm_knee_01_pv_off', lib.project_Name  + '_CR_CC')
    cmds.parent(lib.project_Name + '_l_arm_01_cc_off', lib.project_Name + '_CR_CC')

    cmds.select(d=1)
    cmds.group(lib.project_Name + '_l_arm_01_jc',n=lib.project_Name + '_ljc',w=1)
    cmds.parent(lib.project_Name + '_ljc',lib.project_Name + '_l_shoulder_02_jj')
    cmds.select(d=1)


