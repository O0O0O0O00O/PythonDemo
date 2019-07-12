#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/5/13 20:09
# @Author  : Nana Xing
# @File    : function_test.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :
from demo_list import fact


if __name__=='__main__':
    print('当前执行文件名：' + __name__)
    print("阶乘：", fact(3))