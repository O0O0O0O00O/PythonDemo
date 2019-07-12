#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/5/30 10:18
# @Author  : Nana Xing
# @File    : decorator_class.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :基于类实现的装饰器

class Test():
    def __call__(self):
        print('call me!')


t = Test()
t()  # 调用call方法


class Logging(object):
    """
    不带参数的类装饰器
    """
    def __init__(self, func):
        self.func = func

    # 重载call方法
    def __call__(self, *args, **kwargs):
        print('[DEBUG]: enter function {func}'.format(func=self.func.__name__))
        return self.func(*args, **kwargs)


class LoggingParam(object):
    """
    带参数的类装饰器
    """
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=self.level, func=func.__name__))

            func(*args, **kwargs)

        return wrapper


@Logging
def say(something):
    print('say {}!'.format(something))


@LoggingParam(level='INFO')
def say_param(something):
    print("say {}!".format(something))


if __name__ == '__main__':
    say('nana')
    say_param('juju')
