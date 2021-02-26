# !/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: kr.r

"""
JSON列表的序列化与反序列化：
"""
import json

list1 = ['admin','wuya','weike']

# 序列化
list_str = json.dumps(list1)
print(type(list_str),list_str)

# 反序列化
str_list = json.loads(list_str)
print(type(str_list),str_list)