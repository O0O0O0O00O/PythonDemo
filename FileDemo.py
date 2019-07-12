#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/16 16:49
# @Author  : Nana Xing
# @Site    : 
# @File    : FileDemo.py
# @Software: PyCharm

import os
#创建文件夹
def createDir(folder_name):
    """
    创建文件
    :param folder_name: 文件路径
    :return: 返回创建好的文件路径
    """
    if folder_name.strip:
        folder = os.getcwd()[:-4] + folder_name + '\\'
        if not os.path.exists(folder):
            os.makedirs(folder)
    return folder;

def write_text(content,directory):
    file = directory + "file1.txt"
    with open(file, 'w', encoding='utf-8') as new_file:
        new_file.write(content)


def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        str = file.read()
        print(str)

directory = createDir('test')
str = '哈哈哈leo\n\thehehe'
write_text(str, directory)
path = directory + "\\file1.txt"
read_text(path)