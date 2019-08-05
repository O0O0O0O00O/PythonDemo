#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/8/5 17:40
# @Author  : Nana Xing
# @File    : dict_demo.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :

temp={'a':1,'b':2,'d':3}

def fun1():
    print('******fun1*******')
    for key in temp:
        print('key: %s, value: %s'%(key,temp[key]))

def fun2():
    print('******fun2*******')
    for key in temp.keys():
        print('key: %s, value: %s' % (key, temp[key]))

def fun3():
    print('******fun3*******')
    for value in temp.values():
        print('value:%s'%value)

def fun4():
    print('******fun4*******')
    for kv in temp.items():
        print(kv)

def fun5():
    print('******fun5*******')
    for k,v in temp.items():
        print('key: %s, value: %s' % (k, temp[k]))


fun1()
fun2()
fun3()
fun4()
fun5()