#coding:utf-8
#————————————信息记录用例脚本——————————————

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
#sys.path.append("D:\\Project\\newIpSiteserver\\testCase\\public")
from testCase import public


class InformationRecording:
    def initialize(self,userConfig):
        #主页模块用例初始化
        sitserver_url = userConfig["sitserver"]
        loginUser = userConfig["loginUser"]
        loginPwd = userConfig["loginPwd"]
        publicLogin=[sitserver_url,loginUser,loginPwd]

        self.more_xpath = "//*[@id='propertyControl']"  # 设备配置的xpath,用于导航栏悬停鼠标
        self.wait=userConfig["wait"]

        public.login(self,publicLogin)




    def informationRelease_01001(self,test_informationRelease_01001):
        #发送默认的物业消息，文字消息
        #获取测试数据
        title = test_informationRelease_01001['title']
        content = test_informationRelease_01001['content']
        result = test_informationRelease_01001['result']

        #测试步骤
        driver = self.driver
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        more_xpath = self.more_xpath# 设备配置的xpath
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("messagePublish").click()  # 以id找到信息发布点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        driver.find_element_by_id("addTitle").send_keys(title)
        driver.find_element_by_id("addContent").send_keys(content)
        driver.find_element_by_id("mainTree_1_check").click()
        driver.find_element_by_css_selector("button[onclick='addPropertyMessageRecord()']").click()
        time.sleep(self.wait)
        driver.find_element_by_link_text("确定").click()

        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@class='modal-footer']/button[text()='详情']").click()

        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        #用例结果
        informationtype = driver.find_element_by_xpath("//*[@id='publishMessageBody']/tr/td[2]").text
        infomationtitle=driver.find_element_by_xpath("//*[@id='publishMessageBody']/tr/td[5]").text


        if result==informationtype+infomationtitle:
            return True
        else:
            return False

    def informationRelease_01002(self,test_informationRelease_01002):
        #发送默认的紧急通知，文字消息
        #获取测试数据
        informatiaonType = test_informationRelease_01002['informatiaonType']
        title = test_informationRelease_01002['title']
        content = test_informationRelease_01002['content']
        result = test_informationRelease_01002['result']

        #测试步骤
        driver = self.driver
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        more_xpath = self.more_xpath# 设备配置的xpath
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("messagePublish").click()  # 以id找到信息发布点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        driver.find_element_by_xpath("//select[@id='addMessageType']/option[text()='{}']".format(informatiaonType)).click()
        driver.find_element_by_id("addTitle").send_keys(title)
        driver.find_element_by_id("addContent").send_keys(content)
        driver.find_element_by_id("mainTree_1_check").click()
        driver.find_element_by_css_selector("button[onclick='addPropertyMessageRecord()']").click()
        time.sleep(self.wait)
        driver.find_element_by_link_text("确定").click()

        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@class='modal-footer']/button[text()='详情']").click()

        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        #用例结果
        informationtype = driver.find_element_by_xpath("//*[@id='publishMessageBody']/tr/td[2]").text
        infomationtitle=driver.find_element_by_xpath("//*[@id='publishMessageBody']/tr/td[5]").text


        if result==informationtype+infomationtitle:
            return True
        else:
            return False


    def informationRelease_01003(self,test_informationRelease_01003):
        #发送默认的广告消息，文字消息
        #获取测试数据
        informatiaonType = test_informationRelease_01003['informatiaonType']
        title = test_informationRelease_01003['title']
        content = test_informationRelease_01003['content']
        result = test_informationRelease_01003['result']


        #测试步骤
        driver = self.driver
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        more_xpath = self.more_xpath# 设备配置的xpath
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("messagePublish").click()  # 以id找到信息发布点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        driver.find_element_by_xpath("//select[@id='addMessageType']/option[text()='{}']".format(informatiaonType)).click()
        driver.find_element_by_id("addTitle").send_keys(title)
        driver.find_element_by_id("addContent").send_keys(content)
        driver.find_element_by_id("mainTree_1_check").click()
        driver.find_element_by_css_selector("button[onclick='addPropertyMessageRecord()']").click()
        time.sleep(self.wait)
        driver.find_element_by_link_text("确定").click()

        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@class='modal-footer']/button[text()='详情']").click()

        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        #用例结果
        informationtype = driver.find_element_by_xpath("//*[@id='publishMessageBody']/tr/td[2]").text
        infomationtitle=driver.find_element_by_xpath("//*[@id='publishMessageBody']/tr/td[5]").text


        if result==informationtype+infomationtitle:
            return True
        else:
            return False

if __name__ == "__main__":
    import json

    # 导入用户配置文件
    config_path = 'D:\\Project\\newIpSiteserver\\data\\conf\\config.json'
    with open(config_path, "r", encoding="utf-8-sig") as configfile:
        userConfig = json.load(configfile)

    # 导入测试数据文件
        informationRecordingData_path = userConfig["projectPath"] + 'data\\testData\\informationRecordingData.json'
    with open(informationRecordingData_path, "r+", encoding='utf-8_sig')as f:
        informationRecordingData = json.load(f)

    mm=InformationRecording()
    mm.initialize(userConfig)
    mm.informationRelease_01001(informationRecordingData['test_informationRelease_01001'])