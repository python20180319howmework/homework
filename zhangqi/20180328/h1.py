#定义一个函数实现字符串的len 方法
#例如mylen("hello") 得到5
#要求不要使用python内置的len()
#提示字符串的终止条件是""空串

#定义字符串  利用for循环去遍历整个字符串，得到length 然后输出结果
def len1(str1):
	n = 0
	for i in str1:
		n += 1
	print("长度为{}".format(n))
	if n == 0:
		print("是空字符串")
s = str(input("please enter str"))
len1(s)
print(type(s))






















