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
    print("Hu")
    #arm setup..




















