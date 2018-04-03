#2. 定义一个函数:
#   1)判断输入的字符串是否是回文字符串 （例如："上海自来水来自海上"为回文字符串）

def str1(str2):
	l = []
	for i in str2:
		l.append(i)
	count = 1
	b = len(str2)
	for a in range(b):
		if l[a] == str2[a]:
			count = 1
	return count
if __name__ == "__main__":
	s = input("请输入一个字符串用于判断是不是回文字符串")

	if str1(s) == 1:
		print("您输入的是回文字符串".format(s))
	else:
		print("您输入的不是回文字符串".format(s))































