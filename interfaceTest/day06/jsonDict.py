# !/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: kr.r

"""
JSON字典的序列化与反序列化
    序列化：把python的数据类型转换为str类型的过程
    反序列化：str类型转化为python的数据结构（-->>字典）
"""

import json
import requests

dict1 = {"phoneNumber":"17355641830","internationalAreaCode":"+86",
         "rsaPassword":"cwaN5bYpsDQrgUM/S834MsugMIzxD5Rt0PcCQ4EqX96a7eo01vTe75QoZuUACsBQ3gMcTp8ykdevb76sZlVdk+0XdBoOYjSI3KAV2Qir41WdC00t0tES9RthxTEO5+mVf8pGRA3q0t2WRRclT/j3gwgnYCCjY8aodFx1AOLUzAk=",
         "persistenceHint":True,"deviceId":"2eae9456ecdb53ead4b2ffdbee0a14db",
         "publicKey":"MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCROXqyCKxG8DrQKvrmdwiAHFJseaLHKsdzJ+61EpEGUawyLk5obn2Z2lyVVGjqT3KECk3DJtAD6Jux/m/gW2/lxspvhUO1YE1P8OZuUq5xhr/3AWuSSXCqLM2q6TEMnI2VE1BzlsRcxQVGVd4kGszzpyLXYS9ubFTTp1C2A+uZ1QIDAQAB"}

# print(u'dict1类型：',type(dict1))
# json1 = json.dumps(dict1)
# print(u'json1类型：',type(json1),json1)
# dict2 = json.loads(json1)
# print("反序列化：",type(dict2),dict2)

r = requests.post(url='https://www.fxiaoke.com/FHH/EM0HUL/Authorize/PersonalCloudLogin?_fs_token=',
                  json=dict1,
                  headers={"content-type": "application/json"})
print(r.text)