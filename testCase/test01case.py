# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 14:39
# @Author  : Mysunshine
# @File    : test01case.py
# 读取userCase.xlsx中的用例，使用unittest来进行断言校验

import json
import unittest
from common.configHttp import RunMain
import paramunittest
from testFile import geturlParams
import urllib.parse
from testFile import readExcel

url = geturlParams.geturlParams().get_Url()
# login_xls返回值为嵌套列表
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login')
headers = {'Content-Type': 'application/json'}
# @paramunittest.parametrized参数化
@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        """
        set params
        :param case_name:获取表格中case_name
        :param path:获取表格中path
        :param query:获取表格中query
        :param method:获取表格中method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        # query为字典格式
        self.query = json.loads(query)
        self.method = str(method)

    def description(self):
        """desciption
        test report
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        print(self.case_name+"测试开始前准备")

    def test01case(self):
        info = RunMain().run_main(self.method, url, self.query, headers)
        # loads()是将json格式转化为字典格式
        ss = json.loads(info)
        # 断言：判断预期结果和实际结果是否一致
        if self.case_name == 'login':
            self.assertEqual(ss['code'], 500)
        elif self.case_name == 'login_error':
            self.assertEqual(ss['code'], 100)
        elif self.case_name == 'login_null':
            self.assertEqual(ss['code'], 500)
        else:
            print("不存在该用例！！！")

    def tearDown(self):
        print("测试结束，输出log完结")

    # def checkResult(self):
        """
        check test result
        :return:
        """



