n=int(input("please input a year:"))
if n%400==0 or n%100!= 0 and n%4==0:
	print("this year have {} day".format(366))
else:
	print("this year have {} day".format(365))
