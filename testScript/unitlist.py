#coding:utf-8
#——————————————测试套件—————————————
import unittest
#from testScript.testHomepage import TestHomepage
from testScript.testEquipmentSetting import TestEquipmentSetting
from testScript.testInformationRecording import TestInformationRecording

def unitlist():

    testunit = unittest.TestSuite()  # 定义一个套件# 添加用例进去
    testunit.addTest(TestEquipmentSetting('test_vlanSetting_01001'))
    testunit.addTest(TestEquipmentSetting('test_communityFileManagement_01001'))
    testunit.addTest(TestEquipmentSetting('test_communityFileManagement_01002'))
    testunit.addTest(TestEquipmentSetting('test_communityFileManagement_01003'))
    testunit.addTest(TestEquipmentSetting('test_communityFileManagement_01004'))
    testunit.addTest(TestEquipmentSetting('test_vlanSetting_01002'))
    testunit.addTest(TestEquipmentSetting('test_vlanSetting_01003'))
    #
    testunit.addTest(TestInformationRecording('test_informationRelease_01001'))
    testunit.addTest(TestInformationRecording('test_informationRelease_01002'))
    testunit.addTest(TestInformationRecording('test_informationRelease_01003'))



    #testunit.addTest(TestHomepage('test_homepage_01001'))
    #testunit.addTest(TestHomepage('test_homepage_01003'))

    return testunit


if __name__=="__main__":
    unitlist=unitlist()
    runner = unittest.TextTestRunner()
    runner.run(unitlist)



































