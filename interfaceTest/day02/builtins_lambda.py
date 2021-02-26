# !/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: Renkai

"""
    内部函数-01：lambda函数
        1. 形式参数
        2. 表达式
"""

per = lambda a, b: a + b
# print(per(2, 3))

login = lambda username, passwd: print('登录成功') if username \
                                                  == '无涯' and passwd == 'admin' else print('登录失败')
# login('无涯','admin')

list1 = [1, 2, 3, 4, 5]


def f():
    list2 = []
    for i in list1:
        i += 100
        list2.append(i)
    return list2


# print(f())

def f3(a):
    return a + 100


# print(list(map(f3,list1)))
# print(list(map(lambda a:a+100,list1)))

def f4():
    list2 = []
    for i in list1:
        if i > 2:
            list2.append(i)
    return list2


print(list(filter(lambda a: a > 1, list1)))
