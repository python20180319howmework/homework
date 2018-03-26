#2
num = 0

for year in range(1995,2019):
	if year%4 == 0 and year%100 !=0 or year%400 == 0:
		num+=1
		print("{}年是闰年".format(year))
print("我从出生到现在一共有{}个闰年".format(num))






