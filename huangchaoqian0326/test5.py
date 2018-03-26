n=input("please input string:")
u=0
l=0
d=0
for i in n:
	if ord('A')<=ord(i)<=ord('Z'):
		u=u+1
	elif ord('a')<=ord(i)<=ord('z'):
		l=l+1
	elif i.isdigit():
		d=d+1
	else:
		pass
print("字符串中有{}个大写字母".format(u))
print("字符串中有{}个小写字母".format(l))
print("字符串中有{}个数字".format(d))
