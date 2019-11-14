#coding:utf-8

#————————————公共模块脚本——————————————
'''修改人：蒋玉杰'''
'''版本号：V1.0.201909241'''
'''修改内容：模板定义'''

from PIL import Image
import math
import operator
from functools import reduce
import time,csv,json,os
from selenium import webdriver



#登录函数
def login(self,publicLogin):
    sitserver_url=publicLogin[0]
    loginUser=publicLogin[1]
    loginPwd=publicLogin[2]

    driver = webdriver.Chrome()
    driver.get(sitserver_url)

    driver.implicitly_wait(20)
    driver.maximize_window()

    driver.maximize_window()
    driver.implicitly_wait(20)

    driver.find_element_by_id("userName").send_keys(loginUser)  # 输入
    driver.implicitly_wait(20)

    driver.find_element_by_id("password").send_keys(loginPwd)  # 输入
    driver.implicitly_wait(20)

    driver.find_element_by_class_name("login_button").click()
    driver.implicitly_wait(20)
    time.sleep(1)

    self.driver=driver

    print("登录成功")


#图片对比函数
def image_contrast(imgName):

    config_path = 'D:\\Project\\newIpSiteserver\\data\\conf\\config.json'
    with open(config_path, "r", encoding="utf-8-sig") as configfile:
        userConfig = json.load(configfile)
        configfile.close()

    screenshotPath=userConfig['screenshotPath']
    resultImagePath = userConfig['resultImagePtah']
    img1 = screenshotPath+"{}.png".format(imgName)  # 指定图片路径
    img2 = resultImagePath+"{}.png".format(imgName)  # 指定对比图片路径

    image1 = Image.open(img1)
    image2 = Image.open(img2)


    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )

    if result == 1:  # 自定义判断，只要返回True或False就行
        return True
    else:
        return False


def mkdirScreenshot(now):
    # 保存时间并新建截图文件夹
    config_path = 'D:\\Project\\newIpSiteserver\\data\\conf\\config.json'
    with open(config_path, "r", encoding="utf-8-sig") as configfile:
        userConfig = json.load(configfile)
        configfile.close()

    userConfig['now']=now+"\\"

    with open(config_path, "w+", encoding='utf-8-sig')as f:
        json.dump(userConfig, f, sort_keys=False, indent=4, ensure_ascii=False)
        f.close()

    #新建每次截图的文件夹
    route = userConfig['screenshotPath'] +now
    isExists = os.path.exists(route)
    if not isExists:
        os.mkdir(route)
    else:
        print('Already exist')

# def assertMethod(type, expectedValue, actualValue):#(断言类型，预期值，实际值）
#     if type=='Equal':
#         if expectedValue != actualValue:
#             self.driver.get_screenshot_as_file(screenshotPath.format(case_name))
#         self.assertEqual(expectedValue,actualValue)
#
#     elif type=='NotEqual':
#         if expectedValue != actualValue:
#             self.driver.get_screenshot_as_file(screenshotPath.format(case_name))
#         self.assertNotEqual(expectedValue, actualValue)
#不行有问题

def listQuery(recordStr):
    #例如部门信息列表中当前页的所有信息记录转化为列表[[],[],[]]
    #输入带标题的字符串

    list1 = recordStr.split("\n")
    recordlist = []
    for i in list1:
        recordlist.append(i.split(" "))
    return recordlist



if __name__ == '__main__':
    pass







