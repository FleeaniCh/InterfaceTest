# !/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: kr.r
"""
    1、对字典按ASCII进行排序
    2、进行url编码
    3、进行md5加密
"""
# import hashlib
# from urllib import parse

# dict1 = {'name':'wuya','age':18,'city':'Hefei','work':'tester'}
#
# dict1 = dict(sorted(dict1.items(),key=lambda item:item[0]))
# print(dict1)
#
# datas = parse.urlencode(dict1)
# print(datas)
#
# hash = hashlib.md5()
# hash.update(datas.encode('utf-8'))
# print(hash.hexdigest()) #3cc6702d37d32cdc7c31f9bf4429898e


import hashlib
from urllib import parse


def getMd5(**kwargs):
    """对字典进行加密"""
    sort_ = dict(sorted(kwargs.items(), key=lambda item: item[0]))
    datas = parse.urlencode(sort_)
    hash = hashlib.md5()
    hash.update(datas.encode('utf-8'))
    return hash.hexdigest()


print(getMd5(name='wuya', age=18))
