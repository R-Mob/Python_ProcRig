
import maya.cmds as cmds
from . import libraries as lib


def projectStructure():
    ### project structure
    main_grp = cmds.group(n=lib.project_Name + '_CR_ALL', em=True)
    ort_grp = cmds.group(n=lib.project_Name + '_CR_ORT', em=True)
    rot_grp = cmds.group(n=lib.project_Name+ '_CR_ROT', em=True)
    scl_grp = cmds.group(n=lib.project_Name + '_CR_SCL', em=True)
    skl_grp = cmds.group(n=lib.project_Name + '_CR_SKL', em=True)
    pp_grp = cmds.group(n=lib.project_Name + '_CR_PP', em=True)
    ik_grp = cmds.group(n=lib.project_Name + '_CR_IK', em=True)
    loc_grp = cmds.group(n=lib.project_Name + '_CR_LOC', em=True)
    cc_grp = cmds.group(n=lib.project_Name + '_CR_CC', em=True)
    geo_grp = cmds.group(n=lib.project_Name + '_CR_GEO', em=True)
    proxy_grp = cmds.group(n=lib.project_Name + '_proxy_GEO', em=True)
    highpoly_grp = cmds.group(n=lib.project_Name + '_HighPoly_GEO', em=True)
    skeleton_grp = cmds.group(n=lib.project_Name+ '_Anatomy_GEO', em=True)
    crshp_grp = cmds.group(n=lib.project_Name + '_CR_SHP', em=True)
    xtr_grp = cmds.group(n=lib.project_Name + '_CR_XTR', em=True)

    cmds.parent(cc_grp, loc_grp, ik_grp, pp_grp)
    cmds.parent(skl_grp, pp_grp, scl_grp)
    cmds.parent(scl_grp, rot_grp)
    cmds.parent(rot_grp, ort_grp)
    cmds.parent(proxy_grp, highpoly_grp, skeleton_grp, crshp_grp, geo_grp)
    cmds.parent(ort_grp, geo_grp, xtr_grp, main_grp)

