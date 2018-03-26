#第一题
print("{:>20}:{:<8.2f}".format("我们的平均成绩是",78.4567))

#第二题

a = 256
print("{0:b},二进制,{0:o},八进制,{0:d},十进制,{0:x},十六进制".format(a))

#第三题

#python 最好用的语言  thon 最好用  pyt  的语

s = "python"
t = "最好用的语言"
s += t
print(s[-3:-1])

#第四题
#4 5

#第五题

s = "We are FAMILY"
print(s.upper())
print(s.lower())
print(s.split())

#第六题

a =int( input("输入一个1~100的整型数"))
if a in range(1,101):
	print("你好棒，继续努力")
else:
	print("乖乖，你咋这么不听话呢")

#第七题
#n > 10 and n <= 100

#第八题

print(3 and 4)
#9


#第九题

a, b, c = 50, 10, 20
print(a, b, c)





#第十题
b = int(input("请输入年份"))
if b % 4 == 0 or b % 400 == 0 and b % 100 != 0:
	print("366")
else:
	print("365")


