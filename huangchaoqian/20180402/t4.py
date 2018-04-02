#利用reduce实现列表中元素求积

from functools import reduce
#l=[1,2,3,4,5,6]
def myreduce(l):
	r=reduce(lambda x,y:x * y,l)
	print(r)
l=eval(input("please input list:"))
myreduce(l)
