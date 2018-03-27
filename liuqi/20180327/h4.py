"""
4.读入用户输入的一个日期(年，月， 日)，判断这一天是这年的第几天
"""
year =int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日子:"))
mysum = day
days = [31,28,31,30,31,30,31,31,30,31,30,31]
i=0
if 0 < month <13 and 0 <= day <= 31:
	if (year%100!=0 and year%4==0) or year%400==0:
		days[1] = 29
	while i < month -1:
		mysum = mysum + days[i]
		i += 1
	print("这一天是{}年的第{}天".format(year,mysum))
else:
	print("输入错误！")  
