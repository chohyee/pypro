#!/usr/bin/python3
#-*-coding:utf-8-*-

import threading

class CThread(object):
    '''
    user def thread object
    '''
    def __init__(self):
        self._b_daemon = True
        self._thread = None
    def init(self, arg):
        self._arg = arg
        return 0
    def start(self):
        self._thread = threading.Thread(target = CThread.hook,args=(self,))
        self._thread.setDaemon(self._b_daemon)
        self._thread.start()
    def real_run(self):
        import time
        while True:
            time.sleep(1)
        return 0
    def join(self, timeout=None):
        self._thread.join(timeout)
    def is_alive(self):
        return self._thread.isAlive()
    def is_daemon(self):
        return self._thread.isDaemon()
    def set_daemon(self):
        self._b_daemon = True
    @staticmethod
    def hook(args):
        args.real_run()

if __name__ == '__main__':
    import time
    thread_list = []
    for i in range(1):
        thread = CThread()
        thread.init({})
        thread.start()
        thread_list.append(thread)
    for k in thread_list:
        k.join()
