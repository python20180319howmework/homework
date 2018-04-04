'''
1.定义一个函数，实现字符串的len方法
例如mylen("hello") 得到5
要求不要使用python内置的len()
提示字符串的终止条件是""空串
'''


# 定义一个函数
def num (mystr):
	count = 0
	for i in mystr:
		#print(i)
		count += 1
	return count
mystr = input("请输入一个字符串：")
print(num(mystr))

#判断空串不要用空字符串""去比较  



