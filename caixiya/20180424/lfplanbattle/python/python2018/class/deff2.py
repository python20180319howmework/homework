def func(name,age=10,*arg,city,height,**kw):
	print(name,age)
	for i in arg:
		print(i,end=" ")
	print("")
	print(city,height,kw)

if __name__=="__main__":
	func("小菜","你是最棒的","加油噢",city="河北",height=163,weight=45,like="美食")
