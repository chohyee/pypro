#!/usr/bin/python
'''
构造eip_barad中db数据的工具
'''
import pymysql
import threading
from DBUtils.PooledDB import PooledDB

HOST = '10.x.x.x'
PORT = 3306
USER = 'xxx'
PASSWD = 'xxx'
DB = 'xxx'

class CDbPool(object):
    @staticmethod
    def instance():
        global inst
        try:
            inst
        except Exception as e:
            inst = CDbPool()
        return inst
    
    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=6,
            mincached=2,
            maxcached=5,
            maxshared=3,
            blocking=True,
            maxusage=None,
            setsession=[],
            ping=0,
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWD,
            database=DB,
            charset='utf8'
        )
    
    def conn(self):
        return self.pool.connection()
'''
1.execute(query,args=None),执行一条SQL语句，返回受影响的行数。若args是列表，用%s做占位符，若是字典，用%(name)s
'''
class CDbClient(object):
    def __init__(self):
        self._conn = CDbPool.instance().conn()
        self._cur = self._conn.cursor()
    
    def __query(self, sql, param=None):
        if param is None:
            count = self._cur.execute(sql)
        else:
            count = self._cur.execute(sql, param)
        return count    
    
    def begin(self):
        '''开启事务控制'''
        self._conn.autocommit(0)

    def end(self, option='commit'):
        '''结束事务控制'''
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def commit(self):
        '''手动提交'''
        self._conn.commit()
    def insert_data(self,sql,param):
        return self.__query(sql, param)
        
    def update_data(self,sql):
        pass
         
if __name__ == '__main__':
    import time
    c = CDbClient()
    sql = "insert into `t_barad_0` (`eip`,`region`,`name`,`value`,`flag`,`time`) values (%s,%s,%s,%s,%s,%s)"
    anycast_ip = '182.254.250.121'
    anycast_zone_b = ['bj','gz','hk','in','jp','kr','sg','sh','th']
    while True:
        now_time = time.time()
        flag = now_time%10
        if flag == 0:
            for region in anycast_zone_b:
                c.insert_data(sql,(anycast_ip,region,'inpkg',8192,1,now_time))
                c.insert_data(sql,(anycast_ip,region,'intraffic',8192,1,now_time))
                c.insert_data(sql,(anycast_ip,region,'outpkg',8192,1,now_time))
                c.insert_data(sql,(anycast_ip,region,'outtraffic',8192,1,now_time))
                c.end()
