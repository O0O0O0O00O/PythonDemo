#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/04 14:08
# @Author  : Nana Xing
# @Site    : 
# @File    : Student.py
# @Software: PyCharm

class Student(object):

# 以双下划线开头的变量名为私有变量
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age

    def ptint_student(self):
        print("name,age: ", self.__name, self.__age)

stu = Student("guangyi", 16)
stu.ptint_student()
