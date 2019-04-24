#-*-coding:utf-8-*-
import sys
import os

#打印文件默认编码格式
print('Default coding is: %s'%sys.getdefaultencoding())

'''-------with 的好处，当程序离开with语句后，将自动关闭文件--------'''
'''-------\n会被当做默认的换行符，如果需要特别指定，open中用newline=''来指定-------'''
#以读模式打开文件
with open('1.txt','rt',encoding='utf-8') as fr:
    data = fr.read()

#以写模式打开文件
with open('1.txt','wt',encoding='utf-8') as fw:
    fw.write('write some text')

#以追加模式打开文件
with open('1.txt','at',encoding='utf-8') as fa:
    fa.write('\napend some text')


'''------读写二进制文件-------'''
with open('iperf','rb') as frb:
    data = frb.read(16)
    text = data.decode('utf-8')
    print(text)
with open('iperf','wb') as fwb:
    sometext = 'hello world'
    fwb.write(sometext.encode('utf-8'))


'''-------对不存在的文件进行操作,防止覆盖，文件存在是，下面这段会报错-------'''
if not os.path.exists('notexist.txt'):
    with open('notexist.txt','xt',encoding='utf-8') as fx:
        fx.write('some text and file not eixst!')



'''------将二进制文件中的数据读取到可变缓冲区，这些缓冲区有array、bytearray、numpy等模块创建的数组-------'''
def read_byte_file_into_buffer(filename):
    buff = bytearray(os.path.getsize(filename))#获取文件大小
    with open(filename,'rb') as f:
        f.readinto(buff)
    return buff

buff = read_byte_file_into_buffer('1.txt')



'''------对二进制文件做内存映射--------'''
'''------可随机对文件进行操作--------'''
import mmap
def memory_map(filename,access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename,os.O_RDWR)
    return mmap.mmap(fd,size,access=access)#内存对象，<class 'mmap.mmap'>
with open('b.txt','wb') as f:
    f.write(b'Hello world')
    
m = memory_map('b.txt')
print(type(m),len(m),m[0:])

'''------处理路径名------'''
path = '/data/demo/daily/pyshell/src/readme.doc'
#Get the last component of the path
print(os.path.basename(path))
#Get the dir name
print(os.path.dirname(path))
#Join path component together
print(os.path.join('tmp','data',os.path.basename(path)))


'''-----序列化python对象，将python对象转化为字节流，这样就能将其保存在文件中，存储到数据库中或者通过网络进行传输-----'''

