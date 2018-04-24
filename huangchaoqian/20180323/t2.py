def 
def binb(n):
	l=[]
	while n!= 0:
		a=n%2
		b=n//2
		l.append(str(a))
		n=b
	l.reverse()
	l1="".join(int(l))
	return l1
#binb=l.reverse()
def oo(n):
	l=[]
	while n!= 0:
		a=n%8
		b=n//8
		l.append(a)
		n=b
	l.reverse()
	return l
def ox(n):
	l=[]
	while n!= 0:
		a=n%16
		b=n//16
		l.append(a)
		n=b
	l.reverse()
	return l
if __name__=="__main__":
	n=int(input("please input a num:"))
	a=binb(n)
	print(a)
	b=oo(n)
	print(b)
	c=ox(n)
	print(c)
