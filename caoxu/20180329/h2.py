'''
定义一个函数:
   1)判断输入的字符串是否是回文字符串 （例如："上海自来水来自海上"为回文字符串）
'''


def mystr(s):
	flag = 0
	for i in range(len(s)):
		if s[i] != s[len(s)-i-1] :
			flag = 1
	return flag


if __name__ =='__main__':
	s = input("输入一个字符串:")
	if mystr(s) == 0:
		print("{}是回文字符串".format(s))
	else:
		print("{}不是回文字符串".format(s))
