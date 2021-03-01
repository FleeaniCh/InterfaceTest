# !/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: kr.r

def div(a, b):
    return a / b


'''
1.try代码执行正常，就不会执行except的代码
2.只有try代码执行异常，就会执行except的代码
'''

# try:
#     div(1, 0)
# except KeyError as e:
#     print(e.args)
# except ValueError as e:
#     print(e.args)
# except ZeroDivisionError as e:
#     print(e.args)   # ('division by zero',)
#     print(e)    # division by zero
# except WindowsError as e:
#     print(e.args)
# except Exception as e:
#     print(e.args)


def f(*args, **kwargs):
    return kwargs


try:
    div(1,0)
except Exception as e:
    # print(e.args)   # 异常元组类型
    raise ("执行失败")
else:
    print('pass')
finally:
    print('finally')
