#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/29 20:55
# @Author  : Nana Xing
# @File    : TestStringMethods.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :
import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('Foo'.upper(),'FOO','测试大写')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper(),'FOO测试')
        self.assertTrue('Foo'.isupper(),'Foo')


if __name__=='__main__':
    unittest.main()