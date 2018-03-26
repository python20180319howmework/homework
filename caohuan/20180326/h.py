#第一题
print("{:>20}:{:<8.2f}".format("我们的平均成绩是",78.4567))
#我们的平均成绩是78.46

#第二题
a=256
print("{0:b},{0:d},{0:o},{0:X}".format(num))
#dec=256,oct=400,hex=100

#第三题
s="python"
t="最好用语言"
s+=t
print(s,s[-1],s[2:9],s[:3],s[-3:-1])
#python最好用语言 言 thon最好用 pyt 的语 

#第四题
#不等于

#第五题
s="We are FAMILY"
s2=s.upper()
print(s2)
print(s2.lower())

#第六题
i = input("请输入一个数：")
num = int(i)
if 1 <= num <= 100:
	print("你好棒阿！继续努力")
else:
	print("乖乖，你咋这么不听话呢")

#第七题
'''
n > 10 and n <= 100

'''


#第八题
print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)
# 4

#第九题
a=10
b=20
c=50
a,b,c=c,b,a
print(a,b,c)


#第十题
y = input("请输入年份：")
num = int(y)
if (num% 4 ==0)and(num% 100 != 0):
	print("{}年366天".format(num))
elif(num% 400 == 0):
		print("{}年366天".format(num))
else:
	print("{}年365天".format(num))








