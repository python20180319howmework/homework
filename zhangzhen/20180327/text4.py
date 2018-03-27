#读入用户输入的一个日期(年，月， 日)，判断这一天是这年的第几天
y =int(input("请输入年份："))
m = int (input("请输入月份："))
d =int(input("请输入日："))
ds= 0 
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
	ms = [31,29,31,30,31,30,31,31,30,31,30,31]   
else:
	ms = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(1,13):
	if i == m:
		for j in range(i-1):
			ds = ds+ms[j]
		print("一共%d 天"%(ds+d))



























