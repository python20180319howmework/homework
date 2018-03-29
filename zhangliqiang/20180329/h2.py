

#2. 定义一个函数:
#1)判断输入的字符串是否是回文字符串 （例如："上海自来水来自海上"为回文字符）

def huiwen(strs):

	 
	
	strslist = list(strs)  
	print ("将入参的字符串转换成list:", strslist)  
	strslist.reverse()  
	print ("将list进行反转:", strslist)  
	newstring = ''.join(strslist)  
	print ("将反转后的list再转换成字符串:", newstring)  
	if newstring == strs:  
		print ("是回文!")  
	else:  
		print ("不是回文!")  
  
for i in ['abc', 'abcdedcba', 111,'上海自来水来自海上']:  
	huiwen(i)  

    














