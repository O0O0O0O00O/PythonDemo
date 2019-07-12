#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/19 19:50
# @Author  : Nana Xing
# @Site    : 
# @File    : task_worker.py
# @Software: PyCharm
#任务进程

import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

#从网上获取Queue
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器，即是运行task_manager.py
server_addr = '127.0.0.1'
print('连接到服务器 %s...' % server_addr)
#端口和验证码保持与task_mananger.py
m = QueueManager(address=(server_addr,5000), authkey='abc'.encode('utf-8'))

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print('运行任务 %d *%d' %(n,n))
        r = '%d * %d = %d'%(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('任务队列为空')

print('worker 退出')
