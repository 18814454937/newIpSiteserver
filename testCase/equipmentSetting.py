#coding:utf-8
#————————————设备配置用例脚本——————————————

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


class EquipmentSetting:
    def initialize(self,userConfig):
        #设备配置模块用例初始化
        sitserver_url = userConfig["sitserver"]
        loginUser = userConfig["loginUser"]
        loginPwd = userConfig["loginPwd"]
        publicLogin=[sitserver_url,loginUser,loginPwd]

        self.more_xpath = "//*[@id='programConfig']"  # 设备配置的xpath,用于导航栏悬停鼠标
        self.wait=userConfig["wait"]

        public.login(self,publicLogin)




    def vlanSetting_01001(self,test_vlanSetting_01001):
        #新增一个VLAN
        #获取测试数据
        vlanName = test_vlanSetting_01001['vlanName']
        gateway = test_vlanSetting_01001['gateway']
        netmask = test_vlanSetting_01001['netmask']
        startIP = test_vlanSetting_01001['startIP']
        maxNumber = test_vlanSetting_01001['maxNumber']

        #测试步骤
        driver = self.driver
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        more_xpath = self.more_xpath# 设备配置的xpath
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("vlan").click()  # 以id找到社区网络设置点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        driver.find_element_by_class_name("new_select_button").click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("addVlanName").send_keys(vlanName)
        driver.find_element_by_id("addGateway").send_keys(gateway)
        driver.find_element_by_id("addSubnetMask").send_keys(netmask)
        driver.find_element_by_id("addStartIP").send_keys(startIP)
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("addMaxDeviceNumber").send_keys(maxNumber)
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("button[onclick='addVLAN()']").click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        #用例结果
        vlanList = driver.find_element_by_id('vlanBody').text #VLAN列表的

        if vlanList.find(vlanName)!=-1:
            return True
        else:
            return False


    def vlanSetting_01002(self,test_vlanSetting_01002):
        #编辑VLAN
        #获取测试数据
        vlanName=test_vlanSetting_01002['vlanName']
        maxNumber = test_vlanSetting_01002['maxNumber']
        updateVlan = test_vlanSetting_01002['updateVlan']


        # 测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("vlan").click()  # 以id找到社区网络设置点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        #获取要修改VLAN的序号
        serialNumber=driver.find_element_by_xpath("//td[text()='{}']/../td[1]".format(vlanName)).text
        driver.find_element_by_xpath("//*[@id='vlanBody']/tr[{}]/td[8]/button[2]".format(serialNumber)).click()  #修改
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('updateVlanName').clear()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('updateVlanName').send_keys(updateVlan)
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('updateMaxDeviceNumber').clear()
        time.sleep(self.wait)
        driver.find_element_by_id('updateMaxDeviceNumber').send_keys(maxNumber)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("button[onclick='updateVLAN()']").click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        #用例结果
        newVlanName=driver.find_element_by_xpath("//*[@id='vlanBody']/tr[{}]/td[2]".format(serialNumber)).text  #获取用例新名字
        newmaxNumber = driver.find_element_by_xpath("//*[@id='vlanBody']/tr[{}]/td[6]".format(serialNumber)).text
        if updateVlan+maxNumber==newVlanName+newmaxNumber:
            return True
        else:
            return False


    def vlanSetting_01003(self,test_vlanSetting_01003):
        #删除VLAN
        # 获取测试数据
        vlanName=test_vlanSetting_01003['vlanName']

        # 测试步骤
        driver=self.driver

        more_xpath= self.more_xpath
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  #
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        driver.find_element_by_id("vlan").click()  # 以id找到社区网络设置点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        serialNumber = driver.find_element_by_xpath("//td[text()='{}']/../td[1]".format(vlanName)).text
        driver.find_element_by_xpath("//*[@id='vlanBody']/tr[{}]/td[8]/button[3]".format(serialNumber)).click()  #删除
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        driver.switch_to.alert.accept()#弹框
        #driver.implicitly_wait(10)
        time.sleep(self.wait)


        # 用例结果
        vlanList = driver.find_element_by_id('vlanBody').text

        if vlanList.find(vlanName) == -1:
            return True
        else:
            return False


    def vlanSetting_01004(self,test_vlanSetting_01004):
        #取消新增VLAN
        # 获取测试数据
        vlanName=test_vlanSetting_01004['vlanName']
        gateway = test_vlanSetting_01004['gateway']
        netmask = test_vlanSetting_01004['netmask']
        startIP = test_vlanSetting_01004['startIP']
        maxNumber = test_vlanSetting_01004['maxNumber']

        # 测试步骤
        driver = self.driver
        # driver.implicitly_wait(10)
        time.sleep(self.wait)
        more_xpath = self.more_xpath  # 设备配置的xpath
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        # driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        # driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("vlan").click()  # 以id找到社区网络设置点击
        # driver.implicitly_wait(10)
        time.sleep(self.wait)

        driver.find_element_by_class_name("new_select_button").click()
        # driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("addVlanName").send_keys(vlanName)
        driver.find_element_by_id("addGateway").send_keys(gateway)
        driver.find_element_by_id("addSubnetMask").send_keys(netmask)
        driver.find_element_by_id("addStartIP").send_keys(startIP)
        # driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("addMaxDeviceNumber").send_keys(maxNumber)
        # driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//button[@onclick='addVLAN()']/../button[text()='取消']").click()
        # driver.implicitly_wait(10)
        time.sleep(self.wait)

        # 用例结果
        vlanList = driver.find_element_by_id('vlanBody').text

        if vlanList.find(vlanName) == -1:
            return True
        else:
            return False


    def vlanSetting_01005(self,test_vlanSetting_01005):
        #取消删除VLAN，取消成功
        # 获取测试数据
        vlanName=test_vlanSetting_01005['vlanName']

        # 测试步骤
        driver = self.driver
        # driver.implicitly_wait(10)
        time.sleep(self.wait)
        more_xpath = self.more_xpath  # 设备配置的xpath
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        # driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        # driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("vlan").click()  # 以id找到社区网络设置点击
        # driver.implicitly_wait(10)
        time.sleep(self.wait)

        serialNumber = driver.find_element_by_xpath("//td[text()='{}']/../td[1]".format(vlanName)).text
        driver.find_element_by_xpath("//*[@id='vlanBody']/tr[{}]/td[8]/button[3]".format(serialNumber)).click()  #删除
        time.sleep(self.wait)
        driver.switch_to.alert.dismiss()  # 取消弹框
        time.sleep(self.wait)

        # 用例结果
        vlanList = driver.find_element_by_id('vlanBody').text

        if vlanList.find(vlanName) != -1:
            return True
        else:
            return False


    def vlanSetting_01006(self,test_vlanSetting_01006):
        #取消修改VLAN，取消成功
        # 获取测试数据
        vlanName=test_vlanSetting_01006['vlanName']
        maxNumber = test_vlanSetting_01006['maxNumber']

        # 测试步骤
        driver = self.driver

        more_xpath = self.more_xpath  # 设备配置的xpath"
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))  # 鼠标移动到设备配置
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()  # 将鼠标定位到设备配置的菜单选项展开下级菜单
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("vlan").click()  # 以id找到社区网络设置点击
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        #获取要修改VLAN的序号
        serialNumber=driver.find_element_by_xpath("//td[text()='{}']/../td[1]".format(vlanName)).text
        originalMaxNumber= driver.find_element_by_xpath("//*[@id='vlanBody']/tr[{}]/td[6]".format(serialNumber)).text
        time.sleep(self.wait)
        driver.find_element_by_xpath("//*[@id='vlanBody']/tr[{}]/td[8]/button[2]".format(serialNumber)).click()  #修改
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('updateMaxDeviceNumber').clear()
        time.sleep(self.wait)
        driver.find_element_by_id('updateMaxDeviceNumber').send_keys(maxNumber)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//button[@onclick='updateVLAN()']/../button[text()='取消']").click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        #用例结果
        newMaxNumber = driver.find_element_by_xpath("//*[@id='vlanBody']/tr[{}]/td[6]".format(serialNumber)).text

        if originalMaxNumber==newMaxNumber:
            return True
        else:
            return False


    def communityFileManagement_01001(self,test_communityFileManagement_01001):
        #新增默认区
        # 获取测试数据

        # 测试步骤
        driver = self.driver

        # 设备配置悬停，进入设备档案管理
        more_xpath = self.more_xpath
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("addressBook").click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)


        #获取最后一个区(只能在不改变名字的时候用)
        equipmentListName=driver.find_element_by_id('mainTree_1_ul').text    #获取刚进入设备配置左侧小区下的列表名称
        zoneListName=equipmentListName[:equipmentListName.find('#')-2]   #截取总社区下设备前的区列表
        lastZone =zoneListName[zoneListName.rfind('\n')+1:]          #从右往左查出第一个回车，然后获取最后一个区的名称
        result=str(int(lastZone[:-1])+1)+'区'  #下一个区，用来做断言结果，只适用默认区号(**区)

        #右键打开testTeam下的的菜单
        testTeamMenu = driver.find_element_by_id("mainTree_1_span")
        ActionChains(driver).move_to_element(testTeamMenu).context_click(testTeamMenu).perform()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        #新增区
        driver.find_element_by_id('add_area').click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        driver.find_element_by_css_selector("button[onclick='addAreaSave()']").click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        # 用例结果
        newZoneName=driver.find_element_by_xpath("//ul[@id='mainTree_1_ul']//span[text()='{}']".format(result)).text

        if result == newZoneName:
            return True
        else:
            return False

    def communityFileManagement_01002(self,test_communityFileManagement_01002):
        #新增区并改变所有默认配置
        # 获取测试数据
        zoneDescription = test_communityFileManagement_01002['zoneDescription']
        zone=test_communityFileManagement_01002['zone']
        zoneVLAN = test_communityFileManagement_01002['zoneVLAN']
        equipmentType = test_communityFileManagement_01002['equipmentType']
        number = test_communityFileManagement_01002['number']
        result = test_communityFileManagement_01002['result']

        # 测试步骤
        driver = self.driver

        #设备配置悬停，进入设备档案管理
        more_xpath = self.more_xpath
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("addressBook").click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        #右键打开testTeam下的的菜单
        testTeamMenu = driver.find_element_by_id("mainTree_1_span")
        ActionChains(driver).move_to_element(testTeamMenu).context_click(testTeamMenu).perform()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        #新增区
        driver.find_element_by_id('add_area').click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        #修改设置
        driver.find_element_by_id('add_area_district').clear()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('add_area_district').send_keys(zoneDescription)
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('add_area_alias').clear()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('add_area_alias').send_keys(zone)
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//*[@id='add_area_vlan']/option[text()='{}']".format(zoneVLAN)).click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//*[@id='add_area_device_type']/option[text()='{}']".format(equipmentType)).click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('add_area_device_number').clear()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('add_area_device_number').send_keys(number)
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        #添加，确定
        driver.find_element_by_id('add_area_add_btn').click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("button[onclick='addAreaSave()']").click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        time.sleep(2)

        # 用例结果（展开区，获取设备列表）
        driver.find_element_by_xpath\
            ("//ul[@id='mainTree_1_ul']//span[text()='{}']/../../span[1]".format(zone)).click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        equipmentlist=driver.find_element_by_xpath\
            ("//ul[@id='mainTree_1_ul']//span[text()='{}']/../../ul".format(zone)).text
        print(equipmentlist)

        if equipmentlist.find(result) != -1:
            return True
        else:
            return False

    def communityFileManagement_01003(self,test_communityFileManagement_01003):
        # 在区下新增一台设备
        # 获取测试数据
        zone = test_communityFileManagement_01003['zone']
        VLAN = test_communityFileManagement_01003['VLAN']
        equipmentType = test_communityFileManagement_01003['equipmentType']
        number = test_communityFileManagement_01003['number']
        result = test_communityFileManagement_01003['result']

        # 测试步骤
        driver = self.driver

        # 设备配置悬停，进入设备档案管理
        more_xpath = self.more_xpath
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("addressBook").click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)


        #右键打开要新增设备区下的的菜单
        zoneMenu = driver.find_element_by_xpath \
            ("//ul[@id='mainTree_1_ul']//span[text()='{}']".format(zone))
        ActionChains(driver).move_to_element(zoneMenu).context_click(zoneMenu).perform()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id('add_device').click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//*[@id='vlanSelect']/option[text()='{}']".format(VLAN)).click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//*[@id='disDeviceType']/option[text()='{}']".format(equipmentType)).click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("addDevice_deviceNum").send_keys(number)
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("button[onclick='addDeviceList()']").click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_css_selector("button[onclick='addDeviceSave()']").click()    #确定
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        time.sleep(2)
        print(1)
        # 用例结果
        equipmentlist=driver.find_element_by_xpath \
            ("//ul[@id='mainTree_1_ul']//span[text()='{}']/../../ul".format(zone)).text
        print(equipmentlist)


        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        if equipmentlist.find(result) != -1:
            return True
        else:
            return False


    def communityFileManagement_01004(self,test_communityFileManagement_01004):
        #删除区
        # 获取测试数据
        zone = test_communityFileManagement_01004['zone']

        # 测试步骤
        driver = self.driver

        # 设备配置悬停，进入设备档案管理
        more_xpath = self.more_xpath
        more_menu = WebDriverWait(driver=driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, more_xpath)))
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        ActionChains(driver=driver).move_to_element(more_menu).perform()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_id("addressBook").click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)


        #勾选然后右键打开删除区下的的菜单
        driver.find_element_by_xpath \
            ("//ul[@id='mainTree_1_ul']//span[text()='{}']/../../span[2]".format(zone)).click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        zoneMenu = driver.find_element_by_xpath \
            ("//ul[@id='mainTree_1_ul']//span[text()='{}']".format(zone))
        ActionChains(driver).move_to_element(zoneMenu).context_click(zoneMenu).perform()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.find_element_by_xpath("//div[@id='mainTreeMenu']/ul/li[@id='delete']").click()
        #driver.implicitly_wait(10)
        time.sleep(self.wait)
        driver.switch_to.alert.accept()
        time.sleep(2)
        #driver.implicitly_wait(10)
        time.sleep(self.wait)

        # 用例结果
        addrList=driver.find_element_by_xpath("//ul[@id='mainTree_1_ul']").text

        if addrList.find(zone) == -1:
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
    equipmentSettingData_path = userConfig["projectPath"] + 'data\\testData\\equipmentSettingData.json'
    with open(equipmentSettingData_path, "r+", encoding='utf-8-sig')as f:
        equipmentSettingData = json.load(f)
        f.close()

    mm=EquipmentSetting()
    mm.initialize(userConfig)
    mm.vlanSetting_01001(equipmentSettingData['test_vlanSetting_01001'])