#读入用户输入的一个日期(年，月， 日)，判断这一天是这年的第几天
year=int(input("请输入年份:"))
month=int(input("请输入月份:"))
day=int(input("请输入天:"))
flag=False
if (year%4==0 and year%100!=0)or year%400==0:
	flag=True
count=0
a=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if month==1:
	print("这一天是这年的第%d天"%(day))
	break
elif  month==2:
	print("这一天是这年的第%d天"%(day+31))
	break
else:	
	while 3<i<month-1:
		count+=a[i]
		i+=1
	if flag:
		count+=1

print("这一天是这年的第%d天"%(count+day))

	
