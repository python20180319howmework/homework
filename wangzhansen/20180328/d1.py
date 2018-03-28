'''
1.定义一个函数，实现字符串的len方法
例如mylen("hello") 得到5
要求不要使用python内置的len()
提示字符串的终止条件是""空串
'''

'''
i = 0
while stu[i] != stu[-1]:
		i += 1
print(i+1)

'''

def mylen(stu):
	l = 0
	for i in stu:
		l += 1
	z = l
	print(z)

sts = input("请输入一段字符串:")
z = mylen(sts)
	















