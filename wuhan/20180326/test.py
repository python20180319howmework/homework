print("{:>20}:{:<8.2f}".format("我们的成绩是",78.4567))

print("{0:b},{0:d},{0:o},{0:x}".format(256))

s = "python" 
t = "最好用的语言"
s += t
print(s,s[-1],s[2:9],s[:3],s[-3:-1])

print("4" + "5")

s = "We are FAMILY"
print(s.upper())
print(s.lower())
print(s.split())

a =int(input("请输入一个1~100的整型数:"))
while(1<a<100):
	print("你好棒啊!继续努力")
	break
else:
    print("乖乖,你咋这么不听话呢")

n = 10
print(n>10 & n<=100)

print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)

a = 10
b = 20
c = 50
a,b,c = b,c,a
print(a,b,c)

b =int(input("请输入年份:"))
if(b%4) ==0:
	if(b%100) == 0:
		if(b%400) == 0:
			print("{0}是闰年".format(b))
		else:
			print("{0}不是闰年".format(b))
	else:
		print("{0}是闰年".format(b))
else:
	print("{0}不是闰年".format(b))

