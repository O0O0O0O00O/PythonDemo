#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/5/29 11:12
# @Author  : Nana Xing
# @File    : test_decorator_fun.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :

def debug(func):
    # 装饰器
    def wrapper(*args,**kwargs):# 指定宇宙无敌参数
        print('[DEBUG]: enter {}()'.format(func.__name__))
        return func(*args,**kwargs)
    return wrapper # 返回包装过函数

def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

def html_tags(tag_name):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            print("<{tag}>{content}</{tag}>".format(tag=tag_name, content=content))
            # return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@debug
def say_hello(something):
    print('hello {}!'.format(something))


@debug
def say_goodbye():
    print('goodbye')


@logging(level='INFO')
def do(something):
    print("do {}...".format(something))



@html_tags('b')
def get_hello(name='Toby'):
    return 'Hello {}!'.format(name)



if __name__=='__main__':
    # 不用@的写法如下
    # say_hello=debug(say_hello)
    # say_goodbye=debug(say_goodbye)
    say_hello(something='hhh')
    say_goodbye()
    do('my work')

    # 装饰器有参数
    # 不用@的写法如下
    # get_hello = html_tags('b')(get_hello)
    # html_tag('b') 是一个闭包，它接受一个函数，并返回一个函数
    # hello = html_tags('b')(hello)

    # get_hello()
    # t_hello('nana')