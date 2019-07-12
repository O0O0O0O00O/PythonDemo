#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/24 18:39
# @Author  : Nana Xing
# @Site    : 
# @File    : douban_get1.py
# @Software: PyCharm
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:', data.decode('utf-8'))