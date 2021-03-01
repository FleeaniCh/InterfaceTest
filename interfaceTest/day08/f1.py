# !/usr/bin/env python
# -*-coding:utf-8 -*-

# Author: kr.r

"""
    类：有一系列方法和属性组成
"""

class F1(object):
    pass

'''
# 对象的创建--->就是类实例化的过程
三个特性：
1、对象的句柄，区分不同对象
2、属性
    公有属性
        类属性：它属于类，也属于对象，建议使用类调用
        实例属性：仅属于对象
        局部变量：仅函数内部可用
    私有属性
3、方法
'''

# f1 = F1()
# f2 = F1()
# print(id(f1))
# print(id(f2))

'''
class Person(object):
    # 类属性
    common = u"Earth"

    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def info(self):
        return '姓名：%s，年龄：%d，来自于：%s' % (self.name, self.age, self.common)

per = Person('wuay', 18)
# print(per.name)
# print(per.age)
per2 = Person('李四', 22)
per2.setName('lisi')
per2.setAge(27)
print(per2.info())
'''

'''
class Person(object):
    def __init__(self, *args,**kwargs):
        self.args = args
        self.kwargs = kwargs

    def info(self):
        print('信息：', self.args, self.kwargs.values())
        # print(type(self.kwargs.values()))   # <class 'dict_values'>

# per1 = Person(name='wuya')
# per1.info()
#
# per2 = Person(name='wuya',age=18)
# per2.info()
#
# per3 = Person(name='wuya',age=18,isMarry='marry')
# per3.info()

per4 = Person('name',18,'Xian')
per4.info()
'''

'''
一个类存在默认构造函数（写或不写）
构造函数
1、初始化属性
'''
# class Person(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# per = Person()


'''
类中方法的执行顺序：
对象实例化-->>构造函数-->>对象调用方法-->>最后执行析构函数
'''
# 析构函数
# class Person(object):
#     def __init__(self):
#         print('我是构造方法')
#
#     # 最后执行析构方法
#     def __del__(self):
#         print('我是析构方法')

#     def info(self):
#         print('我是方法')
#
# per = Person()
# per.info()

'''
普通方法
'''
# class Person(object):
#
#     def conn(self,user,passwd,host,port):
#         pass
#
#     def f1(self,*args,**kwargs):    # 动态参数
#         pass
#
#     def info(self):
#         print('这是普通方法')
#
# per = Person()
# per.conn('root','root','localhost',3306)
# per.f1()


'''
特性方法：这个方法不能有形式参数
'''
# class Person(object):
#
#     @property
#     def getUserID(self):
#         pass
#
# per = Person()
# per.getUserID

'''
静态方法：直接使用类名进行调用
对象也可以调用静态方法，一般不建议这样做
'''
# class MySQL(object):
#     @staticmethod
#     def conn(user,passwd,host,port,database):
#         pass
#
# mq = MySQL.conn('root', 'root', '127.0.0.1', 3306, 'db_stu')

'''
类方法：直接使用类来进行调用，属于类
'''
# class Person(object):
#     @classmethod
#     def conn(cls):
#         pass

'''
属于类：
    类属性
    静态方法
    类方法
属于对象：
    实例属性
    普通方法
    特性方法
'''

'''
继承：重用已经存在的数据和行为，减少代码的重复编写
子类继承父类所有的实例变量和方法
'''
'''1、类属性的继承'''
# class Person(object):
#     china = '地球'
#
#
# class UsaPerson(Person):
#     pass
#
# usa = UsaPerson()
# print(usa.china)

'''2、实例属性的继承
2.1子类由于业务的需求，需要继承父类的属性'''
class Fruit(object):
    def __init__(self,name):
        self.name = name
#
# class Apple(Fruit):
#     def __init__(self,name,brand,color):
#         super().__init__(name)
#         self.brand = brand
#         self.color = color
#
#     def info(self):
#         print('名称{0}，品牌{1}，颜色{2}'.format(self.name,self.brand,self.color))
#
#
# apple = Apple('苹果','红富士','red')
# apple.info()

'''2.2子类由于业务的需求，不需要继承父类的属性'''
class Apple(Fruit):
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def info(self):
        print('品牌：{0}，颜色：{1}'.format(self.brand,self.color))


apple = Apple('红富士','red')
apple.info()




