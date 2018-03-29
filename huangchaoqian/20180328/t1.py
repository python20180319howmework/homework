'''
定义一个函数，实现字符串的len方法
例如mylen("hello") 得到5
要求不要使用python内置的len()
'''
def mylen():
	s=input('please input string:')
	count=0
	for i in s:
		count+=1
	return count
print(mylen())
#a=mylen()
#print(a)
