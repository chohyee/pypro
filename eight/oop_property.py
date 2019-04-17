#-*-coding:utf-8-*-
"""获取对象属性"""
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir('abc'))

#实例属性和类属性
class A(object):
    type = 'normal'
    def __init__(self,name):
        self.name = name

#给实例绑定属性和方法,只对该实例生效
class B(object):
    pass
b = B()
b.name = 'vyliu'
print(b.name)

def b_method(self,age):
    self.age = age

from types import MethodType
b.b_method = MethodType(b_method,b)


#要想动态添加的方法对所有实例生效，就给类添加方法
def B_method(self,color):
    self.color = color
B.B_method = B_method
bb = B()
bb.B_method('red')
print(bb.color)# red
b.B_method('green')
print(b.color)#green

#我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

#@property方法的使用
class Student(object):
    __slots__ = ('name', 'age','_score') # 用tuple定义允许绑定的属性名称

    def __init__(self,score):
        self._score = score
    '''
    def get_score(self):
        return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    '''

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    #@property和@score.setter给score属性添加了读写方法
    
#@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，
# @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
s = Student(99)
#s._score = 9999 #AttributeError: 'Student' object has no attribute '_score'
s.score = 100  #@property使得get和set方法能像使用属性一样使用方法，并且带有检测动作
print(s.score)

