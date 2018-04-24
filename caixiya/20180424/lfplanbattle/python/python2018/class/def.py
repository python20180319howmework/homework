def happy1():
   print("祝你生日快乐")
def happy2():
   print("happy birthday to you")
def sing(person):
   happy1()
   happy1()
   happy1()
   happy1()
   happy2()
   happy2()
   print("happy birthday,dear"+person+"@__@")
   happy2()
sing("秋秋")
sing("雅雅")
def sum2num(m,n):
   res=m+n
   return res

def max2num(m,n):
   return m if m>n else n

a,b=eval(input("请输入两个整型数（m,n）"))

res=sum2num(a,b)
print("{}+{}={}".format(a,b,res))
print("{}和{}之间较大的是{}".format(a,b,max2num(a,b)))

def day(year,month):
   if month in (1,3,5,7,8,10,12):
      # print("{}有31天".format(month))
      day=31
   if month in (4,6,9,11):
      #print("{}有30天".format(month))
      day=30
   if month==2:
      if year%4==0 and year%100!=0 or year %400==0:
          day=29
      else:
          day=28
   return day
year,month=eval(input("请输入年月(year,month)："))
print("{}年{}月有{}天".format(year,month,day(year,month)))


def isleap(year):
	if year%4==0 and year%100!=0 or year%400==0:
		return 1
	else:
		return 0	

def weekday(year,month,day):
	sum=0
	for i in range(1990,year):
		sum=365+isleap(i)
	for i in range(1,month):
		if i in [1,3,5,7,8,10,12]:
			sum+=31
		if i in [4,6,9,11]:
			sum+=30
		if i==2:
			sum=sum+28+isleap(year)
	sum+=day		
	return sum%7
year,month,day=eval(input("输入任意日期（year,month,day）："))
print("{}年{}月{}日是星期{}".format(year,month,day,weekday(year,month,day)))
