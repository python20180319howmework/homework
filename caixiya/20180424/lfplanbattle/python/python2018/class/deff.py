def power(x,y=2):
	res=1
	while y>0:
		res*=x
		y-=1
	return res
if __name__=="__main__":
	print(power(5))
	print(power(5,4))

def mysum(*number):
	res=0
	for i in number:
		res+=i
	return res

if __name__=="__main__":
	print(mysum(1,2))
	print(mysum(1,2,3))
	l=[3,4,5,6]
	print(mysum(l[0],l[1],l[2],l[3]))
	print(mysum(*l))

def powsum(*num):
	res=0
	for i in num:
		res+=pow(i,2)
	return res

if __name__=="__main__":
	print(powsum(1,2,3))
	l=[1,2,3]
	print(powsum(*l)
def func(name,age=10,*arg,city,height,**kw):
	print(name,age)
	for i in arg:
		print(i,end="")
	print(city,height,kw)

if __name__=="__main__":
	func()
	print("小菜")
	print("你是最棒的"，"加油噢")
	print(city="河北",height=163,weight=45,like="美食")
