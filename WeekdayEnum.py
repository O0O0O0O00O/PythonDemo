#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/12 17:43
# @Author  : Nana Xing
# @Site    : 
# @File    : WeekdayEnum.py
# @Software: PyCharm

from enum import Enum, unique


@unique
class Weekday(Enum):
    SUN = 0
    MONDAY = 1
    TUESDAY = 2
    WENDAY = 3
    FRU = 4
    FRIDAY = 5
    SAT = 6


for name,member in Weekday.__members__.items():
    print(name, "->", member)