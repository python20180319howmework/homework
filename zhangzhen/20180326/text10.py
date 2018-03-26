
year = int(input("请输入年份："))
if (year % 4 == 0 & year % 100 != 0) or (year % 400 == 0):
	print("这一年有366天")
else:
	print("这一年有355天")


