t = int(input("请输入你的体重(kg):"))
s = float(input("请输入你的身高(m):"))
BMI = t/(s * s)
if BMI < 18.5:
	print("你这么瘦,可以肆无忌惮的大吃大喝啦")
elif 18.5<=BMI<25:
	print("兄弟!你离模特就差八块腹肌了")
elif 25<= BMI< 30:
	print("控制你自己哦!脂肪有点多啦")
else:
	print("不能再吃了!跑几圈去吧,你也可以是男神")

num = 0
birthyear = int(input("请输入你的出生年份:"))
for birthyear in range(birthyear,2018):
	if (birthyear%400==0 or (birthyear%4==0 and birthyear%100 != 0)):
		num = num + 1	
print("经历了%d个闰年"% num)

from math import *
num1 = int(input("输入一个三位数的整数:"))
bai = num1//100
shi = num1 % 100 //10
ge = num1 % 10
result = pow(bai,3)+ pow(shi,3)+ pow(ge,3)
if num1 == result:
	print("这个数是水仙花数")
else:
	print("这个数不是水仙花数")

for i in range(100,1000):
	bai = i//100
	shi = i % 100 //10
	ge = i % 10
	if i == pow(bai,3)+ pow(shi,3)+pow(ge,3):
		print(i,end= ",")


from math import *
year=int(input("请输入一个年份："))
month=int(input("请输入一个月份："))
day=int(input("请输入日："))
count=day
i=0
days=[31,28,31,30,31,30,31,31,30,31,30,31]

if year%4==0 and year%100!=0 or year==400:
	days[1]=29
while i<month-1:
	count=days[i]+count
	i+=1
print(count)


count=0
count1=0
count2=0
str0=input("请输入一个字符串：")
for i in range(len(str0)):
	if str0[i].isdigit():
		count+=1
	if 65<=ord(str0[i])<=90:
		count1+=1
	if 97<=ord(str0[i])<=122:
		count2+=1
print("数字有%d个" % count)
print("大写字母有%d个"% count1)
print("小写字母有%d个"% count2)
