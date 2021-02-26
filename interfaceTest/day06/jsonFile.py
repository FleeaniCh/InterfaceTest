# !/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: kr.r

"""
    文件的序列化与反序列化
"""
import json

import requests

r = requests.get(url='http://www.weather.com.cn/data/sk/101190408.html')
print(r.content.decode('utf-8'))
print(type(r.content.decode('utf-8')))
# 对文件进行序列化--》就是把服务端数据写到文件中
# json.dump(r.content.decode('utf-8'),open('weather.json','w'))

# 对文件的反序列化：读取文件的内容
dict1 = json.load(open('weather.json')) # 读取json信息-->> str
print(type(dict1))  # <class 'str'>
dict2 = json.loads(dict1)   # 反序列化
print(type(dict2))  # class 'dict'>
print(dict2)
