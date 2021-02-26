# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author: Renkai

"""
    1. 实现用户登录功能
    2. 实现查看影虎信息
    3. 实现用户注册功能
"""
import sys

def userInput():
    """用户输入"""
    username = input("请输入用户名：")
    password = input("请输入密码：")
    return username, password

def register(username,password):
    """注册"""
    temp = username+'|'+password
    with open('login.txt','w') as f:    # 覆盖写入
        f.write(temp)
        f.write('\n')   # 写入文件需要手动换行

def login(username,password):
    """登录"""
    f = open('login.txt')
    for line in f:  # 按行获取文件数据
        info = line.split('|')
        # print(info[0],info[1])
        if username == info[0] and password == info[1]:
            return True
    else:
        return False

def info(username,password):
    """获取昵称"""
    r = login(username,password)
    if r:
        print("%s你好，欢迎访问"%username)
    else:
        print('sorry，请重新登录')

def main():
    """主函数"""
    while True:
        print("1.注册    2.登录     3.退出\n")
        ipt = input("请输入选项：")
        if ipt == '1':
            username,password = userInput()
            register(username,password)
        elif ipt == '2':
            username, password = userInput()
            info(username,password)
        elif ipt == '3':
            sys.exit('你已退出系统')
        else:
            print("输入有误，请重新输入")

main()