#!/usr/bin/python3
#-*-coding:utf-8-*-
import threading

# 创建全局ThreadLocal对象,作用是为每个线程创建共享变量(在多线程环境下，每个线程都有自己的数据):
local_school = threading.local()
print(local_school)
def process_student():
    # 获取当前线程关联的student:
    print('Hello, %s (in %s)' % (local_school.student, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name#从args中获取的
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()