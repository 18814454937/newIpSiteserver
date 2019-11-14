#coding:utf-8
#————————————社区管理用例脚本——————————————

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


class CommunityManagement:
    def initialize(self,userConfig):
        #主页模块用例初始化
        sitserver_url = userConfig["sitserver"]
        loginUser = userConfig["loginUser"]
        loginPwd = userConfig["loginPwd"]
        publicLogin=[sitserver_url,loginUser,loginPwd]

        self.more_xpath = "//*[@id='guardControl']"  # 设备配置的xpath,用于导航栏悬停鼠标
        self.wait=userConfig["wait"]

        public.login(self,publicLogin)


    def communityFileManagement_01001(self,test_communityFileManagement_01001):
        #社区档案管理界面显示
        #获取测试数据

        #测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("community").click()  # 以id找到社区档案管理点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        #图片对比结果从公共模块输出



    def departmentInformationManagement_01001(self,test_departmentInformationManagement_01001):
        #新增部门，输入合法部门名称，新增成功
        #获取测试数据
        departmentName = test_departmentInformationManagement_01001['departmentName']
        result = test_departmentInformationManagement_01001['result']

        #测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@id='guardControl']//div[text()='部门信息管理']").click()  # 找到部门信息管理点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("input[onclick='showAddUser()'] ").click()
        time.sleep(self.wait)
        driver.find_element_by_id("addDepartmentName").send_keys(departmentName)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("button[onclick='addDepartmentCommit()']").click()
        time.sleep(self.wait)

        #找出最下面一条记录（只有一页时有效）
        bottom=driver.find_element_by_id('departmentData').find_elements_by_tag_name('tr')[-1]

        name=bottom.find_elements_by_tag_name('td')[2].text
        superiorName=bottom.find_elements_by_tag_name('td')[3].text

        if result==name+superiorName:
            return True
        else:
            return False


    def departmentInformationManagement_01002(self,test_departmentInformationManagement_01002):
        #新增部门，输入合法部门名称，新增成功
        #获取测试数据
        departmentName = test_departmentInformationManagement_01002['departmentName']
        result = test_departmentInformationManagement_01002['result']

        #测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@id='guardControl']//div[text()='部门信息管理']").click()  # 找到部门信息管理点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("input[onclick='showAddUser()'] ").click()
        time.sleep(self.wait)
        driver.find_element_by_id("addDepartmentName").send_keys(departmentName)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("button[onclick='addDepartmentCommit()']").click()
        time.sleep(self.wait)

        #找出最下面一条记录（只有一页时有效）
        bottom=driver.find_element_by_id('departmentData').find_elements_by_tag_name('tr')[-1]

        name=bottom.find_elements_by_tag_name('td')[2].text
        superiorName=bottom.find_elements_by_tag_name('td')[3].text

        if result==name+superiorName:
            return True
        else:
            return False

    def departmentInformationManagement_01003(self,test_departmentInformationManagement_01003):
        #新增部门，输入合法部门名称和上级部门名，新增成功
        #获取测试数据
        departmentName = test_departmentInformationManagement_01003['departmentName']
        superiorDepartment = test_departmentInformationManagement_01003['superiorDepartment']

        #测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@id='guardControl']//div[text()='部门信息管理']").click()  # 找到部门信息管理点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("input[onclick='showAddUser()'] ").click()
        time.sleep(self.wait)
        driver.find_element_by_id("addDepartmentName").send_keys(departmentName)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//*[@id='addParentDepartment']/open[text()='{}']".format(superiorDepartment)).click()
        time.sleep(self.wait)
        driver.find_element_by_css_selector("button[onclick='addDepartmentCommit()']").click()
        time.sleep(self.wait)

        #找出最下面一条记录（只有一页时有效）
        bottom=driver.find_element_by_id('departmentData').find_elements_by_tag_name('tr')[-1]

        name=bottom.find_elements_by_tag_name('td')[2].text
        superiorName=bottom.find_elements_by_tag_name('td')[3].text

        if departmentName+superiorDepartment==name+superiorName:
            return True
        else:
            return False


    def departmentInformationManagement_01004(self,test_departmentInformationManagement_01004):
        #新增部门，输入合法部门名称和上级部门名，新增成功
        #获取测试数据
        departmentName = test_departmentInformationManagement_01004['departmentName']
        updateDepartmentName=test_departmentInformationManagement_01004['updateDepartmentName']
        superiorDepartment = test_departmentInformationManagement_01004['superiorDepartment']

        #测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@id='guardControl']//div[text()='部门信息管理']").click()  # 找到部门信息管理点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        driver.find_element_by_link_text(departmentName).find_element_by_xpath\
            ("//td[text()='{}']/../td[5]/button[text()='{}']".format(departmentName,'修改')).click()
        time.sleep(self.wait)
        driver.find_element_by_id("updateDepartmentName").send_keys(updateDepartmentName)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//*[@id='updateParentDepartment']/open[text()='{}']".format(superiorDepartment)).click()
        time.sleep(self.wait)
        driver.find_element_by_css_selector("button[onclick='updateDepartmentConfirm()']").click()
        time.sleep(self.wait)

        #找出最下面一条记录（只有一页时有效）
        updaterecord=driver.find_element_by_link_text(departmentName).find_element_by_xpath\
            ("//td[text()='{}']/../]".format(updateDepartmentName))



        name=updaterecord.find_elements_by_tag_name('td')[2].text
        superiorName=updaterecord.find_elements_by_tag_name('td')[3].text

        if updateDepartmentName+superiorDepartment==name+superiorName:
            return True
        else:
            return False


    def departmentInformationManagement_01005(self,test_departmentInformationManagement_01005):
        #查询部门，输入部门名称后查询，模糊查询成功
        #获取测试数据
        selectDepartmentName = test_departmentInformationManagement_01005['selectDepartmentName']

        #测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@id='guardControl']//div[text()='部门信息管理']").click()  # 找到部门信息管理点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('departName').send_keys(selectDepartmentName)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("[onclick='searchDepartName()']").click()
        time.sleep(self.wait)
        #获取当前页记录字符串
        recordStr = driver.find_element_by_xpath("//*[@id='departmentData']/..").text
        #调用公共模块转换为列表
        recordlist=public.listQuery(recordStr)
        #获取部门名称索引
        departmentindex=recordlist.index('部门名称')
        for i in range(len(recordlist)):
            if recordlist[i][departmentindex].find(selectDepartmentName) != -1:
                pass
            else:
                return False
            return True


    def departmentInformationManagement_01006(self,test_departmentInformationManagement_01006):
        #查询部门，输入部门名称后查询，模糊查询成功
        #获取测试数据
        selectSuperiorDepartment = test_departmentInformationManagement_01006['selectSuperiorDepartment']

        #测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@id='guardControl']//div[text()='部门信息管理']").click()  # 找到部门信息管理点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('parentName').send_keys(selectSuperiorDepartment)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("[onclick='searchDepartName()']").click()
        time.sleep(self.wait)
        #获取当前页记录字符串
        recordStr = driver.find_element_by_xpath("//*[@id='departmentData']/..").text
        #调用公共模块转换为列表
        recordlist=public.listQuery(recordStr)
        #获取上级部门名称索引
        superiorDepartmentindex=recordlist.index('上级部门名称')
        for i in range(len(recordlist)):
            if recordlist[i][superiorDepartmentindex].find(selectSuperiorDepartment) != -1:
                pass
            else:
                return False
            return True


    def departmentInformationManagement_01007(self,test_departmentInformationManagement_01007):
        #查询部门，输入部门名称后查询，模糊查询成功
        #获取测试数据
        selectDepartmentName = test_departmentInformationManagement_01007['selectDepartmentName']
        selectSuperiorDepartment = test_departmentInformationManagement_01007['selectSuperiorDepartment']

        #测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@id='guardControl']//div[text()='部门信息管理']").click()  # 找到部门信息管理点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('parentName').send_keys(selectSuperiorDepartment)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("[onclick='searchDepartName()']").click()
        time.sleep(self.wait)
        #获取当前页记录字符串
        recordStr = driver.find_element_by_xpath("//*[@id='departmentData']/..").text
        #调用公共模块转换为列表
        recordlist=public.listQuery(recordStr)
        #获取部门名称、上级部门名称索引
        departmentindex = recordlist.index('部门名称')
        superiorDepartmentindex=recordlist.index('上级部门名称')
        for i in range(len(recordlist)):
            if recordlist[i][departmentindex].find(selectDepartmentName) != -1:
                pass
            elif recordlist[i][superiorDepartmentindex].find(selectSuperiorDepartment) != -1:
                pass
            else:
                return False
        return True


    def departmentInformationManagement_01008(self,test_departmentInformationManagement_01008):
        #新增部门，输入合法部门名称和上级部门名，新增成功
        #获取测试数据
        departmentName = test_departmentInformationManagement_01008['departmentName']
        #测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@id='guardControl']//div[text()='部门信息管理']").click()  # 找到部门信息管理点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        driver.find_element_by_link_text(departmentName).find_element_by_xpath\
            ("//td[text()='{}']/../td[5]/button[text()='{}']".format(departmentName,'删除')).click()
        time.sleep(self.wait)
        driver.find_element_by_xpath("//*[@id='deleteModal']//button[text()='确定']").click()
        time.sleep(self.wait)
        # 获取当前页记录字符串
        recordStr = driver.find_element_by_xpath("//*[@id='departmentData']/..").text
        # 调用公共模块转换为列表
        recordlist = public.listQuery(recordStr)
        # 获取部门名称索引
        departmentindex = recordlist.index('部门名称')
        for i in range(len(recordlist)):
            if recordlist[i][departmentindex]!=departmentName:
                pass
            else:
                return False
        return True


    def departmentInformationManagement_01009(self,test_departmentInformationManagement_01009):
        #新增部门，输入合法部门名称和上级部门名，新增成功
        #获取测试数据
        departmentName = test_departmentInformationManagement_01009['departmentName']
        #测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@id='guardControl']//div[text()='部门信息管理']").click()  # 找到部门信息管理点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        driver.find_element_by_link_text(departmentName).find_element_by_xpath\
            ("//td[text()='{}']/../td[5]/button[text()='{}']".format(departmentName,'删除')).click()
        time.sleep(self.wait)
        driver.find_element_by_xpath("//*[@id='deleteModal']//button[text()='取消']").click()
        time.sleep(self.wait)
        # 获取当前页记录字符串
        recordStr = driver.find_element_by_xpath("//*[@id='departmentData']/..").text
        # 调用公共模块转换为列表
        recordlist = public.listQuery(recordStr)
        # 获取部门名称索引
        departmentindex = recordlist.index('部门名称')
        for i in range(len(recordlist)):
            if recordlist[i][departmentindex]==departmentName:
                return True
        return False


    def departmentInformationManagement_010010(self,test_departmentInformationManagement_010010):
        #查询部门，输入部门名称后查询，模糊查询成功
        #获取测试数据
        selectDepartmentName = test_departmentInformationManagement_010010['selectDepartmentName']
        selectSuperiorDepartment = test_departmentInformationManagement_010010['selectSuperiorDepartment']

        #测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@id='guardControl']//div[text()='部门信息管理']").click()  # 找到部门信息管理点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        # 获取当前页记录字符串
        recordStr = driver.find_element_by_xpath("//*[@id='departmentData']/..").text
        driver.find_element_by_id('parentName').send_keys(selectSuperiorDepartment)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("[onclick='searchDepartName()']").click()
        time.sleep(self.wait)
        driver.find_element_by_css_selecetor("[onclick='emptySearch()']").click()   #重置
        time.sleep(self.wait)


        #结果
        #首先判断是否清空输入框
        departmentNameFrame=driver.find_element_by_id('departName').get_attribute('value')
        SuperiorDepartmentNameFrame = driver.find_element_by_id('parentName').get_attribute('value')
        if departmentNameFrame=='':
            pass
        elif SuperiorDepartmentNameFrame=='':
            pass
        else:
            return False
        #判断页面显示记录是否与之前一致
        resetRecordStr = driver.find_element_by_xpath("//*[@id='departmentData']/..").text
        if recordStr==resetRecordStr:
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
    communityManagementData_path = userConfig["projectPath"] + 'data\\testData\\communityManagementData.json'
    with open(communityManagementData_path, "r+", encoding='utf-8-sig')as f:
        communityManagementData = json.load(f)
        f.close()

    mm=CommunityManagement()
    mm.initialize(userConfig)
    mm.communityFileManagement_01001(communityManagementData['test_communityFileManagement_01001'])