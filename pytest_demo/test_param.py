#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/8/26 16:53
# @Author  : Nana Xing
# @File    : test_param.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :
from datetime import datetime, timedelta

import pytest

testdata = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1))
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected



@pytest.mark.parametrize('x', [0, 1])
@pytest.mark.parametrize('y', [2, 3])
def test_foo(x, y):
    print('测试组合:x->%s,y->%s' % (x, y))
    pass


if __name__ == '__main__':
    pytest.main()
