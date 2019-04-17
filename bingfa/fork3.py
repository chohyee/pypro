import os
import time
pid=os.fork() #fork反复拷贝
if  pid==0:
    print("A",os.getpid(),os.getppid())
else:
    time.sleep(2)
    print("B",os.getpid(),os.getppid())

