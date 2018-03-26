#4
data = input("请输入一个日期[格式例如20180326]：")
year = int(data[0:4])
mouth = int(data[4:6])
day = int(data[6:])
if year%4 == 0 and year%100 !=0 or year%400 == 0:
	n = 29
else:
	n = 28
tianshu=0
aaa = [31,n,31,30,31,30,31,31,30,31,30,31]
for i in range(1,13):
	if i == mouth:
		for b in range(i-1):
			tianshu += aaa[b]

	
print("{}月{}日是{}年的第{}天".format(mouth,day,year,tianshu+day))



#print("这是{}年的第{}天".format())

