from math import *
print("{:>20}:{:<8.2f}".format("我们的平均成绩是",78.4567))

a = 256
print("{0:x}".format(a))
print("{0:d}".format(a))
print("{0:b}".format(a))
print("{0:o}".format(a))
s = "python"
t = "最好的语言"
s += t
print(s)
print(s[-1])
print(s[2:9])
print(s[:3])
print(s[-3:-1])

print("4+5","=",4+5)

k = "We are FAMILY"
print(k.upper())
print(k.lower())
print(k.split())





zx = int(input("请输入整形数："))


if 1<=zx<=100:
	print("你好棒，继续努力！")

else:
	print("乖乖，你咋这么不听话呢")

n = 33
print(10<n and n<=100)



print(not 1 or 0 and  1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)	




a,b,c =10,20,50
a,b,c =20,50,10
print(a,b,c)



year =float( input("输入任意年："))
if (year%4 == 0 and year% 100!= 0) or year% 400== 0:
	print("是瑞年")
else:
	print("不是瑞年")
