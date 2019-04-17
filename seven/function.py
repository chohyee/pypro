#-*-coding:utf-8-*-
"""接受任意参数的函数"""
import demo
print(demo.Date.day)
print(demo.Date.string_to_date('2017-12-18'))

class A(object):
    @staticmethod
    def echo():
        print('method')