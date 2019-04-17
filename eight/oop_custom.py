#-*-coding:utf-8-*-
"""定制类"""
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000

class Custom(object):
    def __init__(self,name):
        self.name = name
    # ①定制 __str__方法，在打印类的时候调用的方法
    def __str__(self):
        return 'Custom object (name:%s)'%self.name
    # ②定制 __getattr__方法，在调用类的方法或属性时，如果不存在，就会报错，就是这个方法报的错
    def __getattr__(self, attr):
        if attr == 'age':
            return 99
            # 返回函数也是可以的,调用方式要变为实例的函数调用，如c.age()
            #return lambda:99
        raise AttributeError('\'Custom\' object has no attribute \'%s\'' % attr)

# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
# ③ 链式调用
class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path,path))
    def __str__(self):
        return self._path
c = Custom('vyliu')
# ①例
print(c)
# ②例
# print(c.score) #AttributeError: 'Custom' object has no attribute 'score'
# 为了避免上述报错，而动态赋予一个变量，那就要定制__getattr__方法了
print(c.age) # 99
# print(c.age()) # 函数调用

# ③例  这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
print(Chain().service.list) # /service/list
print(Chain('api.cloud.com').service.list) # api.cloud.com/service/list

