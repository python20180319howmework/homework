year=int(input("请输入出生年份"))
num=0
for year in range(1993,2019):
	if year%4 == 0 and year%100 !=0 or year%400 == 0:
		num=num+1
print("出生到现在有{}个闰年".format(num))

