class Fish(object):
	def __init__(self,name,color,size):
		self.__name=name
		self.__color=color
		self.__size=size
	def pri_fish(self):
		print("{}是{}的，大小为{}.".format(self.__name,self.__color,self.__size))
	def setname(self,newname):
		self.__name=newname
	def setcolor(self,newcolor):
		self.__color=newcolor
	def setsize(self,newsize):
		self.__size=newsize
f1=Fish("金鱼","金黄色",20)
#print(f1.name,f1.color,f1.size)
f1.pri_fish()
f1.setname("鲤鱼")
f1.setcolor("银色")
f1.setsize(30)
print(f1._Fish__name,f1._Fish__color,f1._Fish__size)
