'''读入用户输入的一个字符串，判断字符串中有多少个大写字母，多少个数字，多少个小写字母
提示：
    判断一个字符串是否是数字：isdigit()  例如"1".isdigit()为True
    得到单个字符串对应的值 ord("A") == 65'''
count=0
count2=0
count3=0
str1=input("输入一个字符串:")
for i in range(len(str1)):
	if str1[i].isdigit():
		count+=1
	if 65<=ord(str1[i])<=90:
		count2+=1
	if 97<=ord(str1[i])<=122:
		count3+=1
print("大写字母有%d个"%(count2))
print("小写字母有%d个"%(count3))
print("数字有%d个"%(count))
