#!/usr/bin/python3
#-*-coding:utf-8-*-
"""工具类"""
import threading

class MyThread(threading.Thread):
    """重新定义带返回值的线程类,重写父类run方法"""
    def __init__(self,func,args=()):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args
    def run(self):
        self.result = self.func(*self.args)
    def get_result(self):
        try:
            return self.result
        except Exception:
            return None
class A:...