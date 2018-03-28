#1.编写一个计时器,将计时结果显示出来import random
'''
import time
for i in range(101):
	t = time.time()
	tl = time.localtime(t)
	ts = time.strftime("\r%Y-%m-%d %H-%M-%S",tl)
	i += 1
	time.sleep(1)
	print(ts,end = " ")

#2.随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出
from random import *
l = []
n = randint(0,1000)
print(n)
for i in range(0,501):
	if n > 1:	
		m = n % 2
		n = n // 2
		i += 1
		l.insert(0,m)
else :
	l.insert(0,n)
 
print(l)


#3.用户任意输入他的生日，判断他输入00后，90后，还是80后
i = input("请输入您的破壳日：")
y = int(i[0:4])
print(y)

if 1980 <= y < 1990:
	print("80后")
elif 1990<= y < 2000:
	print("90后")
elif y >= 2000:
	print("00后")
else:
	print("你out了")

#5.现在有一个列表，li = [1,2,3,'a','b','4','c'],有一个字典（此字典是
#动态生成的，并不知道里面有多少键值对，所以用 dic = {} 模拟此字典 ）；
#现在需要完成这样的操作：如果字典没有‘k1’这个键，那么就创建这个‘k1’这个键和
#对应的值（该键值设为空列表），并将列表li中的索引位为奇数对应的元素，添加到
li = [1,2,3,'a','b','4','c']
dic = {}
l = []

if dic.get("k1",-1) == -1:
	dic["k1"]= ""
	for i in range(len(li)):
			if i % 2 != 0:
				print(i)
				l.append(li[i])

dic["k1"]= l
print(dic)

#6.组合嵌套题，有如下列表，按照要求实现每一个功能
#lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
#<1> 将列表lis中的‘tt’变成大写（两种方式）
#<2> 将列表lis中数字3变成字符串‘100’（两种方式）
#<3>将列表中‘1’变成数字101（两种方式）


lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
l1 = lis[0][1][2]
l1["k1"]= ["TT",'3','1']
print(lis)

l1["k1"] =  ["tt",'100','1']
print(lis)

l1["k1"]= ['tt','3',101]
print(lis)
'''

#7.请删除字典中的键'k5',如果不存在键'k5',则输出"对不起！不存在你要删除的元素"
dic = {}
num = 0
for key in dic.keys():
	num += 1	
if num >= 5 :
	dic.pop(k5)
else:
	print("对不起，不存在你要删除的元素")
	

#8.删除元祖中的所有重复的元素，并生成一个列表
s =  [1,1,1,3,2,58,1,3,0,3,574]
l = set(s)
t2 = tuple(l)
print(type(t2),t2)





