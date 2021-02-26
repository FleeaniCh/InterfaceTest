#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:Renkai

# for i in range(1,10):
#     print(i,end='  ')

# while True:
#     p = int(input('1.姓名 2.年龄'))
#     if p == 1:
#         name = input('你的名字是什么？\n')
#     elif p == 2:
#         age = input('你的年龄\n')
#     else:
#         break

# age = 19
# print('success') if age>20 else print('fail')

str1 = 'admin'
# print(dir(str1))
str2 = str1.replace('admin', 'administrator')
print(str1)
print(str2)

print(str1.find('m'))

print(str1.startswith('a'))
print(str1.endswith('n'))

print(str1.isdigit())

print(str1.upper())

# 应用较为广泛
str3 = '你好，无涯'
print(str3.split('，'))
print('。'.join(str3.split('，')))

name = 'wuya'
age = 18
print("我的名字是%s，今年%s岁"%(name,age))
print("我的名字是{0}，今年{1}岁".format(name,age))
print("我的名字是{name}，今年{age}岁".format(name=name,age=age))