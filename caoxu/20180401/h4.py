'''
每一个要求封装成小函数
'''


import os


#创建目录
def my_path(l):
	if os.path.exists(l) != True:
		os.mkdir(l)


#创建文件
def my_open(l,n):
	f = open(l+n,"x+")
	f.close()


#写入内容
def my_write(l,n,cont):
	with open(l+n,"r+")as f:
		f.writelines(cont)


#追加标题
def my_write2(l,n,cont2):
	with open(l+n,"r+")as f:
		content = f.read()
		f.seek(0,0)
		f.write(cont2+content)


#追加作者
def my_write3(l,n,cont3):
	with open(l+n,"r+")as f:
		c = f.readline()
		t = f.read()
		f.seek(0,0)
		f.write(c+cont3+t)


#尾部追加读者
def my_write4(l,n,name):
	with open(l+n,"a+")as f:
		f.write(name)


#打印文件内容
def my_print(l,n):
	with open(l+n,"r+")as f:
		f.seek(0,0)
		while True:
			w = f.readline()
			if (w == ""):
				break
			print(w)


if __name__ =="__main__":
	

	#参数
	l = "/home/goodboy/小练习"
	l1 = "/home/goodboy/小练习/"
	n = "Blowing in the wind.txt"
	cont = ["Beautiful is better than ugly.\n",
    		"Explicit is better than implicit.\n",
    		"Simple is better than complex.\n",  
    		"Complex is better than complicated.\n",
    		"Flat is better than nested.\n"]
	cont2 = "The Zen of Python\n"
	cont3 = "Tim Peters\n"
	name = "caoxu 2018.4.1"
	

	#调用函数
	my_path(l)
	my_open(l1,n)
	my_write(l1,n,cont)
	my_write2(l1,n,cont2)
	my_write3(l1,n,cont3)
	my_write4(l1,n,name)
	my_print(l1,n)
		
	
