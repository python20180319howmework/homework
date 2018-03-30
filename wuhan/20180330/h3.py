def mydict(a):
	l = []
	for key in a.keys():
		l.append(key)
	return l


def mydict2(height,*,name,city):
	print("height:",height,"name:",name,"city:",city)
	
	
if __name__ =='__main__':
	a = eval(input("输入键值对:"))
	print(mydict(a))

	mydict2(172,name = "小沈阳",city = "beijing")

