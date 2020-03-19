# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 14:25
# @Author  : Mysunshine
# @File    : readExcel.py
# 读取Excel的方法
import os
from testFile import getpathInfo
from xlrd import open_workbook
path = getpathInfo.get_Path()


class readExcel:
    def get_xls(self, xls_name, sheet_name):
        cls = []
        # xlsPath返回值为：'D:\\simpleAPItest\\testFile\\case\\userCase.xlsx'
        xlsPath = os.path.join(path, 'case', xls_name)
        file = open_workbook(xlsPath)
        sheet = file.sheet_by_name(sheet_name)

        # 获取行数
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        # cls返回值是嵌套列表
        return cls


if __name__ == '__main__':
    print(readExcel().get_xls('userCase.xlsx','login'))
    # a = readExcel().get_xls('userCase.xlsx','login')
    # b = tuple(a)
    # print(b)
    # print(readExcel().get_xls('userCase.xlsx','login')[0][1])
    # print(readExcel().get_xls('userCase.xlsx', 'login')[1][2])



