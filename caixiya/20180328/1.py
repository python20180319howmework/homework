'''
定义一个函数，实现字符串的len方法
例如mylen("hello") 得到5
要求不要使用python内置的len()
提示字符串的终止条件是""空串
'''
def mylen(stra):
	count=0
	for i in stra:
		count+=1
	return count
stra=input("请输入一个字符串：")
print("'{}'字符串的len为{}".format(stra,mylen(stra)))
