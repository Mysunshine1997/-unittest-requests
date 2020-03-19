# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 14:25
# @Author  : Mysunshine
# @File    : geturlParams.py
# 获取接口的URL，参数，method等
from testFile import readConfig
readconfig = readConfig.ReadConfig()


class geturlParams:
    def get_Url(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':9527' + '/auth/loginfront'
        return new_url


if __name__ == '__main__':
    print(geturlParams().get_Url())
