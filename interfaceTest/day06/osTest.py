# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author: Renkai

import os

# 获取当前文件路径
p1 = os.path.abspath(__file__)
print(p1)   # E:\git\GITHUB\interfaceTest\day06\osTest.py

# 获取当前文件所属目录
# p2 = os.path.dirname(p1)
p2 = os.path.dirname(__file__)
print(p2)   # E:\git\GITHUB\interfaceTest\day06

# 获取文件当前目录的上一级目录
p3 = os.path.dirname(os.path.dirname(__file__))
print(p3)   # E:/git/GITHUB/interfaceTest

# 实现目录的拼接
f = open(os.path.join(p3,'day03_module_package/login.txt'))
print(f.read())

# 创建文件夹
# os.mkdir('log')
# 删除文件夹
# os.rmdir('log')

'''
    请求参数是不确定的，可能有一个，可能有N个
'''
def f(*args,**kwargs):
    return kwargs

print(f(name='renkai',age='18'))

print(f(name='renkai',age='18',address='Hefei'))