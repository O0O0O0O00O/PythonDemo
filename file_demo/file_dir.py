#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/4 17:07
# @Author  : Nana Xing
# @File    : file_dir.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :os.path的常用方法
import os

print('脚本的绝对路径：'+os.path.abspath(__file__))
print('path（__file__）的父路径：'+os.path.dirname(__file__))
print('脚本文件名：'+os.path.basename(__file__))

print('是否是绝对路径：')
print(os.path.isabs(__file__))

print('是否是存在的目录：')
print(os.path.isdir(__file__))

print('是否是存在的文件：')
print(os.path.isfile(__file__))

print('路径分割, 将路径分割为目录和文件名：')
print(os.path.split(__file__))
path_list=os.path.split(__file__)
for path in path_list:
    print(path)


print('分割文件名和文件后缀：')
print(os.path.splitext(__file__))

print('将目录和文件名组合在一起：')
print(os.path.join('c:\code','test.py'))

print('获取文件大小（字节）')
print(os.path.getsize(__file__))