#1
heavy = float(input("请输入体重:"))
high = float(input("请输入身高:"))
BMI = heavy/(high*high)
print(BMI)
if BMI < 18.5:
   print("你这么瘦，可以肆无忌惮的大吃大喝啦")
elif BMI>=18.5 and BMI < 25:
   print("兄弟！你离模特就差八块腹肌了")
elif BMI>=25 and BMI<30:
   print("控制你自己哦!脂肪有点多啦")
elif BMI >=30:
  print("不能再吃了！跑几圈去吧，你也可以是男神")
else: 
  print("加油")
#2
year = int(input("请输入出生年份:"))
count= 0
count1=2018-year+1
while count1>0:
     if year%4==0 and year%100!=0 or year%400== 0:
        count=count+1
        year=year+1
        count1=count1-1
     else:
        count=count+0
        count1=count1-1
        year=year+1

print(count)

#3
num =int(input("请输入一个三位整型数:"))
num1=num%10
num2=((num-num1)%100)/10
num3=(num-num2*10-num1)/100
sumn=pow(num1,3)+pow(num2,3)+pow(num3,3)
if(sumn==num):
   print("是水仙花数")
else:
   print("不是水仙花数")
#3.2
count=0
num=100
while(num<=999):
   num1=num%10
   num2=((num-num1)%100)/10
   num3=(num-num2*10-num1)/100
   sumn=pow(num1,3)+pow(num2,3)+pow(num3,3)
   if(sumn==num):
      count+=1
      num+=1
   else:
      count+=0
      num+=1
print(count)
#4
year=int(input("请输入年：")) 
month=int(input("请输入月："))
day=int(input("请输入日："))
sumn=0 
days=0
if(year%4==0 and year%100!=0 or year%400==0):
   day1=[31,29,31,30,31,30,31,31,30,31,30,31]
   for i in day1[:month-1]:
       sumn+=i
   days=sumn+day
else:
    day2=[31,28,31,30,31,30,31,31,30,31,30,31]
    for j in day2[:month-1]:
        sumn+=j
    days=sumn+day
print(days)

#5
str=input("请输入一个字符串：")
count1=0
count2=0
count3=0
i=0
while i<len(str):
     
     if(65<=ord(str[i])<=90):
        count1+=1
     if(97<=ord(str[i])<=122):
        count2+=1
     if(str[i].isdigit()):
        count3+=1
     i+=1
print("该字符串有{}个大写字母，{}个小写字母，{}个数字"\
.format(count1,count2,count3)) 
#选作1
num=int(input("请输入行数："))
i=0
while i<=num:
   print("*"*i)
   i+=1
for j in range(1,num+1):
   print(" "*(num-j),end="")
   print("*"*(j*2-1),end="")
   print(" "*(num-j))
'''
#选作2
year=int(input("请输入任意年："))
month=int(input("请输入任意月："))
day=int(input("请输入任意日："))
days=0
for i in range(1999,year):
	days+=365
     if(i%4==0 and i%100!=0 or i%400==0):
     	days += 1
     else:
     	days += 0
if(year%4==0 and year%100!=0 or year%400==0):
	day1=[31,29,31,30,31,30,31,31,30,31,30,31]
	for j in day1[:month-1]:
	    days+=day1[j]
	days+=day
else:
	day2=[31,28,31,30,31,30,31,31,30,31,30,31]
	for k in day2[:month-1]:
        days+=day2[k]
    days+=day
weekday=days%7
print("该天是星期{}".format(weekday))
'''
