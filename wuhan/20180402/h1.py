import os
fd=open("h.py")
l=[]
l2=[]
a=("The Zen of Python")
b=("Tim Peters")
l1=("姓名：","黄永鹏 ","时间："," 20180331")
def mywrite(myfile,l):
	with open(myfile,"w") as fd1:
		fd1.writelines(l)
if os.path.exists("./小练习/")!=True:
	os.mkdir("./小练习/")
def mowei(myfile,l1):
	with open(myfile,"a+") as fd2:
		fd2.writelines(l1)

def biaoti(myfile,a):
	with open(myfile,"r+") as fd3:
		t=fd3.readlines()
		fd3.seek(0)
		fd3.writelines(a)
		fd3.writelines("\n")
		fd3.writelines(t)

def zuozhe(myfile,b):
	with open(myfile,"r+") as fd4:
		fd4.seek(17)
		k=fd4.readlines()
		fd4.seek(0)
		l2.append(fd4.readline())
		l2.append(b)

		str5=" ".join(l2)
		fd4.seek(0)
		fd4.writelines(str5)
		fd4.writelines("\n")
		fd4.writelines(k)

for line in fd.readlines():
	if len(line)>2:
		l.append(line)
		str1='\n'.join(l)
	else:
		pass
filemy="./小练习/"+"Blowing in the wind"+".txt"
mywrite(filemy,str1)
biaoti(filemy,a)
zuozhe(filemy,b)
mowei(filemy,l1)
print(a)
print(b)
print(str1)
str2="".join(l1)
print(str2)
fd.close()

