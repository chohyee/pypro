#!/usr/bin/python3
#-*-coding:utf-8-*-
import os
import time

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
    time.sleep(5)#这里为了让父进程晚于子进程结束，假若父进程先结束了，其pid会变成1(俗称僵尸进程)，那么子进程的父pid就为1了，僵尸进程也称为init进程
