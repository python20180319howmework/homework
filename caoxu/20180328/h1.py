'''定义一个函数，实现字符串的len方法
例如mylen("hello") 得到5
要求不要使用python内置的len()'''


def mylen(l):
	cnt = 0
	for i in l:
		cnt+=1
	return cnt


if __name__ == "__main__":
	h=input("输入一个字符串:")
	print("{}的长度为{}".format(h,mylen(h)))
