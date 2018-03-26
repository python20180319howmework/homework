#1，输出的是我们班的平均成绩是78.46

#2,
print("{0:b},{0:d},{0:o},{0:X}".format(256))

#3,s       为    python最好用的语言
#  s[-1]   为    言
#  s[2:9]  为    thon最好用
#  s[:3]   为    pyt
#  s[-3:-1]为    的与
 
#4,两个引号里面的内容拼接  应该为  45

#5,
s="WE are FAMILY"
s1=s.upper()
s2=s.lower()
print(s1,s2,s.split(" "),sep="\n")

#6,
a=int(input("请输入："))
if 0<a<100:
	print("你好棒阿！继续努力")
else :
	print("乖乖，你咋这么不听话呢")

#7,n>10 and n<=100

#8,结果为4

#9,a,b,c 互换
a = 10
b = 20
c = 50
print("换后的a={1},换后的b={2},换后的c={0}".format(a,b,c))

#10,
year=int(input("请输入查询的年份："))
if year%4 == 0 and year%100 !=0 or year%400 == 0:
	print(year,"年有366天")
else:
	print(year,"年有365天")




















