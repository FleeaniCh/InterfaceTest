#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: Renkai
"""
    动态参数
"""
# def f1(*args,**kwargs):
#     print(args,kwargs)
#
# f1([1,2,3,])
# f1('a')
# f1(name='wuya')
# f1(dict1={'name':'wuya'})

"""
    需求：
    1. 对请求参数进行ascii码排序
    2. 排序后，对请求参数进行md5的加密
        1) 写一个函数，获取请求参数，对请求参数加密
"""

# def data(**kwargs):
#     return dict(sorted(kwargs.items(), key=lambda item: item[0]))  # 对字典进行排序
#
# dict1 = {'name': 'wuya', 'age': 18, 'address': 'xian', 'work': 'tester'}
# print(data(**dict1))

'''
返回值:
    1. None
    2. 
'''

def f():
    print('Hello world')
# print(f())

def add(a,b):
    return a+b
# print(add(2,3))

def login():
    username = input("请输入登录账号：\n")
    passwd = input("请输入登录密码：\n")
    if username == 'wuya' and passwd == 'admin':
        return 'vsdchavjchdvajhvj'
    else:
        return False

def profile(session):
    if session == login():
        print("欢迎您访问无涯的个人主页")
    else:
        print("你未登录系统，3s后跳转至登录页面，错误码: 302")

profile('vsdchavjchdvajhvj')