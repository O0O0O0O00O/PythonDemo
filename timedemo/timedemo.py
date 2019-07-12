#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/5 14:05
# @Author  : Nana Xing
# @File    : timedemo.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :
import datetime

t = 1562293469596
now_dt=datetime.datetime.now()
product_create_time = datetime.datetime.fromtimestamp(t / 1000)
diff = now_dt - product_create_time
s=diff.total_seconds()
h=s/(60*60)
if h >2:
    print('超过两个小时')
print(diff.days)

print(h)