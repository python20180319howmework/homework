y=int(input("please input year:"))
m=int(input("please input month:"))
d=int(input("please input day:"))
flag=0
day=0
if m in range(1,13):
	for i in range(1,m):
		if i in [1,3,5,7,8,10,12]:
			day=day+31
		elif i in [4,6,9,11]:
			day=day+30
		else:
			if y%400==0 or y%100!=0 and y%4==0:
				flag=1
			day=day+28+flag
	day=day+d
	print("这一天是这年的第{}天".format(day))
else:
	print("error!")
