'''
1. 完成一下步骤:
(1) 在任意位置创建一个目录，如'~/小练习'
(2) 在此目录下创建一个文件Blowing in the wind.txt
     将以下内容写入文件
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.  
    Complex is better than complicated.
    Flat is better than nested.
           
(3) 在文件头部插入标题“The Zen of Python”
(4) 在标题后插入作者“Tim Peters”
(5) 在文件末尾加上字符串“你的名字和作业时间”
(6) 在屏幕上打印文件内容
(7) 以上每一个要求封装成小函数
'''
import os
def write_word():
	f=open('./ls/wind.txt','w+')
	f.write("Beautiful is better than ugly.\n")
	f.write("Explicit is better than implicit.\n")
	f.write("Simple is better than complex.\n")
	f.write("Complex is better than complicated.\n")
	f.write("Flat is better than nested.\n")
	f.close()
def charu():
	with open('./ls/wind.txt','r+')as f:
		context = f.read()
		f.seek(0,0)
		f.write("The Zen of Python\n"+context)
def ch():
	with open('./ls/wind.txt','r+')as f:
		context =f.read()
		f.seek(0,0)
		f.write("Time Peryters\n"+context)
	with open('./ls/wind.txt','a+')as f:
		f.write("lf 2018.4.1")
	with open('./ls/wind.txt','r+')as f:
		f.seek(0,0)
	#	f.readlines()
		print(f.readlines())
write_word()
charu()
ch()
