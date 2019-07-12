#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/19 10:53
# @Author  : Nana Xing
# @Site    : 
# @File    : thread1.py
# @Software: PyCharm

import time,threading

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000):
        #获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            #释放锁
            lock.release


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread(9))
t1.start()
t2.start()
# t1.join()
# t2.join()
print(balance)