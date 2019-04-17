#-*-coding:utf-8-*-
"""生成器与迭代器"""
def generator(max):
    a,b,n = 0,1,0
    while n < max:
        a,b = b,a+b
        yield b
        n = n +1
#有yield关键字就不是函数了，而是生成器了，并且执行到yield的时候就返回值
for item in generator(5):
    print(item)