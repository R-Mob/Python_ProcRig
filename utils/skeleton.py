import maya.cmds as cmds
from . import libraries as lib
from . import utilities as util
project_name = "Ciervo"

def jointPlacement():
    ### jnt chain formation with proper LRA
    cmds.select(d=True)
    # leg joints...
    cmds.joint(p=(lib.jointAttr('leg_1_LOC_L')), n=project_name + '_l_leg_01_jj')
    cmds.joint(p=(lib.jointAttr('leg_2_LOC_L')), n=project_name + '_l_leg_02_jj')
    cmds.joint(project_name + '_l_leg_02_jj', e=True, zso=True, oj='xyz')
    cmds.joint(p=(lib.jointAttr('leg_3_LOC_L')), n=project_name + '_l_leg_03_jj')
    cmds.joint(project_name + '_l_leg_03_jj', e=True, zso=True, oj='xyz')
    cmds.joint(p=(lib.jointAttr('leg_4_LOC_L')), n=project_name + '_l_leg_04_jj')
    cmds.joint(project_name + '_l_leg_04_jj', e=True, zso=True, oj='xyz')
    cmds.joint(p=(lib.jointAttr('leg_5_LOC_L')), n=project_name + '_l_leg_05_jj')
    cmds.joint(project_name + '_l_leg_05_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('leg_6_LOC_L')), n=project_name + '_l_leg_06_jj')
    cmds.joint(project_name + '_l_leg_06_jj', e=True, zso=True, oj='xyz')
    cmds.joint(p=(lib.jointAttr('leg_7_LOC_L')), n=project_name + '_l_leg_07_je')
    cmds.joint(project_name + '_l_leg_07_je', e=True, zso=True, oj='xyz')

    cmds.select(project_name + '_l_leg_01_jj')
    cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='zdown', ch=True)

    cmds.select(project_name + '_l_leg_07_je')
    cmds.joint(e=True, zso=True, oj='none')

    # front arm joint...
    cmds.select(d=True)

    cmds.joint(p=(lib.jointAttr('clavicle_1_LOC_L')), n=project_name + '_l_shoulder_01_jj')
    cmds.joint(p=(lib.jointAttr('clavicle_2_LOC_L')), n=project_name + '_l_shoulder_02_jj')

    cmds.joint(project_name + '_l_shoulder_02_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('clavicle_3_LOC_L')), n=project_name + '_l_shoulder_03_je')

    cmds.joint(project_name + '_l_shoulder_03_je', e=True, zso=True, oj='xyz')

    cmds.select(project_name + '_l_shoulder_01_jj')
    cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='zdown', ch=True)

    cmds.select(project_name + '_l_shoulder_03_je')
    cmds.joint(e=True, zso=True, oj='none')

    cmds.select(d=True)

    cmds.joint(p=(lib.jointAttr('arm_1_LOC_L')), n=project_name + '_l_arm_01_jj')
    cmds.joint(p=(lib.jointAttr('arm_2_LOC_L')), n=project_name + '_l_arm_02_jj')
    cmds.joint(project_name + '_l_arm_02_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('arm_3_LOC_L')), n=project_name + '_l_arm_03_jj')

    cmds.joint(project_name + '_l_arm_03_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('arm_4_LOC_L')), n=project_name + '_l_arm_04_jj')

    cmds.joint(project_name + '_l_arm_04_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('arm_5_LOC_L')), n=project_name + '_l_arm_05_jj')

    cmds.joint(project_name + '_l_arm_05_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('arm_6_LOC_L')), n=project_name + '_l_arm_06_je')

    cmds.joint(project_name + '_l_arm_06_je', e=True, zso=True, oj='xyz')

    cmds.select(project_name + '_l_arm_01_jj')
    cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='zdown', ch=True)

    cmds.select(project_name + '_l_arm_06_je')
    cmds.joint(e=True, zso=True, oj='none')

    # spine joint....

    cmds.select(d=True)

    cmds.joint(p=(lib.jointAttr('spine_01_LOC_C')), n=project_name + '_c_spine_01_jj')
    cmds.joint(p=(lib.jointAttr('spine_2_LOC_C')), n=project_name + '_c_spine_02_jj')
    cmds.joint(project_name + '_c_spine_02_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('spine_3_LOC_C')), n=project_name + '_c_spine_03_jj')
    cmds.joint(project_name + '_c_spine_03_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('spine_4_LOC_C')), n=project_name + '_c_spine_04_jj')
    cmds.joint(project_name + '_c_spine_04_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('spine_5_LOC_C')), n=project_name + '_c_spine_05_jj')
    cmds.joint(project_name + '_c_spine_05_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('spine_6_LOC_C')), n=project_name + '_c_spine_06_jj')
    cmds.joint(project_name + '_c_spine_06_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('spine_7_LOC_C')), n=project_name + '_c_spine_07_je ')
    cmds.joint(project_name + '_c_spine_07_je ', e=True, zso=True, oj='xyz')

    cmds.select(project_name + '_c_spine_01_jj')
    cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='ydown', ch=True)

    cmds.select(project_name + '_c_spine_07_je ')
    cmds.joint(e=True, zso=True, oj='none')

    # neck joint...
    cmds.select(d=True)

    cmds.joint(p=(lib.jointAttr('neck_1_LOC_C')), n=project_name + '_c_neck_01_jj')
    cmds.joint(p=(lib.jointAttr('neck_2_LOC_C')), n=project_name + '_c_neck_02_jj')
    cmds.joint(project_name + '_c_neck_02_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('neck_3_LOC_C')), n=project_name + '_c_neck_03_jj')
    cmds.joint(project_name + '_c_neck_03_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('neck_4_LOC_C')), n=project_name + '_c_neck_04_jj')
    cmds.joint(project_name + '_c_neck_04_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('neck_5_LOC_C')), n=project_name + '_c_neck_05_jj')
    cmds.joint(project_name + '_c_neck_05_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('neck_6_LOC_C')), n=project_name + '_c_neck_06_jj')
    cmds.joint(project_name + '_c_neck_06_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('neck_7_LOC_C')), n=project_name + '_c_neck_07_jj')
    cmds.joint(project_name + '_c_neck_07_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('neck_8_LOC_C')), n=project_name + '_c_neck_08_je')
    cmds.joint(project_name + '_c_neck_08_je', e=True, zso=True, oj='xyz')

    cmds.select(project_name + '_c_neck_01_jj')
    cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='ydown', ch=True)

    cmds.select(project_name + '_c_neck_05_jj')
    cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='zup', ch=False)

    cmds.select(project_name + '_c_neck_08_je')
    cmds.joint(e=True, zso=True, oj='none')

    # tail joint...
    cmds.select(d=True)

    cmds.joint(p=(lib.jointAttr('tail_1_LOC_C')), n=project_name + '_c_tail_01_jj')
    cmds.joint(p=(lib.jointAttr('tail_2_LOC_C')), n=project_name + '_c_tail_02_jj')
    cmds.joint(project_name + '_c_tail_02_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('tail_3_LOC_C')), n=project_name + '_c_tail_03_jj')
    cmds.joint(project_name + '_c_tail_03_jj', e=True, zso=True, oj='xyz')

    cmds.joint(p=(lib.jointAttr('tail_4_LOC_C')), n=project_name + '_c_tail_04_je')
    cmds.joint(project_name + '_c_tail_04_je', e=True, zso=True, oj='xyz')

    cmds.select(project_name + '_c_tail_01_jj')
    cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='yup', ch=True)

    cmds.select(project_name + '_c_tail_04_je')
    cmds.joint(e=True, zso=True, oj='none')

    # head joint...
    cmds.select(d=True)

    cmds.joint(p=(lib.jointAttr('head_1_LOC_C')), n=project_name + '_c_head_01_jj')
    cmds.joint(p=(lib.jointAttr('head_2_LOC_C')), n=project_name + '_c_head_02_je')
    cmds.joint(project_name + '_c_head_02_je', e=True, zso=True, oj='xyz')

    cmds.select(project_name + '_c_head_01_jj')
    cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='ydown', ch=True)

    cmds.select(project_name + '_c_head_02_je')
    cmds.joint(e=True, zso=True, oj='none')

    # pelvis joint...
    cmds.select(d=True)

    cmds.joint(p=(lib.jointAttr('pelvis_1_LOC_C')), n=project_name + '_c_pelvis_01_jj')
    cmds.joint(p=(lib.jointAttr('pelvis_2_LOC_C')), n=project_name + '_c_pelvis_02_je')
    cmds.joint(project_name + '_c_pelvis_02_je', e=True, zso=True, oj='xyz')

    cmds.select(project_name + '_c_pelvis_01_jj')
    cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='ydown', ch=True)

    cmds.select(project_name + '_c_pelvis_02_je')
    cmds.joint(e=True, zso=True, oj='none')

    cmds.select(d=True)

    cmds.parent(project_name + '_l_leg_01_jj', project_name + '_c_pelvis_01_jj')
    cmds.parent(project_name + '_c_pelvis_01_jj', project_name + '_c_spine_02_jj')

    cmds.select(d=True)
    # mirror leg joints..
    cmds.mirrorJoint(project_name + '_l_leg_01_jj', mirrorBehavior=True, myz=True, searchReplace=('_l_', '_r_'))
    cmds.select(d=True)
    # mirror shoulder joint..
    cmds.mirrorJoint(project_name + '_l_shoulder_01_jj', mirrorBehavior=True, myz=True, searchReplace=('_l_', '_r_'))
    cmds.select(d=True)
    # mirror arm joints...
    cmds.mirrorJoint(project_name + '_l_arm_01_jj', mirrorBehavior=True, myz=True, searchReplace=('_l_', '_r_'))
    cmds.select(d=True)

    cmds.parent(project_name + '_l_shoulder_01_jj', project_name + '_l_arm_01_jj', project_name + '_c_spine_01_jj',
                project_name + '_c_neck_01_jj', project_name + '_c_tail_01_jj', project_name + '_c_head_01_jj',
                project_name + '_r_shoulder_01_jj', project_name + '_r_arm_01_jj', project_name + '_CR_SKL')
    cmds.select(d=True)




