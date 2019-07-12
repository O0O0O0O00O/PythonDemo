#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/2/27 19:35
# @Author  : Nana Xing
# @File    : testTemplate.py
# @ProjectName: PythonDemo
# @Software: PyCharm
import os
#region 创建文件夹
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
    return folder
#endregion

def write_text(content,directory):
    file = directory + "file1.txt"
    with open(file, 'w', encoding='utf-8') as new_file:
        new_file.write(content)


def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        str = file.read()
        print(str)