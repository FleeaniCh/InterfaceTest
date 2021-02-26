# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author: Renkai

# import reflect
# reflect.login()

"""
    反射
"""
# # 通过import导入目标模块并且放在一个对象中
# f = __import__('reflect')
# # 通过对象找reflect模块中index的字符串并且调用
# f.index()
# f.info()

import reflect

# # 调用reflect模块中的logout函数
# f = getattr(reflect,'logout')
# f()

# # 如何找到Person中的info方法并且调用它
# obj = reflect.Person()
# if hasattr(obj,'inf0'):
#     f = getattr(obj,'info')
#     f()
# else:
#     print("Sorry")

# obj = reflect.Person()
# f = setattr(obj,'exit','this is a exit method')
# f2 = hasattr(obj,'exit')
# print('setattr后的结果：',f2)
# f3 = delattr(obj,'exit')
# f4 = hasattr(obj,'exit')
# print('delattr后的结果：',f4)

# # 在reflect模块中设置变量str2
# f5 = setattr(reflect,'str2','hello world')
# # 判断str2是存在
# f6 = hasattr(reflect,'str2')
# print(f6)

# # 在reflect模块中删除str1
# f7 = hasattr(reflect,'str1')
# print(f7)
# f8 = delattr(reflect,'str1')
# f9 = hasattr(reflect,'str1')
# print(u'删除后的结果：',f9)

# 反射案例（主要用于自动化测试中的关键字驱动）
url = input("请输入路由地址：\n")
target_models,target_function = url.split('/')
m = __import__(target_models)   #  导入模块并放置在对象中
if hasattr(m,target_function):
    target_function = getattr(m,target_function)
    target_function()
else:
    print('Not Found 404 Page')