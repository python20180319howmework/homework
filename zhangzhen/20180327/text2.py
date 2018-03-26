

#判断从你出生到今年共有多少的闰年
num = 0
for i in range(1994,2019):
	if (i % 4 == 0 and i % 100 != 0 )or i % 400 == 0:
		num = num + 1
	else:
		continue;
print(num)






