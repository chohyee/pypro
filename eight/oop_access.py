#-*-coding:utf-8 -*-
"""对象属性访问管理"""
class A(object):
    """这个类用来声明Access类中的__private变量的类型"""
    def __init__(self,point):
        self.point = point

class Access(object):
    """在这里可以声明属性类型"""
    __private: A
    name:str
    age:int

    def __init__(self,name,age,private):
        self.name = name
        self.age = age
        self.__private = private #如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）
    def get_private(self):
        """获取私有类"""
        return self.__private
    #TODO 123
    def set_private(self,private):
        """设置私有类"""
        self.__private = private

    # 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
    # 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。


if __name__ == '__main__':
    access = Access('vy',18,'a')
    print(access.get_private())
    access.__private = 'b'
    #双下划线变量一定不能被访问吗？其实不是，对于类Access中的__private属性，只不过python将私有变量解释为了access._Access__private，其中access为实例。
    print(access.get_private()) #这里结果为a，access.__private = 'b'仅给access新增了一个属性而已


#补充
'''
1.以单个下划线开头的变量或方法仅供内部使用
2.一个变量的最合适的名称已经被一个关键字所占用,用单末尾下划线 var_
3.私有
4.可以使用“_”来表示它只是一个临时值
'''