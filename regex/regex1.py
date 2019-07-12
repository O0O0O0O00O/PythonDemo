#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/23 17:25
# @Author  : Nana Xing
# @Site    : 
# @File    : regex1.py
# @Software: PyCharm

import re

def matchPhone():

    s = 'a'
    while s != '$':
        test = input("请输入要匹配的电话号码：")
        if re.match(r'^\d{3}\-\d{3,8}$', test):
            print("匹配")
        else:
            print("不匹配")
        s = input("结束请输入$，继续请输入任意键：")

if __name__ == '__main__':
    matchPhone()