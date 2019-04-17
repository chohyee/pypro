#-*-coding:utf-8-*-
"""装饰器"""
#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下。

#下面log是一个decorator，不带参数
def log(fun):
    def wrapper(*args,**kwargs):
        print('call%s'%fun.__name__)
        return fun(*args,**kwargs)
    return wrapper

@log
def now():
    print('2017-03-21')
now()#callnow \n 2017-03-21
#调用now()函数，不仅会运行now()函数本身,在now的定义前加上now=log(now)，因此now()=log(now)()=wrapper(),并且wrapper中的fun=now


#下面log2是个decorator，带参数

def log2(text):
    def decorator(fun):
        def wrapper(*args,**kwargs):
            print('%s %s'%(text,fun.__name__))
            return fun(*args,**kwargs)
        return wrapper
    return decorator

@log2('newCall')
def future():
    print('2020-07-13')
future()#newCall future \n 2020-07-13   , future = log('newCall')(future), future()=log('newCall')(future)()=wrapper()=future()

#需要注意的是，被装饰的函数__name__属性改变了，都成为了wrapper，会影响引用被装饰函数__name__属性的函数的判断，可能会出错
#解决办法是在wrapper函数前加上@functools.wraps(func)
print(now.__name__)#wrapper
print(future.__name__)#wrapper

#解决办法
#下面log是一个decorator，不带参数
import functools
def log(fun):
    @functools.wraps(fun)
    def wrapper(*args,**kwargs):
        print('call%s'%fun.__name__)
        return fun(*args,**kwargs)
    return wrapper

@log
def newNow():
    print('new time')
newNow()
print(newNow.__name__)#  newNow,被装饰的函数将会保留自己的函数名称，newNow

#同样对于有参数的被装饰函数也一样
def log2(text):
    def decorator(fun): #s
        @functools.wraps(fun)  #意思就是__name__用呗修饰的函数的
        def wrapper(*args,**kwargs):
            print('%s %s'%(text,fun.__name__))
            return fun(*args,**kwargs)
        return wrapper
    return decorator
@log2('new future')
def future2():
    print('new future')
future2()
print(future2.__name__)#future2

#---------------------------------------------------------
#练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time
def costTime(fun):
    def wrapper(*args,**kwargs):
        a = time.time()
        tmp_fun = fun(*args,**kwargs)
        b = time.time()
        print('cost time: %s'%(b-a))
        return tmp_fun
    return wrapper

@costTime
def fun_sleep():
    time.sleep(3)

fun_sleep()
