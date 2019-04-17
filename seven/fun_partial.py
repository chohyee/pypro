#-*-coding:utf-8-*-
"""偏函数"""

#偏函数，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点
print(type(int('123456')))#默认以十进制转换字符串为int类型,但有时候需要2进制的转换,就需要写成下面这样的
print(type(int('123456',base=8))),print(int('123456',base=8))#<class 'int'> 42798

#但有时候需要一个base=2的默认int函数，可以自定义如下，将base默认固定为2：
def int2(x,base=2):
    return int(x,base)
print(int2('10001'))
#其实functools提供了工具--偏函数
import functools
int2 = functools.partial(int, base=2)
print(int2('10010'))#结果为18
