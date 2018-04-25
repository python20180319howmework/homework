def isleap(year):
	if year%4==0 and year%100!=0 or year%400==0:
		return 1
	else:
		return 0	

def weekday(year,month,day):
	sum=0
	for i in range(1990,year):
		sum=sum+365+isleap(i)
	for i in range(1,month):
		if i in [1,3,5,7,8,10,12]:
			sum+=31
		if i in [4,6,9,11]:
			sum+=30
		if i==2:
			sum=sum+28+isleap(year)
	sum+=day		
	return sum%7

def dayofmonth(year,month):
	if month in [1,3,5,7,8,10,12]:
		monthday=31
	if month in [4,6,9,11]:
		monthday=30
	if month==2:
		monthday=28+isleap(year)

year,month,day=eval(input("输入任意日期（year,month,day）："))
print("{}年{}月{}日是星期{}".format(year,month,day,weekday(year,month,day)))
