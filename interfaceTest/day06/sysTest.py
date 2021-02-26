# !/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: kr.r

import sys

# print(sys.argv)  # ['E:/git/GITHUB/interfaceTest/day06/sysTest.py']
#
# # Terminal可中运行：python sysTest.py sleep
# if sys.argv[1] == 'sleep':
#     print('sleep')
# else:
#     print('end')

# print(dir(sys))
# print(sys.version)
# print(sys.platform)

for item in sys.path:
    print(item)
'''
C:\Python\Python37\python.exe E:/git/GITHUB/interfaceTest/day06/sysTest.py
E:\git\GITHUB\interfaceTest\day06
E:\git\GITHUB\interfaceTest
E:\git\GITHUB\interfaceTest\day03_module_package
D:\Program Files\JetBrains\PyCharm 2020.1\plugins\python\helpers\pycharm_display
C:\Python\Python37\python37.zip
C:\Python\Python37\DLLs
C:\Python\Python37\lib
C:\Python\Python37
C:\Python\Python37\lib\site-packages
D:\Program Files\JetBrains\PyCharm 2020.1\plugins\python\helpers\pycharm_matplotlib_backend
'''

'''
    1、标准库：C:\Python\Python37\lib
    2、第三方库：C:\Python\Python37\lib\site-packages
    3、自定义库：
'''
