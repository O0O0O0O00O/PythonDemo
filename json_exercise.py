#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/17 14:52
# @Author  : Nana Xing
# @Site    : 
# @File    : json_exercise.py
# @Software: PyCharm

import json

class Student(object):
    def __init__(self, name , age, score):
        self.name = name
        self.age = age
        self.score =score

    # def student2dict(self):
    #     return {'name': self.name,
    #             'age': self.age,
    #             'score': self.score}

s = Student('leo', 18, 88)

# s_string = json.dumps(s, default=s.student2dict())
# print(s_string)

print(json.dumps(s, default=lambda obj: obj.__dict__))
