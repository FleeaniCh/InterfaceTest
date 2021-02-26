#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:Renkai

list1 = [1, 99, 23, 45, 100, 0, 678]
# print(dir(list1))
# list1.append(999)
# list1.insert(0,999)
# print(list1)

list2 = list1.copy()
print(list2)

print(list1.count(100))

print(list1.index(100))

# list1.remove(100)
# print(list1)

# ele = list1.pop()
# print(ele)
# print(list1)

# list2 = [2,3,4]
# list1.extend(list2)
# print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)

# 列表的推导式
for i in list1:
    if i > 2:
        print(i, end='、')
print()
print([x + 1 for x in list1])
print([x + 1 for x in list1 if x > 2])

# 元组
tuple1 = (1, 5, 6, ['wuya', '18'], {'name': 'name', 'age': 18})
# print(dir(tuple1))
tuple1[3][0]='admin'
print(tuple1)
tuple1[4]['name']='wuya'
print(tuple1)