"""
读入用户输入的任意一年，判断有多少天
"""
year = int(input("输入年份：")) 
a = year%100
b = year%4
c = year%400
if (a != 0 and b == 0 )or  c == 0:
	print("这一年有３６６天")
else:
	print("这一年有３６５天")
