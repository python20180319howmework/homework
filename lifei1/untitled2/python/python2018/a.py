l=[1,2,3,"hello","world"]
l2=l[:4]
print(l)
print(l2)
print(l)
l=[x*x for x in range(1,11)]
print(l)
l1=[x*x for x in range(1,11) if x%2==0]
print(l1)

myls=["hello","uplooking",123,345,"python"]
myls1=[i.upper()for i in myls if isinstance(i,str)]
print(myls1)
def fbnq(n):
	if n<=0:
		return -1
	if n==1 or n==2:
		return 1
	return fbnq(n-1)+fbnq(n-2)

def printfbnq(m):
	for i in range(1,m+1):
		#print(fbnq(i))
#printfbnq(8)
		yield fbnq(i)
g=printfbnq(8)
print(g)
	
print(next(g))
for res in g:
	print(res,end=" ")
print("")


from collections import Iterator, Iterable
print("字符串{}可迭代类型".format("是"if isinstance([],Iterable) else "不是"))

print("字符串{}迭代器".format("是"if isinstance([],Iterator) else "不是"))
print(iter("123"))

def func(a,b,f):
	return f(a)+f(b)
print(func(5,-7,abs))
print(func(100,110,str))


str=map(str,[1,2,3,4,5,6])
l=list(str)
print(l)


from functools import reduce
print(reduce(lambda x,y:x*10+y,map(lambda x:ord(x)-ord("0"),"12345")))

#def isspilt(stra):
	
#l=["hello","","1","2","  ","\n"]
#f=filter(isspilt,)
l=["hello","good","study","alice","Peter","Hello"]
print(sorted((map(lambda x:chr(x),str(l)))))
