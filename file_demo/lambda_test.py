#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/5/31 10:31
# @Author  : Nana Xing
# @File    : lambda_test.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :  lambda匿名函数语法：lambda parameters:express
# lambda函数 ，是指一类无需定义标识符（函数名）的函数或子程序。
# lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值

def sum(x,y):
    return x+y

p=lambda x,y:x+y

print(sum(2,3))
print(p(2,3))
