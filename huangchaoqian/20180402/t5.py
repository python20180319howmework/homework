#使用filter筛选序列中所有回文数,假定序列是[132, 12321, 11, 9989, 666]

def huiwen(s):
	l=list(s)
	l.reverse()
	newstr="".join(l)
	if s==newstr:
		return 1
	else:
		return 0
s=[132,12321,11,9989,666]
f=filter(huiwen,[str(x) for x in s])

print(list(f))



