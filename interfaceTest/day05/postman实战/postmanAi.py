# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author: Renkai

import json
import requests

def readJson():
    return json.load(open('one.json','r'))  # 返回python字典

print(readJson()['item'][0]['request'])

def one_get():
    r = requests.request(method='',url='')
    return r.json()
