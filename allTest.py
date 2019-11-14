#coding:utf-8

#——————————————测试报告——————————————


#reload(sys)
#sys.setdefaultencoding('utf-8')
#sys.getdefaultencoding()  #查看系统编码

import time,unittest
import os,sys,json
from HTMLTestRunner import HTMLTestRunner
from testCase import public



if  __name__=="__main__":
    test_report = "D:\\Project\\newIpSiteserver\\report\\"  # 报告存放路径
    now=time.strftime("%Y-%m-%d  %H_%M_%S")
    public.mkdirScreenshot(now)

    from testScript.unitlist import unitlist

    filename=test_report + now + "result.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream = fp, verbosity = 1,
                          title = 'newIpSitServer', description = u'测试报告')

    unitlist=unitlist()
    runner.run(unitlist)
    fp.close()

