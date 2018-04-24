class Flower(object):
	def __init__(self,name,color,status):
		self.__name=name
		self.__color=color
		self.__status=status
f1=Flower("迎春花","黄色","生机")
f2=Flower("樱花","粉白色","朦胧")
print(f1._Flower__name,f1._Flower__color,f1._Flower__status)
print(f2._Flower__name,f2._Flower__color,f2._Flower__status)
