# coding:utf-8

# —————————设备配置测试脚本——————————————

import sys
import unittest
import json
from testCase.informationRecording import InformationRecording
#sys.path.append('D:\\Project\\newIpSiteserver\\testCase\\public')



# 导入用户配置文件
config_path = 'D:\\Project\\newIpSiteserver\\data\\conf\\config.json'
with open(config_path, "r", encoding="utf-8-sig") as f:
    userConfig = json.load(f)
    f.close()

# 导入测试数据文件
informationRecordingData_path = userConfig["projectPath"] + 'data\\testData\\informationRecordingData.json'
with open(informationRecordingData_path, "r+", encoding='utf-8_sig')as f:
    informationRecordingData = json.load(f)
    f.close()


class TestInformationRecording(unittest.TestCase):
    def setUp(self):
        # 初始化用户配置
        self.contratImageEnable = userConfig["contratImageEnable"]
        self.screenshotPath = userConfig["screenshotPath"]
        self.resultImagePtah = userConfig["resultImagePtah"]
        self.now=userConfig["now"]

        # 调用模块初始化函数并传入配置文件
        InformationRecording.initialize(self, userConfig)
        self.driver=self.driver

    def test_informationRelease_01001(self):
        # 获取函数名和截图路径
        self.case_name = sys._getframe().f_code.co_name
        case_name = self.case_name
        screenshotPath = self.screenshotPath +self.now+ '{}.png'

        # 调用用例并传入测试数据
        try:
            result = InformationRecording.informationRelease_01001(self,informationRecordingData['test_informationRelease_01001'])
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshotPath.format(case_name))
            raise (e)

        # 失败截图和断言
        if result != True:
            self.driver.get_screenshot_as_file(screenshotPath.format(case_name))
        self.assertTrue(result)

    def test_informationRelease_01002(self):
        # 获取函数名和截图路径
        self.case_name = sys._getframe().f_code.co_name
        case_name = self.case_name
        screenshotPath = self.screenshotPath +self.now+'{}.png'

        # 调用用例并传入测试数据
        try:
            result = InformationRecording.informationRelease_01002(self,informationRecordingData['test_informationRelease_01002'])
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshotPath.format(case_name))
            raise (e)

        # 失败截图和断言
        if result != True:
            self.driver.get_screenshot_as_file(screenshotPath.format(case_name))
        self.assertTrue(result)

    def test_informationRelease_01003(self):
        # 获取函数名和截图路径
        self.case_name = sys._getframe().f_code.co_name
        case_name = self.case_name
        screenshotPath = self.screenshotPath +self.now+'{}.png'

        # 调用用例并传入测试数据
        try:
            result = InformationRecording.informationRelease_01003(self,informationRecordingData['test_informationRelease_01003'])
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshotPath.format(case_name))
            raise (e)

        # 失败截图和断言
        if result != True:
            self.driver.get_screenshot_as_file(screenshotPath.format(case_name))
        self.assertTrue(result)


    def tearDown(self):
        # 截图，配置文件中使能
        contratImageEnable = self.contratImageEnable
        resultImagePtah = self.resultImagePtah + '{}.png'

        case_name = self.case_name
        driver = self.driver

        if contratImageEnable == '1':
            driver.get_screenshot_as_file(resultImagePtah.format(case_name))
        elif contratImageEnable == '0':
            pass
        else:
            print("配置错误,只能是0和1")

        # 关闭浏览器
        driver.quit()
        print('结束')

if __name__ == '__main__':
    unittest.main()
