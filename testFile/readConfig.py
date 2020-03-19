# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 14:25
# @Author  : Mysunshine
# @File    : readConfig.py
# 读取配置文件的方法，并返回文件中内容
import os
import configparser
from testFile import getpathInfo


path = getpathInfo.get_Path()
config_path = os.path.join(path, 'config.ini')
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')


class ReadConfig:

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    # 写好，留着以后用
    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':
    print('baseurl:', ReadConfig().get_http('baseurl'))
    print('on_off:', ReadConfig().get_email('on_off'))
