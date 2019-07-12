#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/24 10:46
# @Author  : Nana Xing
# @Site    : 
# @File    : my_datetime.py
# @Software: PyCharm

from datetime import datetime, timedelta
import time

# 获取系统当前时间
dt = datetime.now()
print('1.当前时间：', dt)
today = dt.date().today()
print('今天：', today)

# datetime转换成timestamp（与时区无关，世界上任何计算机的timestamp都相同）
dt = datetime.now()
s = dt.timestamp()
# 时间戳
t = time.time()
print('2.时间戳：', t, s)
datetime.fromtimestamp(t)
print('3.时间戳转化为datetime：', datetime.fromtimestamp(s))


# 字符串转换成datetime
def str2datetime(str):
    cday = datetime.strptime(str, '%Y/%m/%d %H:%M:%S')
    print('字符串转换成datetime：', cday)
    return cday


# datetime转换成字符串
def datetime2str(dt):
    s = dt.strftime("%Y-%m-%d %H:%M:%S")
    print('datetime转换成str ：', s)
    return s

str2datetime('2018/4/5 12:34:45')
dt = datetime.now()
datetime2str(dt)




if __name__=='__main__':
    # datetime加减
    dt1 = datetime.now()
    tomorrow = dt1 + timedelta(days=1)
    yesterday = dt1 + timedelta(days=-1)
    print('明天：', tomorrow)
    print('昨天：', yesterday)
    temp = tomorrow - yesterday
    print('明天-昨天：', temp)
    last_hour = dt1 + timedelta(hours=-1)
    print('一个小时前：', last_hour)
