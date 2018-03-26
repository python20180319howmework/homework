

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
