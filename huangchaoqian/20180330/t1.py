'''
完成一下步骤:
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

def dir():
	if os.path.exists("./小练习")!=True:
		os.mkdir("./小练习")


def fil(filename,context):
	with open(filename,"w") as fd1:
		fd1.writelines(context)

def filere():
	fd=open("./t1.txt")
	l=[]
	for i in fd:
		l.append(i)
	file1="./小练习/"+"Blowing in the wind"+".txt"
	return fil(file1,l)


def mytitle(filename):
	with open(filename,"w") as fd2:
		fd2.writeline("The Zen of Python")

def zuozhe(filename):
	with open(filename,"w") as fd3:
		fd3.writeline("Tim Peters")

def nametime(filename):
	with open(filename,"w") as fd4:
		fd4.writeline("你的名字和作业时间")


if __name__=="__main__":
	filere()
	print(dir())
	print(mytitle(file1))
	print(zuozhe(file1))	
	print(filere())
	print(nametime(file1))	



