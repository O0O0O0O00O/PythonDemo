#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/8/26 16:43
# @Author  : Nana Xing
# @File    : test_demo.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :
import pytest


class TestClass:
    def test_one(self):
        print('one')
        x='this'
        assert 'h' in x

    def test_two(self):
        print('two')
        x='hello'
        assert hasattr(x,'check')


if __name__=='__main__':
    pytest.main(['-q','--html=a.html'])