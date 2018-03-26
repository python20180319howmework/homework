'''
输入身高体重,判断BMI值,给出建议
'''

'''
i = int(input("请输入身高"))
t = int(input("请输入体重"))
b = t / (i * i)
if b < 18.5:
	print("你这么瘦,可以肆无忌惮的大吃大喝啦")
elif 18.5 <= b <=25:
	print("兄弟,你离模特就差八块腹肌了")
elif 25 <= b <= 30:
	print("控制住你计几,脂肪有点多了")
elif 30 <= b:
	print("不能再吃啦,跑几圈去吧,你也可以是男神")
'''
'''
判断你出生到今年共有多少个闰年
'''
'''
chusheng = int(input("请输入你的出生年份"))
jinnian = int(input("请输入今年的年份"))
zongji = 0
for nian in range(chusheng,jinnian+1):
	if nian % 4 == 0 and nian % 4 !=0 or nian % 4 == 0:
		zongji = zongji + 1
		print(zongji,"个闰年")
'''
'''
输入三位整数,判断它是否是水仙花数,计算出有多少个水仙花数
'''
'''
shuru = int(input("请输入一个三位整数"))
gewei = shuru % 10
shiwei = (shuru // 10) % 10
baiwei = (shuru // 100) % 10
if shuru == (gewei ** 3) + (shiwei ** 3) + (baiwei ** 3):
	print("是水仙花数")  
else:
	print("不是水仙花数")
'''
'''
l = 0
for p in range(100,1001):
	ge = p % 10
	shi = (p // 10) % 10
	bai = (p // 100) % 10
	if p == (ge ** 3) + (shi ** 3) + (bai ** 3):
		l = l + 1
		print(p)
		print(l,"个水仙花数")
'''
'''
输入一个日期,判断是这一年的第几天
'''
'''
pingnian = [31,59,90,120,151,181,212,243,273,304,334,365]
runnian = [31,60,91,121,152,182,213,244,274,305,335,366]
year = int(input("请输入年份"))
month = int(input("请输入月份"))
day = int(input("请输入日期"))
remained = 0
if year % 4 == 0 and year % 4 !=0 or year % 4 == 0:
	if month > 1:
		remained = runnian[month - 1] + day
	else:
		remained = day
else:
	if month > 1:
		remained = pingnian[month - 1] + day
	else:
		remained = day
print(remained,"天")
'''
'''
读入用户输入的字符串,判断字符串中有多少各大写字母,多少个数字,多少个小写字母
'''
chuan = input("请输入一段字符串")
da = 0
xiao = 0
shu = 0
for k in chuan:
	if ord('A')<= ord(k)<= ord('Z'):
		da = da + 1
		if ord('a')<= ord(k)<= ord('z'):
			xiao = xiao + 1
		else:
			shu = shu + 1
		print(da,"个大写字母",xiao,"个小写字母",shu,"个数字")




















