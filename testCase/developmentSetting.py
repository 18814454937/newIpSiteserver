#coding:utf-8
#————————————开发设置用例脚本——————————————

'''修改人：蒋玉杰'''
'''版本号：V1.0.201909241'''
'''修改内容：模板定义'''

from selenium import webdriver
import csv
import unittest
import sys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from testCase import public


class DevelopmentSetting:
    def initialize(self,userConfig):
        #主页模块用例初始化
        sitserver_url = userConfig["sitserver"]
        loginUser = userConfig["loginUser"]
        loginPwd = userConfig["loginPwd"]

        publicLogin=[sitserver_url,loginUser,loginPwd]
        public.login(self,publicLogin)


    def systemSubjectManagement_01001(self,test_systemSubjectManagement_01001):
        #'''用例标题'''
        #获取测试数据
        result = test_systemSubjectManagement_01001['result']

        #测试步骤
        driver = self.driver



        #用例结果

        if result==result:   #自定义判断，只要返回True或False就行
            return True
        else:
            return False




if __name__ == "__main__":
    import json

    # 导入用户配置文件
    config_path = 'D:\\Project\\newIpSiteserver\\data\\conf\\config.json'
    with open(config_path, "r", encoding="utf-8-sig") as f:
        userConfig = json.load(f)
        f.close()

    # 导入测试数据文件
    developmentSetting_path = userConfig["projectPath"] + 'data\\testData\\developmentSettingData.json'
    with open(developmentSetting_path, "r+", encoding='utf-8-sig')as f:
        developmentSettingData = json.load(f)
        f.close()

    mm=DevelopmentSetting()
    mm.initialize(userConfig)
    mm.systemSubjectManagement_01001(developmentSettingData['test_systemSubjectManagement_01001'])