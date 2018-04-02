

'''
使用filter筛选序列中所有回文数,假定序列是[132, 12321, 11, 9989, 666]
'''

def ishuiwen(m):
	
	l1=list(m)
	l2=l1.reverse()
	str2=''.join(l1)
	if str2==m:
		return 1
	else:
		return 0
print(list(filter(ishuiwen,map(str,[x for x in [132,12321,11,9989,666]]))))
	
	
		

