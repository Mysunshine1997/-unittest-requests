# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 13:34
# @Author  : Mysunshine
# @File    : configHttp.py
# 这个文件主要来通过get，post，put，delete等方法来进行http请求，并拿到请求响应
import requests
import json


class RunMain:
    def send_post(self, url, data, headers):
        # headers是字典的形式
        # 将data进行json编码，result结果为字典格式
        # json()的作用是输出所有的返回信息，如果没有.json()那么仅返回状态码
        result = requests.post(url=url, data=json.dumps(data), headers=headers).json()
        # 将输出的json美观好看；此处的result为字典格式，输出的res为json格式即为str
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        result = requests.get(url=url, params=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None, headers=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data, headers)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print('method值错误')
        return result


if __name__ == '__main__':
    # 以下是类的实例化，验证是否能正常使用定义的方法
    url = 'http://47.100.95.65:9527/auth/loginfront'
    datas = {"loginWay": "1", "password": "liz123456", "username": "liz"}
    headers = {'Content-Type': 'application/json'}
    result1 = RunMain().run_main('post', url, datas, headers)
    print(result1)
    ss = json.loads(result1)
    print(ss['code'])
