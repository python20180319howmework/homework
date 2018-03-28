"""
3.用户任意输入他的生日，判断他输入00后，90后，还是80后
"""
year =int( input("请输入你的生日年份："))
if year > 1900 and year < 2000:
	print("你是９０后")
elif year <= 1900 and year >= 1800:
	print("你是８０后")
elif year >= 2000:
	print("你是００后")
else:
	print("我也不知道你是几零后")
	
