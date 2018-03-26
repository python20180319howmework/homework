
#第一题  输出 78.45  第一个字符串右对齐  第二个字符串左对齐
print("{:>20}:{:<8.2f}".format("我们的平均成绩是", 78.4567))




#第二题 格式化输出256的二进制，十进制，八进制，十六进制表达

num1 = 256
print("{0:b},{0:d},{0:o},{0:x}".format(num1))

#第三题 s = "python",t = "最好用的语言",s += t,则
#s , s[-1],s[2:9],s[:3],s[-3:-1]分别输出的是什么

s = "python"
t = "最好用的语言"
s += t
print(s,s[-1],s[2:9],s[:3],s[-3:-1])
# 分别输出   s += t 即s = s + t  s = "python最好用的语言"
#全部、最后一个字、字符串第三个字符到第十个字符
#第一个字符到第四个字符 和倒数第三个字符到倒数第二个字符


#第四题
#不等于  因为字符相加是拼接在一起  而不是求和
print ("4" + "5")
#第五题

s = "We are FAMILY"
print(s.upper())
print(s.lower())
print(s.split())
#第六题
num = int (input ("请输入一个1-100的整型数"))
if  (1<num<100):
	print("你好棒啊，继续努力！")
else :
	print("乖乖，你咋这么不听话呢")


# 第七题  n>10 and n <= 100
#第八题
print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)
#第九题
a = 10
b = 20
c = 50
a,b,c=20,10,50
print(a,b,c)
print("a={2},b={0},c={1}".format(a,b,c))
#第十题
i = int(input("请输入年份"))
if (i % 400 == 0)or (i%100 != 0 and i % 4 == 0) :
	print("总共有366天")
else: 
	print("总共有365天")













