#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:Renkai

dict1 = {'name':'wuya','age':18}
dict2 = {'address':'xian'}

# dict2 = dict1.copy()
# print(dict2)
# print(dict1.get('age'))
#
# for key in dict1.keys():
#     print(key)
#
# for value in dict1.values():
#     print(value)
#
# for key,value in dict1.items():
#     print(key,":",value)
dict1.update(dict2)
print(dict1)

dict3 = {'name': 'wuya', 'age': 18, 'address': 'xian'}
print(sorted(dict1.items(),key=lambda item:item[0]))