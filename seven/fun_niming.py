#-*-coding:utf-8-*-
"""匿名函数"""
#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

print(list(map(lambda x:x*x,[1,2,3,4])))#f(x)=x*x,[1, 4, 9, 16]
