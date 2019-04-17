#-*-coding:utf-8-*-
"""classmethod方法和staticmethod方法的区别"""
class Date(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def string_to_date(cls,string_date):
        """返回类对象的类方法"""
        day,month,year = map(int,string_date.split('-'))
        #day, month, year = map(int, "2017-2-3".split('-'))
        date1 = cls(day,month,year)
        return date1

class Sub(Date):
    century = 0
    def __init__(self,century=0):
        #assert isinstance(century, object)
        self.century = century
