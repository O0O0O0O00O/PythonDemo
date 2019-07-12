#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/5/23 20:47
# @Author  : Nana Xing
# @File    : file_reader.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :

with open('pi_digits.txt') as file_obj:
        file_content = file_obj.read()
        print(file_content.strip())

with open('pi_digits.txt') as file_obj:
    for line in file_obj:
        print(line.strip())

def get_new_version(max_version):
    str_list=max_version.split('.')
    sorted_str_list=sorted(str_list,reverse=True)
    for i in range(len(sorted_str_list)):
        temp=int(sorted_str_list[i])+1
        if temp>=100:
            sorted_str_list[i]=str(0)
        else:
            sorted_str_list[i]=str(temp)
            break

    print(str_list)
    print(sorted_str_list)
    new_version='.'.join(sorted_str_list)
    print(new_version)


get_new_version('99.99.99')