"""
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
"""
# ----------------------------------------------------
import os
def mdir():
	if os.path.exists("./小练习") != True:
		os.mkdir("./小练习")	
# -----------------------------------------------------

def writ():
	f = open("./小练习/blowing in the wind.txt","w+")

	l =[
	"Beautiful is better than ugly.\n",\
	"Explicit is better than implicit.\n",\
	"Simple is better than complex.\n",\
	"Complex is better than complicated.\n",\
	"Flat is better than nested.\n"
		]

	f.writelines(l)
	#f.seek(0,0)
	#print(f.read())
	f.close()
# -----------------------------------------------------

def wrin():
	writ()
	with open("./小练习/blowing in the wind.txt","r+") as f:
		content = f.read()
		f.seek(0,0)
		f.write("-----The Zon of python------        "+content)
	#print(f.tell())
	#print(f.read())
	f.close()
# ----------------------------------------------------

def wtin():
	wrin()
	with open("./小练习/blowing in the wind.txt","r+") as f:
		content = f.read()
		f.seek(25,0)
		f.write("Tim Peters\n") 
	f.close()

# ----------------------------------------------------

def wrint():
	mdir()
	wtin()
	f = open("./小练习/blowing in the wind.txt","a+")
	
	f.seek(0,0)
	f.write("                                 刘琪\n")
	f.write("                               2018.3.31 ")
	f.seek(0,0)
	print(f.read())
	f.close()
# ---------------------------------------------------
wrint()










