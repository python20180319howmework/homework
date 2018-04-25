#1.print("{:>20}:{:<8.2f}".format("我们的平均成绩是",78.4567))
#             我们的平均成绩是:78.45    ok
#2.输入256
num=256
print("{0:b},{0:d},{0:o},{0:x},{0:X}".format(num))
#3.s="python",t="最好用的语言"，s+=t,则
#s输出：python最好用的语言
#s[-1]输出：言
#s[2:9]输出：thon最好用
#s[:3]输出：pyt
#s[-3:-1]输出：的语
s="python"
t="最好用的语言"
s+=t
print(s)
print(s[-1])
print(s[2:9])
print(s[:3])
print(s[-3:-1])
#4."4"+"5"不等于"9",等于"45"
#5.
s="We are FAMILY"
S=s.upper()
ss=s.lower()
print(S,ss,s.split(" "))
#6.
num=int(input("请输入1～100之间的一个整型数："))
if num>=1 and num<=100:
	print("你好棒阿！继续努力")
else:
	print("乖乖，你咋这么不听话呢")
#7.n>10 and n<=100
#8.not1or0and1or3and4or5and6or7and8and9
#False or 0 or 4 or 6 or 9
#0 or 4 or 6 or 9
#4 or 6 or 9
#4 or 9
#4(答案)
#9.以下：
a,b,c=10,20,50
a,b,c=b,c,a
print(a,b,c)
#10.以下：
year=int(input("请输入任意一年："))
if year%4==0 and year%100!=0 or year%400==0:
	print("{}年有366天".format(year))
else:
	print("{}年有365天".format(year))	
