# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 12:05
# @Author  : Mysunshine
# @File    : __init__.py.

import json
import requests

url = 'http://47.100.95.65:9527/auth/loginfront'
datas = {"loginWay": "1", "password": "liz123456", "username": "liz"}
headers = {'Content-Type': 'application/json'}

result = requests.post(url=url, data=json.dumps(datas), headers=headers)
print(result)
# 将输出形式美观好看，json.dumps()是将字典形式的内容转化为json格式
res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
print(res)

