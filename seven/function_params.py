#-*-coding:utf-8-*-
"""函数相关知识"""

#位置参数：*开头的参数，元组
#关键字参数：**开头的参数，字典

#**开头的参数只能作为最后一个参数出现
#*开头的参数只能作为最后一个位置参数出现，但是*开头的参数后能有其他参数出现

#将元信息加在函数参数上
def add(x:int,y:int) -> int:
    return x+y
sum = add(1,2)
print(sum)

'''用函数代替只有单个方法的类'''
from urllib.request import urlopen

class UrlTemplate:
    def __init__(self,template):
        self.template = template
    def open(self,**kwargs):
        return urlopen(self.template.format_map(kwargs))
yahoo = UrlTemplate('http://www.baidu.com?s={name}&f={fields}')
for line in yahoo.open(name='ie',fields='8'):
    print(line.decode('utf-8'))
'''下面用单个方法代替'''
def UrlTemplate(template):
    def open(**kwargs):
        return urlopen(template.format_map(kwargs))
    return open
yahoo = UrlTemplate('http://www.baidu.com?s={name}&f={fields}')
for line in yahoo(name='ie',fields='8'):
    print(line.decode('utf-8'))
