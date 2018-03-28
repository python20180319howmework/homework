#用户任意输入他的生日，判断他输入00后，90后，还是80后
y=input('birthyear:')
a=y[2:4]
b=y[0:2]
if 19<=int(b)<20:
	if 80<=int(a)<90:
		print("该用户是80后！")
	elif 90<=int(a)<100:
		print("该用户是90后！")
elif int(b)>=20:
	print("该用户是00后！")

#总结整型、浮点、字符串、列表、元祖、字典、集合的常用方法，且比较各自擅长的领域
'''
列表常用方法：append，insert，pop，remove，extend，index
字符串常用方法：split，len
元祖常用方法：
'''
