#-*-coding:utf-8-*-
"""函数作为返回值 -- 闭包"""
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回   --闭包
def lazy_fun(*args):
    def sum_fun():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum_fun
#上面函数只返回了内部函数的引用，并未执行(不返回求和的结果，而是返回求和的函数)
#请再注意一点，当我们调用lazy_fun()时，每次调用都会返回一个新的函数，即使传入相同的参数(前提是内部函数没有引用任何循环变量，或者后续会发生变化的参数)：
f = lazy_fun(1,2,3,4,5)
print(f())#相当于sum_fun()


