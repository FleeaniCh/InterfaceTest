# !/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: Renkai

"""
    需求：要求注册账户，然后注册的账户登录到系统后，显示登录的昵称
        1. 注册函数
        2. 登录函数
        3. 获取昵称函数
"""
import sys

def register():
    """注册"""
    password, username = userInput()
    temp = username+'|'+password
    with open('login.txt','w') as f:
        f.write(temp)


def userInput():
    """用户输入"""
    username = input("请输入用户名：")
    password = input("请输入密码：")
    return password, username


def login():
    """登录"""
    password, username = userInput()
    with open('login.txt') as f:
        info = f.read()
    info = info.split('|')
    if username == info[0] and password == info[1]:
        return True
    else:
        return False

def getNick(func):
    """获取昵称"""
    with open('login.txt') as f:
        info = f.read()
    info = info.split('|')
    if func:
        print("%s你好，欢迎访问"%info[0])
    else:
        print('请登录')


if __name__ == '__main__':
    while True:
        print("1.注册    2.登录     3.退出\n")
        ipt = input("请输入选项：")
        if ipt == '1':
            register()
        elif ipt == '2':
            getNick(login())
        elif ipt == '3':
            sys.exit('你已退出系统')
        else:
            print("输入有误，请重新输入")