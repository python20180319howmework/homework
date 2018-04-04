'''
5. 使用filter筛选序列中所有回文数,假定序列是[132, 12321, 11, 9989, 666]
'''
def ishuiwen(num):
	l=list(str(num))
	l.reverse()
	newnum=int(''.join(l))
	if newnum==num:
		return num
	else:
		return 0
l=[132,12321,11,9989,666]
f=filter(ishuiwen,[x for x in l])
print(list(f))
