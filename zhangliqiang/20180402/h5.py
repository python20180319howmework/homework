


#5. 使用filter筛选序列中所有回文数,假定序列是[132, 12321, 11, 9989, 666]
def huiwen(strs):

	 
	
	strslist = list(strs)   
	strslist.reverse()  
	newstring = ''.join(strslist)
	if newstring == strs:
		return True
	else:
		return False
	#strs =str [132, 12321, 11, 9989, 666]
f = filter(huiwen,map(str,[x for x in [132,12321,11,9989,666]]))
print(list(f))
	
	  
