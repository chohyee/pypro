#!/usr/bin/python3
#-*-coding:utf-8-*-
'''在回调函数中携带额外的状态'''

#普通回调函数
def apply_async(func,args,*,callback):#*args后面的参数只能为关键字参数(键值对),\单独的*后的参数只能为关键字参数，或者*+参数后的参数只能为关键字参数
    #compute the result
    result = func(*args)

    #Invoke(调用) the callback with the result
    callback(result)
def print_result(result):
    print('Got:',result)
def add(x,y):
    return x+y
apply_async(add,(2,3),callback=print_result)

#带状态的回调函数
class ResultHandler(object):
    def __init__(self):
        self.sequence = 0
    def handler(self,result):
        self.sequence += 1
        print('[{}] Got:{}'.format(self.sequence,result))
r = ResultHandler()
apply_async(add,(2,3),callback=r.handler)
