"""
2、判断从你出生到今年共有多少的闰年 
"""
year = int(input("请输入你的出生年份："))
num = 0
for i in range(year,2019):
	if (i%100 != 0 and i%4==0) or i%400 == 0:
		num += 1
	#else:
		#continue
else:
	print("共有{}个闰年".format(num))
