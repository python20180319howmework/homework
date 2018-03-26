
# 1.思考下列语句输出结果

mystrf = "我们的平均成绩是          "
myfloat = "78.4567 "
print("{:>20}".format(mystrf))
print("{0:.2f}".format(float(myfloat)))

#2. 格式化输出256 二进制。。

num1 = 256
print("{0:b},{0:d},{0:o},{0:x},{0:X}".format(num1))

#3. 

s = "python"
t = "最好用的语言"
s += t
print(s,s[-1],s[2:9],s[:3],s[-3:-1])
#4.
a = 4
b = 5
c = a + b
d = 9
print(c is d)

#5  “We are FAMILY”,求得其对应的全部大写，全部小写，以及将其切分按空格
statement = "We are FAMILT"
s2 = statement.upper()
print(s2,statement)
print(s2.lower())
#6.要求用户输入1～100之间的一个整型数，如果用户输入符合要求则输出"你好棒阿！继续努力",
#否则输出"乖乖,你咋这么不听话呢"
num2 = int(input("请输入1-100中的数字")) 

if num2 in  range (1, 100):
	print("你好棒啊 继续努力")
else:
	print("乖乖，你咋这么不听话呢")
#7.
print("a > 2 and a <= 100")

#8.
print("false")
#9.
a = 10
b = 20
c = 50

d = a
a = c
c = b
b = d
print(a,b,c,d)
#10.
year = int(input("请输入年份"))
if(year% 400 == 0)or (year%4==0 and year%100 !=0):
	print("一年有366天".format(year))
else:
	print("一年有365天".format(year))









