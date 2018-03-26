#第一题
'''
i = int(input("请输入身高："))
m = int(input("请输入体重"))
BMI = m / (i*i)
if BMI < 18.5:
	print("你这么瘦,可以肆无忌惮的大吃大喝了")
elif 18.5 <= BMI < 25:
	print("兄弟，你离模特就差八块腹肌了")
elif 25 <= BMI < 30:
	print("控制你自己哦！脂肪有点多啦")
elif BMI >= 30:
	print("不能再吃了！跑几圈去吧，你也可以是男神")
'''
#第二题
'''
year =int(input ("请输入你的出生年月日："))
cnt = 0
for year in range(year,2019):
	if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
		cnt += 1
print(cnt)

'''
#第三题
flower = int(input("请输入一个三位整型数："))
a = flower%10
b = flower//10%10
c = flower//100%10
num = 0
if flower == a*a*a + b*b*b + c*c*c:
	print("{}是水仙花数".format(flower))
else:
	print("{}不是水仙花数".format(flower),"\n")
for hua in range(111,1000):
	d = hua % 10
	e = hua // 10 % 10
	f = hua //100 % 10
	if hua == d*d*d + e*e*e + f*f*f:
		num += 1
		print("三位数里{}是水仙花数".format(hua))
print("共有{}个水仙花数".format(num))
‘
第四题
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

#第五题
mystr = str(input("请输入字符串："))
DX = 0
XX = 0

for s in mystr:
	if ord('a')<= ord(s) <= ord('z'):
		XX += 1
		
for s in mystr:
	if ord('A') <= ord(s) <= ord('Z'):
		DX += 1


print("{}中有{}个大写{}个小写".format(mystr,DX,XX))


























