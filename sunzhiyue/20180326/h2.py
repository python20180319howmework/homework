# 1
h = float(input("请输入身高"))
t = float(input("请输入体重"))
BMI = t / (h * h)
if BMI < 18.5:
	print("你这么手，可以肆无忌惮的大吃大喝啦")
elif 18.5 <= BMI < 25:
	print("兄弟！你离模特就差八块腹肌了")
elif 25 <=BMI < 30:
	print("控制自己哦！脂肪有点多了")
elif BMI >= 30:
	print("不能再吃了！跑几圈去吧，你也可以是男神")

#2
s = int(input("请输入出生年份"))
j = int(input("请输入今年年份"))
c = 0
for i in range(s, j):
	if (i % 4 == 0 and i % 100 !=0)or i % 400 == 0 :
		c += 1
print("从你出生到今年共有{}闰年".format(c))


#3
num = int(input("请输入一个三位正整数"))
ge = num % 10
shi = (num // 10) % 10
bai = num // 100
if num == pow(ge, 3)+pow(shi, 3)+pow(bai, 3):
	print("{}是水仙花数".format(num))
else:
	print("{}不是水仙花数".format(num))


#4


year = int(input("输入年份"))
month = int(input("输入月份"))
day =  int (input("输入日期"))
count = day
i = 0
day1 = [31, 28, 31, 30, 31, 30,31, 31, 30, 31,30,31]
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
	day1[1]=29
while i<month-1:
	count = day1[i]+ count
	i +=1
print(count)


#5
str1 = input("请输入一个字符串")
A = 0
b = 0
num1 = 0
for i in range(len(str1)):
	if str1[i].isdigit():
		num1 += 1
	elif 65<= ord(str1[i])<=90:
		A += 1
	elif 97 <= ord(str1[i])<=122:
		b += 1
print("大写字母有{}".format(A))
print("小写字母有{}".format(b))
print("数字有{}".format(num1))





