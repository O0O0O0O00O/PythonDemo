#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/10 19:37
# @Author  : Nana Xing
# @Site    : 
# @File    : Screen.py
# @Software: PyCharm


class Screen(object):
    # __slots__ = ("width", "height", "area")

    def __init__(self, width, height):
        self.width = width
        self.height = height


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise ValueError("宽度必须是整数或者浮点数")
        if value < 0:
            raise ValueError("宽度必须大于等于0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise ValueError("长度必须是整数或者浮点数")
        if value < 0:
            raise ValueError("长度必须大于等于0")
        self._height = value

    @property
    def area(self):
        self._area = self._width * self._height
        return self._area

s = Screen(2,2)

s.width = 10
s.height = 20.0
print("宽度，长度，面积：", s.width, s.height, s.area)