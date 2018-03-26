

#判断从你出生到今年共有多少闰年
year = int (input("请输入您的出生年份"))
i = 0
for n in range(year,2019):
	if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
		i = i + 1
	else:
		pass
print(i)

















