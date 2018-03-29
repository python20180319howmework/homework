"""
1.定义一个函数，实现字符串的len方法
例如mylen("hello") 得到5
要求不要使用python内置的len()
提示字符串的终止条件是""空串
"""
# 定义一个函数　ｄｅｆ　
def mylen(newstr):
	j = 0
	for i in newstr: # 遍历字符串
		j += 1
	return j

newstr = input("请输入字符串：")
a = mylen(newstr)
print("字符串的长度是{}".format(a))

