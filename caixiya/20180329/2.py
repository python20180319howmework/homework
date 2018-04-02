'''
定义一个函数:
   1)判断输入的字符串是否是回文字符串 （例如："上海自来水来自海上"为回文字符串）
'''
def ishuiwen(stra):
	for i in range(len(stra)):
		if stra[i]==stra[-1-i]:
			return "是回文字符串"
		else:
			return "不是回文字符串"

if __name__=="__main__":
	stra=input("请输入一个字符串：")
	print("{}结果{}".format(stra,ishuiwen(stra)))
