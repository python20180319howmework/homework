n=int(input("please input your birthyear:"))
y=int(input("this year is:"))
count=0
for i in range(n,y+1):
	if i%400==0 or i%100!=0 and i%4==0:
		count=count+1
print("从你出生到今年共有{}个闰年".format(count))
