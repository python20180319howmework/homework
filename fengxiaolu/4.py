y = int(input("请输入年份："))
m = int(input("请输入月份："))
d = int (input("请输入日："))
s = 0
days = [31,28,31,30,31,30,31,31,30,31,30,31]
i = 0
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
	days[1] = 29
while i < m - 1:
	s = s + days[i]
	i = i + 1
print("这一日期是该年的第%s天" % (s + d))