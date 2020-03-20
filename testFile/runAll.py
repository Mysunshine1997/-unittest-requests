# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 14:26
# @Author  : Mysunshine
# @File    : runAll.py
# 开始执行接口自动化，项目工程部署完毕后直接运行该文件即可
import sys
sys.path.append(r"D:\simpleAPItest")
import os
from common import HTMLTestRunnerNew as HTMLTestRunner
from testFile import getpathInfo
import unittest
from testFile import readConfig
from common.configEmail import SendMail
# from BeautifulReport import BeautifulReport
# 下面的是定时任务引入的模块
from apscheduler.schedulers.blocking import BlockingScheduler
import pythoncom
# import common.Log
from common import Log


path = getpathInfo.get_Path()
report_path = os.path.join(path, 'result')
# base_dir返回值为D:\\simpleAPItest
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

on_off = readConfig.ReadConfig().get_email('on_off')


# log = common.Log.logger

class AllTest:  # 定义一个类AllTest
    def __init__(self):  # 初始化一些参数和数据
        global resultPath
        # result/report.html
        resultPath = os.path.join(base_dir, "result\\report.html")
        # 配置执行哪些测试文件的配置文件路径
        self.caseListFile = os.path.join(path, "caselist.txt")
        # 真正的测试断言文件路径
        self.caseFile = os.path.join(base_dir, "testCase")
        # 存放在caselist.txt中需要执行的用例
        self.caseList = []

    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        fb = open(self.caseListFile, encoding='utf-8')
        for value in fb.readlines():
            data = str(value)
            # 如果data非空且不以#开头
            if data != '' and not data.startswith("#"):
                # 读取每行数据会将换行转换为\n，去掉每行数据中的\n，caseList内容为test01case.py
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        """
        :return:
        """
        # 通过set_case_list()拿到caselist元素组
        self.set_case_list()
        # 测试用例较多时，使用测试套件unittest.TestSuite
        test_suite = unittest.TestSuite()
        suite_module = []
        # 从caselist元素组中循环取出case
        for case in self.caseList:
            # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            case_name = case.split("/")[-1]
            # 打印出取出来的名称
            print(case_name + ".py")
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            # 将discover存入suite_module元素组
            suite_module.append(discover)
            print('suite_module:' + str(suite_module))
        # 判断suite_module元素组是否存在元素
        if len(suite_module) > 0:
            # 如果存在，循环取出元素组内容，命名为suite
            for suite in suite_module:
                # 从discover中取出test_name，使用addTest添加到测试集
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        # 返回测试集
        return test_suite

    def run(self):
        """
        run test
        :return:
        """
        # 打开result//report.html测试报告文件，如果不存在就创建
        fp = open(resultPath, 'wb')
        try:
            # 调用set_case_suite获取test_suite
            suit = self.set_case_suite()
            print('try')
            print(str(suit))
            if suit is not None:  # 判断test_suite是否为空
                print('if-suit')
                # 调用HTMLTestRunner
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
            # log.info(str(ex))

        finally:
            print("*********TEST END*********")
            # log.info("*********TEST END*********")
            fp.close()
        # 判断邮件发送的开关
        # if on_off == 'on':
            # send_mail.outlook()
        # else:
            # print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")


# pythoncom.CoInitialize()
# scheduler = BlockingScheduler()
# scheduler.add_job(AllTest().run, 'cron', day_of_week='1-5', hour=14, minute=59)
# scheduler.start()

if __name__ == '__main__':
    AllTest().run()
    c_mail = SendMail('2974835299@qq.com', 'jkpunzizckxkdfhg',
                      recv=['3035386062@qq.com'],
                      title='发送邮件20200311',
                      content='测试发送邮件，qq发件，另一个是qq邮箱。20200311',
                      file=r'D:\simpleAPItest\result\report.html',
                      ssl=True,
                      )
    Email = c_mail.send_mail()
    logger = Log.logger
    logger.info('随便打印---！！')
