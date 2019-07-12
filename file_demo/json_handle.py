#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/5/31 10:16
# @Author  : Nana Xing
# @File    : json_handle.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :
import json

numbers=[1,2,4,56,6]
# 'numbers.json'
def write_numbers(file_name):
    with open(file_name, 'w') as file_obj:
        # json字符串
        json.dump(numbers, file_obj)


def read_numbers(file_name):
    with open(file_name,'r') as file_obj:
        numbers=json.load(file_obj)
    print(numbers)


if __name__=='__main__':
    file_name='numbers.json'
    read_numbers(file_name)