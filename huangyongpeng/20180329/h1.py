

from math import *
'''
1.定义一个函数，实现字符串的len方法
例如mylen("hello") 得到5
要求不要使用python内置的len()
'''
def zifu(a):
	count=0
	for i in a:
		count+=1 
	
	print(count)

if __name__=='__main__':

	a=str(input("请输入字符串："))
	zifu(a)
