#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/24 16:37
# @Author  : Nana Xing
# @Site    : 
# @File    : gui_demo.py
# @Software: PyCharm
from tkinter import *
import tkinter.messagebox as messagebox
win = Tk()
# 设置窗口大小300*300和位置（120,100）
win.geometry('300x300+120+100')
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self, text='Hello',command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo("Message",'Hello,%s' % name)

# 实例化
app = Application()
# 设置窗口标题
app.master.title('Hello world GUI')
# 主消息循环
app.mainloop()