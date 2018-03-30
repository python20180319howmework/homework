def my1(base = 3,*arg):
	a = 0
	for i in arg:
		a +=i
		b = a * base
	print(b)

my1(4,1,1,1)
	
