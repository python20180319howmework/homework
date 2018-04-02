
'''
判断输入的字符串是否是回文字符串 （例如："上海自来水来自海上"为回文字符串）
'''
def huiwen(h):
	k=-1
	for i in range(len(h)//2+1):
		if h[i]==h[len(h)-1-i]:
			k=1
		else:
			k=0
	return k
	if k==1:
		print("是回文")	
	else:
		print("不是回文")
	

if __name__=="__main__":
	a=str(input("请输入一个字符串："))
	print(huiwen(a))
	




