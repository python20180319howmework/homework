
'''
根据字典的特性模拟一个通讯录,完成一下功能,用户根据输入的数选择功能
   1) 1.查找电话号码
   2) 2.增加联系人
   3) 3.删除联系人
   4) 4.修改联系人的电话号码
   5) 5.退出通讯录,并将所有联系人写入文件,要求写入文件后的格式为
         例如:
                王占森   123455556
                刘淇  222222333335
        尝试使用面向对象编程
'''
import os
if os.path.exists("./信息保存/")!=True:
	os.mkdir("./信息保存/")
class Txl(object):
	def __init__(self,m):
		self.__mm=m
	def	cx(self):
		for key in dic.keys():
			if self.__mm==key:
				print( dic[self.__mm])	 
	def zj(self,xm,hm):
		self.__xm=xm
		self.__hm=hm
		dic[self.__xm]=self.__hm 
	def sc(self,k):
		self.__k=k
		dic.pop(self.__k)
	def xg(self,m,n):
		self.__m=m
		self.__n=n
		dic[self.__m]=self.n
	def tc(self):
		for item in dic.items():
			l1.append(item)
		with open(l,'w+') as f:
			f.writelines(str(l1))
dic={"01":123456,"02":234567,"03":345678,"04":456789}	
l="./信息保存/"+"txl.txt"
l1=[]

while(1):
	a=input("请您输入所需要的服务代号：")
	if a==("1"):
		b=input("请输入您想查找的姓名：")
		t=Txl(b)
		print(t.cx())
		t.tc()
	elif a==("2"):
		b=input("请输入您想增加联系人姓名：")
		c=input("请输入您增加的号码：")
		t=Txl(b)
		t.zj(b,c)
		t.tc()
		print("您已经成功添加了联系人！！！")
	elif a==("3"):
		b=input("请输入您想删除的姓名：")
		t=Txl(b)
		t.sc(b)
		t.tc()
		print("{}联系人已经成功删除！！！".format(b))
	elif a==("4"):
		b=input("请输入您想修改信息的姓名：")
		c=input("请输入您修改后的号码：")
		t=Txl(b)
		t.xg(b,c)
		t.tc()
		print("您已经成功的修改了信息！！")	
	elif a==("5"):
		print("系统即将退出，并为您保存！！！")	
		break


#e=Xuanze(2)
#x.panduan()
#t=Txl("03")
#t.cx()
#t.zj('05',336699)
#t.sc('02')
#t.xg('01',999999)
#t.tc()
