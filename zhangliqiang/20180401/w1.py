


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
def biaoti():
	if os.path.exists("~/zlq/小练习")!=True:
		os.mkdir("/home/zlq/小练习")
	fd1 = open("/home/zlq/小练习/"+"Blowing in the wind.txt","x+")

	l = ["Beautiful is better than ugly.\n",
		"Explicit is better than implicit.\n",
    	"Simple is better than complex.\n",  
    	"Complex is better than complicated.\n",
    	"Flat is better than nested.\n"]
	fd1.writelines(l)
	fd1.close()

	with open("/home/zlq/小练习/"+"Blowing in the wind.txt","r+")as fd1:
		context = fd1.read()
		fd1.seek(0,0)
	
		fd1.write("The Zen of Python\n"+context)
	with open("/home/zlq/小练习/"+"Blowing in the wind.txt","r+")as fd1:
		context = fd1.read()
		fd1.seek(0,0)
	#fd1.write("  The Zen of Python \n "+context)
		fd1.write("Tim Peters\n "+context)


	with open("/home/zlq/小练习/"+"Blowing in the wind.txt","a+")as fd1:
		fd1.write("zlq 2018.4.1")

	with open("/home/zlq/小练习/"+"Blowing in the wind.txt","r+")as fd1:
		fd1.seek(0,0)
		while True:
			l = fd1.readline()
			if (l ==""):
				break
			print(l)
if __name__ =='__main__':
	biaoti()
	






