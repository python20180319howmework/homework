
'''
定义一个函数，实现字符串的len方法
例如mylen("hello") 得到5
要求不要使用python内置的len()
提示字符串的终止条件是""空串
'''


def yjklen(mystr):
	n = 0
	for i in mystr:
		if i != "":
			n+=1
		else:
			break
	return n

mystr = str(input("请输入一个字符串："))
print("'{}'有 {} 个子字符串".format(mystr,yjklen(mystr)))

