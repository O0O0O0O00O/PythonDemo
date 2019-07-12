#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/10 20:45
# @Author  : Nana Xing
# @Site    : 
# @File    : test.py
# @Software: PyCharm

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学生类
"""
class Student(object):

#@property装饰器就是负责把一个方法变成属性调用
    @property
    def score(self):
        """
        返回学生分数getter
        :return:
        """
        return self._score

    @score.setter
    def score(self, value):
        """
        setter方法，设置学生分数
        :param value: 分数值
        :return:
        """
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
