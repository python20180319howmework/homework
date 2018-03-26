
#读入用户输入的一个字符串，判断字符串中有多少个大写字母，多少个数字，多少个小写字母
intCount = 0
smallCount = 0
bigCount = 0
mystr = input("请输入一个字符串：")
for i in mystr:
	if i.isupper():
		bigCount += 1
	elif i.isdigit():
		intCount += 1
	else:
		smallCount += 1
print("大写字母%d个小写字母%d个数字%d个"%(bigCount,smallCount,intCount))
		



