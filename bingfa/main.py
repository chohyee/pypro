#!/usr/bin/python3
#-*-coding:utf-8-*-
import os
from util import MyThread
import logging

LOG_FORMAT = "%(asctime)s - [%(processName)s][%(thread)s][%(thread)d] - %(pathname)s - %(funcName)s - %(message)s"
logging.basicConfig(level=logging.DEBUG,filename='/tmp/uwsgi.log',format=LOG_FORMAT)

def shell():    
    ret = os.popen('nslookup python.org')
    #注意readlines()只能获取一次，因此需要先将其值保存
    result = ret.readlines()
    logging.debug(result)
    return result
def ping():
    ret = os.popen('ping www.baidu.com -c 1')
    result = ret.readlines()
    logging.debug(result)
    return result
def run():
    #t = MyThread(shell)
    tt = MyThread(ping)
    #t.start()
    tt.start()
    #t.join()
    tt.join()
    logging.debug(tt.get_result())
    return tt.get_result()
if __name__ == '__main__':
    run()
