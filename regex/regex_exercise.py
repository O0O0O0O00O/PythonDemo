#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/23 19:07
# @Author  : Nana Xing
# @Site    : 
# @File    : regex_exercise.py
# @Software: PyCharm

import re,unittest

def is_valid_email(addr):
    if re.match(r'^([a-zA-Z]+)@(gmail|microsoft)(.com)$',addr):
        print('OK')
    else:
        print('NO')

# is_valid_email('someone@gmail.com')
# 测试:
assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
print('ok')