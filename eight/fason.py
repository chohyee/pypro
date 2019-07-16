#-*-coding:utf-8-*-
class Pa(object):
    def __init__(self,value):
        self.value = value
    def a(self):
        print("Pa:a方法")
        self.b()
    def b(self):
        return None
class Fa(Pa):
    def __init__(self,value):
        super().__init__(value)
    def b(self):
        print("Fa:b方法")

class So(Fa):
    pass


def progress():
    s = So(12)
    s.a()

    

if __name__ == '__main__':
    progress()

'''
So没有自己的__init__方法，因此是一层层使用父类的
s.a()，s没有a()方法，依次取父类的,会取到Pa类中的a()方法，Pa中的a方法调了b()方法，虽然
Pa中有b()方法，但是首先是会去调So中的b方法，无奈没有，因此会找到Fa中的b方法，所以这个py文件
运行的结果是：

    Pa:a方法
    Fa:b方法

'''
