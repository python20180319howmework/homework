import os


#在任意位置创建一个目录，如'~/小练习'
if os.path.exists("~/goodboy/小练习") != True:
	os.mkdir("/home/goodboy/小练习")



#在此目录下创建一个文件Blowing in the wind.txt
f = open("/home/goodboy/小练习/"+"Blowing in the wind.txt","x+")



'''
将以下内容写入文件
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.  
    Complex is better than complicated.
    Flat is better than nested.
'''
l = ["Beautiful is better than ugly.\n",
	"Explicit is better than implicit.\n",
    "Simple is better than complex.\n",  
    "Complex is better than complicated.\n",
    "Flat is better than nested.\n"]
f.writelines(l)
f.close()


#在文件头部插入标题“The Zen of Python”
with open("/home/goodboy/小练习/"+"Blowing in the wind.txt","r+")as f:

	content = f.read()
	f.seek(0,0)
	f.write("The Zen of Python\n"+content)




#在标题后插入作者“Tim Peters”
with open("/home/goodboy/小练习/"+"Blowing in the wind.txt","r+")as f:
	c = f.readline()
	t = f.read()
	f.seek(0,0)
	f.write(c+"Tim Peters\n"+t)

	
	



#在文件末尾加上字符串“你的名字和作业时间”
with open("/home/goodboy/小练习/"+"Blowing in the wind.txt","a+")as f:
	f.write("caoxu 2018.4.1")


#在屏幕上打印文件内容
with open("/home/goodboy/小练习/"+"Blowing in the wind.txt","r+")as f:
	f.seek(0, 0)
	while True:
		l = f.readline()
		if (l == ""):
			break
		print(l)
