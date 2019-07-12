#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/03 11:38
# @Author  : Nana Xing
# @Site    : 
# @File    : webapp.py
# @Software: PyCharm
from flask import Flask
from flask import request,render_template

app = Flask(__name__)

# 处理主页请求
@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

#
@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

# 处理登录请求，成功跳转到success.htm，错误跳转到from.html
@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password =='123':
        return render_template('success.html', username=username)
    return render_template('form.html', message='wrong username or password', username=username)

if __name__ == '__main__':
    app.run()