#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author: Renkai

"""
    作用域：
        1. 全局作用域：全局变量
        2. 局部作用域：针对局部
"""
# name = '无涯'
def f():
    global name
    name='无涯课堂'
    print(name)

# f() # 无涯课堂 ——就近原则

def f1():
    name = '我是父函数的值'
    def f2():
        # name = '我是子函数的值'
        print(name)
    return f2()

f1()