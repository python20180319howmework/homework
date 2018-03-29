#1
'''
def sum1(m, n):
sumnum = 0
	for i in range(1, n+1):
		sumnum = sumnum + int(str(m)*i)
	return sumnum
	print("是{}".format(sumnum))
a, b = eval(input("请输入两个1到十之内的整型数")
print(sum1(a, b)

'''

'''
# 2
l = ["172.16.3.1","172.16.1.5","172.15.2.0","172.16.3.1","172.16.3.1","172.16.1.5"]
d = []

for i in range(0, 6):
	d.append(int(l.count(l[i])))
if d[i] == max(d):
print("{}出现了{}次".format(l[i],max(d)))

'''




'''

#3.定义一个函数，计算给定的整型数是否为质数
num = 0
def zhiheshu(num):
	num = int(input("请输入一个整型数:"))
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				return 1
				break
			else:
				return 0
if zhiheshu(num) == 1:
	print("{}"是.format(num))
else:
	print(("{}"不是.format(num))

'''



#5.定义一个函数，判断用户输入的成绩所属的等级
'''
a = 0
def banduan(a):
	a = int(input("请输入您的成绩:"))
	if 90 <= a <  100:
		return "A"
	elif 80 <= a < 90:
		return "B"
	elif 70 <= a < 80:
		return "Ci"
	elif 60 <= a < 70:
		return "D"
	else:
		return "E"
print("您的等级为：",banduan(a))
'''
















