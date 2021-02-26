# !/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: kr.r

"""
    元组的序列化与反序列化
"""
import json

tuple1 = (1, 2, 3)

# 序列化
tuple_str = json.dumps(tuple1)
print(tuple_str, type(tuple_str))  # [1, 2, 3] <class 'str'>

# 反序列化
str_tuple = json.loads(tuple_str)
print(str_tuple, type(str_tuple))  # [1, 2, 3] <class 'list'>
