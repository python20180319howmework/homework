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
import time
def func():
	if os.path.exists("./小练习")!=True:
		os.mkdir("./小练习")
	f=open("./小练习/"+"Blowing in the wind.txt","w+")
	f.write("Beautiful is better than ugly.\n")
	f.write("Explicit is better than implicit.\n")
	f.write("Simple is better than complex.\n")
	f.write("Complex is better than complicated.\n")
	f.write("Flat is better than nested.\n")
	f.close()

	with open("./小练习/"+"Blowing in the wind.txt","r+")as f:
		context = f.read()
		f.seek(0,0)
		f.write("The Zen of Python\n"+context)
	
	with open("./小练习/"+"Blowing in the wind.txt","r+")as f:
		c=f.readline()
		context = f.read()
		f.seek(0,0)
		f.write(c+"Tim Peters\n "+context)


	with open("./小练习/"+"Blowing in the wind.txt","a+")as f:
		f.write("caixiya"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))

	with open("./小练习/"+"Blowing in the wind.txt","r+")as f:
		while True:
			l = f.readline()
			if (l ==""):
				break
				print(l)
if __name__=="__main__":
	func()
