'''
定义一个函数:
   1)判断输入的字符串是否是回文字符串 （例如："上海自来水来自海上"为回文字符串）
'''
def str1(s):
	'''
	l=[]
	for i in s:
		l.append(i)
	print(l)
	
	a=tuple(l)
	print(a)
	'''
	l=list(s)
	l.reverse()
	newstr="".join(l)
	print(newstr)
	if s == newstr:
		print("{}是回文字符串".format(s))
	else:
		print("{}不是回文字符串".format(s))
if __name__=="__main__":
	s=input("please input string:")
	str1(s)
