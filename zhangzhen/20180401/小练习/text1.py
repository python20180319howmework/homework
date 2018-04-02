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
3) 在文件头部插入标题“The Zen of Python”
(4) 在标题后插入作者“Tim Peters”
(5) 在文件末尾加上字符串“你的名字和作业时间”
(6) 在屏幕上打印文件内容
(7) 以上每一个要求封装成小函数
'''
import os

if os.path.exists("/home/zhangzhen/python20180319/homework/0401/小练习") != True:
	os.mkdir("/home/zhangzhen/python20180319/homework/0401/小练习")



def f1(filename,content):
	
#f = open("Blowing in the wind.txt","w+")

#f.write("Beautiful is better than ugly.\n"+"Explicit is better than implicit.\n"+"Simple is better than complex.\n"+"Complex is better than complicated.\n"+"Flat is better than nested.")

	f = open(filename,"w+")
	f.write(content)
	f.seek(0,0)
#print(f.read())
	f.close()

#调用
f1("Blowing in the wind.txt","Beautiful is better than ugly.\n"+"Explicit is better than implicit.\n"+"Simple is better than complex.\n"+"Complex is better than complicated.\n"+"Flat is better than nested.")






def f2(filename,content):
	with open("Blowing in the wind.txt","r+") as f:
		content = f.read()
		f.seek(0,0)
		f.write("The Zen of Python \n"+content)
	'''
	n = f.tell()
	print(n)

	'''
#调用

f2("Blowing in the wind.txt","Beautiful is better than ugly.\n"+"Explicit is better than implicit.\n"+"Simple is better than complex.\n"+"Complex is better than complicated.\n"+"Flat is better than nested.")


def f3(filename,content):
	with open("Blowing in the wind.txt","r+") as f:
		a = f.readline()
		content = f.read()
		f.seek(0,0)
		f.write(a+"Tim Peters\n"+content)

#调用
f3("Blowing in the wind.txt","Beautiful is better than ugly.\n"+"Explicit is better than implicit.\n"+"Simple is better than complex.\n"+"Complex is better than complicated.\n"+"Flat is better than nested.")




def f4(filename,content):
	with open("Blowing in the wind.txt","r+") as f :

		content = f.read()
		f.seek(0,0)
		f.write(content+"张震，20180401\n")
	
#调用
f4("Blowing in the wind.txt","Beautiful is better than ugly.\n"+"Explicit is better than implicit.\n"+"Simple is better than complex.\n"+"Complex is better than complicated.\n"+"Flat is better than nested.")


def f5(filename,content):
	with open("Blowing in the wind.txt","r+") as f:
		content = f.read()
		f.seek(0,0)	
		print(f.read())



#调用
f5("Blowing in the wind.txt","Beautiful is better than ugly.\n"+"Explicit is better than implicit.\n"+"Simple is better than complex.\n"+"Complex is better than complicated.\n"+"Flat is better than nested.")






















