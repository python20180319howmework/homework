year=int(input("请输入年份"))
for year in range(1993,2018):

if year % 4 == 0 and year % 100 != 0:
	print("yes")
elif year%400==0:
	print("yes")
else:
	print("no")

