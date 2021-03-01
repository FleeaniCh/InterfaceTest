# !/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: kr.r

"""
    open()函数的参数：
        1、要操作的文件名称
        2、以什么样的方式操作文件
"""

# w -->> 写文件
import json

f = open('file.json','w')
temp = {
    "name":'wuya',
    "age":18,
    "address":"Hefei"
}
f.write(json.dumps(temp))
f.close()
#
# # a -->> 追加
# f = open('file.json','a')
# f.write('wuya')
# f.close()

# f = open('file1','w')
# f.write('wuya')
# f.close()

# r -->> 读文件
'''
read([n])--> 默认读取文件的所有内容
readlines() --> 按行读取并组成列表
for循环按行读取
'''
# f = open('file1',encoding='utf-8')
# data = f.read()
# data = f.readlines()
# print(data)
# for i in f: # 按行读取
#     print(i)

#  文件上下文的处理
with open('file2','w') as f:
    f.write('wuya')

