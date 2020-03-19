# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 14:25
# @Author  : Mysunshine
# @File    : getpathInfo.py
# 获取项目的绝对路径
import os
from common import Log


def get_Path():
    # os.path.realpath(__file__) 获取当前执行脚本的绝对路径
    # os.path.split()按照路径将文件名和路径分开
    path = os.path.split(os.path.realpath(__file__))[0]
    return path


if __name__ == '__main__':
    print('ok', get_Path())
    logger = Log.logger
    logger.info('随便打印---！！')



