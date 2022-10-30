# -*- codeing = utf-8 -*-
# @Time : 2022/10/25 18:06
# @Author : zhangwei
# @File : demo1.py
# @Software : PyCharm
from flask import Flask,current_app,redirect,abort,render_template
from flask import request
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/html')
def hello():
    return render_template('index.html')


if __name__ == '__main__':

    pass