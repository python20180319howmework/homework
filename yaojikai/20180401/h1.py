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

#创建目录
def mulu(mulu):
	if os.path.exists(mulu) != True:
		os.mkdir(mulu)

#创建文件
def wenjian(mulu,name):
	f = open(mulu+name,"x+")
	f.close()

#写入内容
def xieru(mulu,name,cont):
	with open(mulu+name,"r+")as f:
		f.writelines(neirong)

#追加标题
def biaoti(mulu,name,cont2):
	with open(mulu+name,"r+")as f:
		content = f.read()
		f.seek(0,0)
		f.write(tianjia+content)

#追加作者
def zuozhe(mulu,name,cont3):
	with open(mulu+name,"r+")as f:
		c = f.readline()
		t = f.read()
		f.seek(0,0)
		f.write(c+tianjia1+t)

#尾部追加读者
def duzhe(mulu,name,name1):
	with open(mulu+name,"a+")as f:
		f.write(name)

#打印文件内容
def dayin(mulu,name):
	with open(mulu+name,"r+")as f:
		f.seek(0,0)
		while True:
			w = f.readline()
			if (w == ""):
				break
			print(w)

if __name__ == "__main__":
	#参数
	mulu = "/home/huahua/小练习/"
	lujing = "/home/huahua/小练习/"
	name = "Blowing in the wind.txt"
	neirong = ["Beautiful is better than ugly.\n","Explicit is better than implicit.\n","Simple is better than complex.\n","Complex is better than complicated.\n","Flat is better than nested.\n"]
	tianjia = "The Zen of Python\n"
	tianjia1 = "Tim Peters\n"
	name1 = "yaojikai 2018.4.1"
	#调用函数
	mulu(mulu)
	wenjian(lujing,name)
	xieru(lujing,name,neirong)
	biaoti(lujing,name,tianjia)
	zuozhe(lujing,name,tianjia1)
	duzhe(lujing,name,name1)
	dayin(lujing,name)
		




