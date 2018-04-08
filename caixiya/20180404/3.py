'''
3. 根据字典的特性模拟一个通讯录,完成一下功能,用户根据输入的数选择功能
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
import sys
import os
import pickle
from enum import Enum,unique

class Person(object):
	def __init__(self,name,tel):
		self._name=name
		self._tel=tel
	def showInfo(self):
		print("name:{},tel:{}".format(self._name,self._tel))
	def setname(self,name):
		self._name=name
	def settel(self,name):
		self._tel=tel
		
class PhoneBook(object):
	def __init__(self):
		if len(sys.argv)<2:
			print("you should mark you phonebook")
			sys.exit(1)
		else:
			try:
				if os.path.exists(sys.argv[1])==True:
					with open(sys.argv[1],"rb") as f:
						self.pbdic=pickle.load(f)
				else:
					self.pbdic={}
					#print("this is a bug")
			except EOFError:
				self.pbdic={}
	def addPerson(self,name,person):
		for key in self.pbdic.keys():
			if key==name:
				print("此联系人已存在")
				return
		self.pbdic[name]=person
		print("联系人:{}已经成功添加到您的电话本".format(name))
 
	def deletePerson(self,name):		
		for key in self.pbdic.keys():
			if key==name:
				self.pbdic.pop(key)
				print("{}已删除".format(key))
				return
			else:
				print("电话本中没有你要删除的联系人")
	def updatenamePerson(self,name,newname):
		if name==newname:
			#print("联系人姓名并未修改")
			#return
			raise ValueError("你传错啦")
		for key in self.pbdic.keys():
			if key==name:
				self.pbdic[key].setname(newname)
				key=newname
				return
		else:
			print("您要修改的联系人不存在")

	def updatetelPerson(self,name,newtel):
		for key in self.pbdic.keys():		
			if key==name:
				self.pbdic[key].settel(newtel)
				return
		else:
			print("你要修改的联系人不存在")
	
	def findPerson(self,name):
		for key in self.pbdic.keys():
			if key==name:
				print("找到了您要找的联系人：")
				self.pbdic[key].showInfo()
				return
		else:
			print("查无此人")
	def showPerson(self):
		for v in self.pbdic.values():
			v.showInfo()
	def quitBook(self):
		with open(sys.argv[1],"wb") as f:
			pickle.dump(self.pbdic,f)

	def showMenu(self):
		print('''
			********欢迎使用电话本系统********
			1.增加联系人
			2.删除联系人
			3.修改联系人信息
			4.查找联系人
			5.显示所有联系人
			9.退出通讯录,并将所有联系人写入文件,''')

@unique
class Menu(Enum):
	ADD=1
	DELETE=2
	UPDATE=3
	FIND=4
	SHOW=5
	QUIT=9
@unique
class Update(Enum):
	UPDATENAME=1
	UPDATETEL=2

if __name__=="__main__":
	myphone=PhoneBook()
	while True:
		myphone.showMenu()
		choose=input("请输入你的选择：")
		choose=int(choose)
		if choose==Menu.ADD.value:
			name=input("请输入你要添加的联系人姓名")
			tel=input("请输入新联系人的电话号码：")
			p=Person(name,tel)
			myphone.addPerson(name,p)
		elif choose==Menu.DELETE.value:
			name=input("你要删除的用户是：")
			myphone.deletePerson(name)
		elif choose==Menu.UPDATE.value:
			print("1.修改联系人姓名 2.修改联系人电话")
			c=int(input())
			name=input("请输入你要修改的联系人姓名：")
			if c==Update.UPDATENAME.value:
				try:
					newname=input("请输入修改后的名字：")
					myphone.updatenamePerson(name,newname)
				except ValueError:
					print("你输入的姓名不正确")
			elif c== Update.UPDATETEL.value:
				newtel = input("请输入此联系人的新号码:")
				myphone.updatetelPerson(name, newtel)
			else:
				print("操作错误")	
		elif choose == Menu.FIND.value:
			name = input("输入你要查找的姓名:")
			myphone.findPerson(name)
		elif choose == Menu.SHOW.value:
			myphone.showPerson()
		elif choose == Menu.QUIT.value:
			myphone.quitBook()
			print("***************感谢使用此电话本管理系统***********************")
			break
'''
p1=Person("xiya","123456")
p2=Person("zhangzhen","456123")
pb=PhoneBook()
pb.addPerson("xiya",p1)
pb.addPerson("zhangzhen",p2)
pb.showPerson()														
pb.quitBook()
pb.deletePerson("xiya")
pb.showPerson()
pb.updatenamePerson("zhangzhen","zhangliqiang")
pb.showPerson()
'''
