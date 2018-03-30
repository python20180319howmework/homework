"""
2. 定义一个函数:
   1)判断输入的字符串是否是回文字符串 （例如："上海自来水来自海上"为回文字符串
"""
def hstr(s):
	a = len(s)
	i = 0
	count = 1    
	while i <= (a/2):
		if s[i] == s[a-i-1]:
			count = 1
			i += 1
		else:
			count = 0
			break
	return count			

if __name__ == "__main__":
	a = input("请输入字符串a:")
	s1 = hstr(a)
	if s1 == 1:
		print("{}是回文字符串".format(a))
	else:
		print("{}不是回文字符串".format(a))

