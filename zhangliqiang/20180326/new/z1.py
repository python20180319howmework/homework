

#让用户输入他的体重和身高 判断BMI,根据BMI指标合理给出建议
#BMI= 体重/身高×身高
kg = int(input("请输入体重"))
m  = float(input("请输入身高"))
BMI = kg/(m*m)
if BMI < 18.5:
	print("你这么瘦,可以肆无忌惮的大吃大喝")
elif 18.5 <= BMI < 25: 
	print("兄弟！你离模特就差八块腹肌了")
elif 25 <= BMI < 30:
	print("控制你自己！脂肪有点多")
else:  
	print("不能再吃了！跑几圈去吧,你也可以是男神")

#判断从你出生到今年共有多少闰年
cnt = 0
year = int(input("请输出生年份"))
for i  in range(year,2018):
	if(i% 400 == 0)or (i%4==0 and i%100 !=0):
		cnt +=1
print("共%d个闰年" % cnt)

#判断一个三位整形数，判断它是否是一个水仙花数(如153=1*1*1+5*5*5+3×3*3)
from math import*


n = int(input("请输入一个三位整形数"))

c1 = n//100

c2 = n//10%10

c3 = n%10
if n == c1 ** 3 + c2 ** 3 + c3 ** 3:
	print("{}是水仙花数".format(n))
count = 0
for i in range(100,1000):
	a1 = i//100%10
	a2 = i//10%10
	a3 = i%10
	if i == a1**3 + a2**3 + a3**3:
		print(i)
		count += 1
		print(count)
#4.读入用户输入的一个日期(年，月， 日)，判断这一天是这年的第几天

from math import*

year = int(input("请输入年份"))
month = int(input("请输入月份"))
day = int(input("请输入天"))
sum1 = day
days = [31,28,31,30,31,30,31,31,30,31,30,31]
i = 0
if(year%4 == 0 and year %100 !=0)or(year %400 == 0):
	days[1] =29
while i < month -1:
	sum1 = sum1 + days[i]
	i += 1
print("这是一年的第{}天".format(sum1))


#5.读入用户输入的一个字符串，判断字符串中有多少个大写字母，多少个数字，多少个小写字母

passwd = input("输入字符串")
d = 0
x = 0
num = 0
for i in passwd:
	if ord('A')<= ord(i) <= ord('Z')
		d = d + 1
		if ord ('a')<= ord(i)<= ord('z')
			x = x + 1
		else:
			num = num +1
		print(d,"大写字母",x，"小写字母",num,"数字")


	





