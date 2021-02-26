# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author: Renkai

import time as t

# 获取当前时间戳
print(int(t.time()))

# 获取当前时间
print(t.localtime())
nowTime = t.strftime('%Y-%m-%d %H:%M:%S',t.localtime())

t.sleep(2)
print(nowTime)

