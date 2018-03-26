

#判断从你出生到今年有多少瑞年

birth=int(input("输出你的出生年份："))
num =0
for i in range(birth,2018):
	if i%4==0 and i%100!=0 or i%400==0:
		num+=1
	else:
		pass
print(num)