def locPlacement():
    ### locator placement as proxy jnt setup..
    # Spine locators...
    lib.LocatorPlacement('spine_01_LOC_C', 0, 139, -64.74)
    lib.LocatorPlacement('spine_2_LOC_C', 0, 138.943, -45.941)
    lib.LocatorPlacement('spine_3_LOC_C', 0, 137.794, -29.046)
    lib.LocatorPlacement('spine_4_LOC_C', 0, 135.817, -12.087)
    lib.LocatorPlacement('spine_5_LOC_C', 0, 133.261, 6.514)
    lib.LocatorPlacement('spine_6_LOC_C', 0, 130.34, 27.703)
    lib.LocatorPlacement('spine_7_LOC_C', 0, 127, 51.898)
    spineLocGrp = cmds.group('spine_01_LOC_C', 'spine_2_LOC_C', 'spine_3_LOC_C', 'spine_4_LOC_C', 'spine_5_LOC_C',
                             'spine_6_LOC_C', 'spine_7_LOC_C', n='spineLocGRP')

    # Neck locators...
    lib.LocatorPlacement('neck_1_LOC_C', 0, 127, 51.9)
    lib.LocatorPlacement('neck_2_LOC_C', 0, 124.06, 58.85)
    lib.LocatorPlacement('neck_3_LOC_C', 0, 124.4, 65.65)
    lib.LocatorPlacement('neck_4_LOC_C', 0, 131.86, 72.4)
    lib.LocatorPlacement('neck_5_LOC_C', 0, 143.3, 73.28)
    lib.LocatorPlacement('neck_6_LOC_C', 0, 153.49, 72.28)
    lib.LocatorPlacement('neck_7_LOC_C', 0, 162.7, 73.46)
    lib.LocatorPlacement('neck_8_LOC_C', 0, 167.53, 73.9)
    neckLocGrp = cmds.group('neck_1_LOC_C', 'neck_2_LOC_C', 'neck_3_LOC_C', 'neck_4_LOC_C', 'neck_5_LOC_C',
                            'neck_6_LOC_C', 'neck_7_LOC_C', 'neck_8_LOC_C', n='neckLocGRP')

    # Head locators...
    lib.LocatorPlacement('head_1_LOC_C', 0, 167.53, 73.9)
    lib.LocatorPlacement('head_2_LOC_C', 0, 167.53, 104.06)
    headLocGrp = cmds.group('head_1_LOC_C', 'head_2_LOC_C', n='headLocGRP')

    # Tail locators...
    lib.LocatorPlacement('tail_1_LOC_C', 0, 139, -67.26)
    lib.LocatorPlacement('tail_2_LOC_C', 0, 134.25, -77.56)
    lib.LocatorPlacement('tail_3_LOC_C', 0, 125.62, -83.65)
    lib.LocatorPlacement('tail_4_LOC_C', 0, 117.88, -85.63)
    tailLocGrp = cmds.group('tail_1_LOC_C', 'tail_2_LOC_C', 'tail_3_LOC_C', 'tail_4_LOC_C', n='tailLocGRP')

    # Back leg locators - left...
    lib.LocatorPlacement('leg_1_LOC_L', 12.8, 139.47, -38.5)
    lib.LocatorPlacement('leg_2_LOC_L', 5, 129.83, -60.68)
    # lib.LocatorPlacement('leg_2_LOC_L',11.015,129.83,-61.685)
    lib.LocatorPlacement('leg_3_LOC_L', 16.9, 94.2, -46)
    lib.LocatorPlacement('leg_4_LOC_L', 11.34, 58.47, -73.16)
    lib.LocatorPlacement('leg_5_LOC_L', 14.53, 15.7, -75.65)
    # lib.LocatorPlacement('leg_6_LOC_L',14.53,7.5,-72)
    lib.LocatorPlacement('leg_6_LOC_L', 14.53, 2.45, -69.6)
    lib.LocatorPlacement('leg_7_LOC_L', 14.53, 0, -62.36)
    backlegLocGrp = cmds.group('leg_1_LOC_L', 'leg_2_LOC_L', 'leg_3_LOC_L', 'leg_4_LOC_L', 'leg_5_LOC_L', 'leg_6_LOC_L',
                               'leg_7_LOC_L', n='backLegLocGRP')

    # front arm locators - left...
    # lib.LocatorPlacement('clavicle_1_LOC_L',10.3,101.83,43.5)
    lib.LocatorPlacement('clavicle_1_LOC_L', -18.595, 101.83, 28.074)
    lib.LocatorPlacement('clavicle_2_LOC_L', 15.63, 109.34, 45.5)
    lib.LocatorPlacement('clavicle_3_LOC_L', 5.7, 152.2, 32.2)
    lib.LocatorPlacement('arm_1_LOC_L', 15.63, 109.34, 45.5)
    lib.LocatorPlacement('arm_2_LOC_L', 13.62, 86.44, 37.12)
    lib.LocatorPlacement('arm_3_LOC_L', 13.55, 57.75, 35.57)
    lib.LocatorPlacement('arm_4_LOC_L', 14.22, 14.1, 33.58)
    # lib.LocatorPlacement('arm_5_LOC_L',14.22,7.33,36.38)
    lib.LocatorPlacement('arm_5_LOC_L', 14.22, 3.12, 39.18)
    lib.LocatorPlacement('arm_6_LOC_L', 14.22, 0, 46.76)
    frontArmLocGrp = cmds.group('clavicle_1_LOC_L', 'clavicle_2_LOC_L', 'clavicle_3_LOC_L', 'arm_1_LOC_L',
                                'arm_2_LOC_L',
                                'arm_3_LOC_L', 'arm_4_LOC_L', 'arm_5_LOC_L', 'arm_6_LOC_L', n='frontArmLocGRP')

    # pelvis locator...

    lib.LocatorPlacement('pelvis_1_LOC_C', 0, 139.47, -38.5)
    lib.LocatorPlacement('pelvis_2_LOC_C', 0, 127.13, -74.78)
    pelvisLocGrp = cmds.group('pelvis_1_LOC_C', 'pelvis_2_LOC_C', n='pelvisLocGRP')

    cmds.parent('spineLocGRP', 'neckLocGRP', 'headLocGRP', 'tailLocGRP', 'backLegLocGRP', 'frontArmLocGRP',
                'pelvisLocGRP',
                lib.project_Name + '_CR_LOC')

    cmds.select(d=True)
    cmds.hide(lib.project_Name + '_CR_LOC')

def globalController():
    lib.controlType('circleFourArrow',lib.project_Name +'_Translation_cc',80,lib.project_Name +'_Translation_cc_off')
    cmds.setAttr(lib.project_Name +'_Translation_cc_off'+'.tz',-10)
    lib.controlType('circle', lib.project_Name + '_Scale_cc', 70, lib.project_Name + '_Scale_cc_off')
    cmds.setAttr(lib.project_Name + '_Scale_cc' + '.rx', 90)
    cmds.select(d=True)
    cmds.makeIdentity(lib.project_Name + '_Scale_cc',apply=1,t=1,r=1,s=1,n=0,pn=1)
    cmds.setAttr(lib.project_Name + '_Scale_cc_off' + '.tz', -10)
    cmds.select(d=True)
    cmds.parent(lib.project_Name + '_Scale_cc_off',lib.project_Name +'_Translation_cc')
    cmds.parent(lib.project_Name + '_Translation_cc_off',lib.project_Name +'_CR_ALL' )
    cmds.select(d=True)
    cmds.parentConstraint(lib.project_Name + '_Scale_cc',lib.project_Name + '_CR_ORT',mo=1)
    cmds.scaleConstraint(lib.project_Name + '_Scale_cc', lib.project_Name + '_CR_SCL', mo=1)








