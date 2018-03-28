def isrunnian(y):
	if y%400==0 or y%100!=0 and y%4==0:
		flag=1
def month(m,y):
	if m in range(1,13):
		for i in range(1,m):
			if i in [1,3,5,7,8,10,12]:
				day=day+30
			elif i in [4,6,9,11]:
				day=day+30
			else:
				day=day+28+isrunnian(y)
		return day
	else:
		return 0
def year(y1,y2):
	for i in range(y1,y2):
		day=day+365+isrunnian(i)
if __name__=="__main__":
	y=int(input("year:"))
	m=int(input("month:"))
	d=int(input("day:"))
	flag=0
	day=0
	year(1990,y)
	month(m,y)
	print("day:",day)
