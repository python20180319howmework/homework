#5. 使用filter筛选序列中所有回文数,假定序列是[132, 12321, 11, 9989, 666]



def ishuiwen(x):
	l1 = str(x)
	for i in range(len(l1)) :
		if l1[i]!=l1[len(l1)-i-1]:
			return False
	return True
		
	


l =[132,12321,11,9989,666]
f = filter(ishuiwen,l)
print(list(f))






