# !/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: Renkai

"""
    装饰器:
        1. 函数可以当做变量
        2. 函数的参数也可以是函数
        3. 函数是可以嵌套的
        步骤：
            1. 执行getinfo函数的时候，把被装饰的函数当做参数来传递
            2. getinfo函数返回值会重新赋值
            3. 一旦结合了装饰器，调用原函数相当于被拦截
    开放封闭原则：
        1. 封闭：已实现的功能代码尽可能不要修改
        2. 开放：对现有的功能代码可扩展
"""

def f():
    print('hello')
# per = f()
# per

# def login(username, passwd):
#     if username == '无涯' and passwd == 'admin':
#         return 'vcdsvv12ebwjbf232112'
#     else:
#         return '登录账号错误'
#
# def profile(token):
#     if token == 'vcdsvv12ebwjbf232112':
#         return '欢迎访问个人主页'
#     else:
#         return '请登录系统'
# print(profile(login('wuya','admin')))

def f3():
    def f4():
        return 'hello'
    return f4()
# print(f3())


# 装饰器
def getInfo(func):
    """闭包"""
    def wrapper():
        print('Python自动化测试实战')
        func()
    return wrapper

@getInfo
def f5():
    # print('Python自动化测试实战')
    # getInfo()
    print("网易云课堂")

@getInfo
def f6():
    # print('Python自动化测试实战')
    # getInfo()
    print('51CTO的平台')

# f5()

def login_(username,password):
    if username == 'wuya' and password == 'admin':
        return 'sdf2345'
    else:
        return '账号错误'

def login(func):
    def inner(*args,**kwargs):
        # print(args,kwargs)
        if kwargs['token'] == 'sxzda1234':
            return func(kwargs)
        else:
            return '请登录系统'
    return inner

@login
def profile(token):
    """个人主页"""
    return '欢迎访问个人主页'

print(profile(token='sxzda1234'))
