#用户任意输入他的生日，判断他输入00后，90后，还是80后
year = int(input("请输入出生年份:"))
month = int(input("请输入出生月份:"))
day = int(input("请输入出生天:"))

if year >= 2000:
	print("你是00后")
elif year < 2000 and year >= 1990:
	print("你是90后")
elif year < 1990 and year >= 1980:
	print("你是80后")
else:
	print("你out了!!")
