#判断从你出生到今年共有多少的闰年 
year=int(input("输入你的出生年份:"))
count=0
for i in range(year,2018):
	if((i%4==0 and i%100!=0)or i%400==0):
		count+=1
print("从你出生到今年共有%d个闰年"%(count))
