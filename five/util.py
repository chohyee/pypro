#-*-coding:utf-8-*-
import sys

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
