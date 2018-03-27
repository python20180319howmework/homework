



#1.编写一个计时器,将计时结果显示出来
import time
t = time.time()

for i in range(6):
	
	tl = time.localtime(i)

	
	ts = time.strftime("%S",tl)
	
	print(ts)
	time.sleep(1)

#2.随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出
import random
l1 = (random.randint(0,100))
print("l1=%d"%(l1))
l = []
count = 0
while l1>0:
	for i in range(l1):
		l.append(l1%2)
		l1 //= 2
		count += 1
else:
	print("对应二进制为",end="")
for i in range(count):
	print(l[count-i-1],end="")





#3.用户任意输入他的生日，判断他输入00后，90后，还是80后
year = int(input("请输入出身年份"))


if 80 <= year <= 89: 
	print("是80后")
elif 90 <= year <= 99:
	print("是90后")
elif 0 <=year <= 9:
	print("是00后")
else:
	print("你out了")
	
#4.总结整型、浮点、字符串、列表、元祖、字典、集合的常用方法，且比较各自擅长的领域


'''
整型：正整数或负整数,不带小数点，将字符串转换为数字，进制的转换
浮点：由整数部分和小数部分组成,浮点型也可以使用科学计数法表示
字符串：普通字符串是通过ASCII存储的可以进行拼接大小写转换等
列表:是内容可变的、有序的，和字符串以及元组不同，非常的常用
元祖：元组和列表一样，但是无法修改
字典：字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中字典的建是唯一的
集合：集合可以有任意数量的元素，它们可以是不同的类型（例如：数字、元组、字符串等）。但是，集合不能有可变元素（例如：列表、集合或字典）



'''


'''
5现在有一个列表，li = [1,2,3,'a','b','4','c'],有一个字典（此字典是
动态生成的，并不知道里面有多少键值对，所以用 dic = {} 模拟此字典 ）；
现在需要完成这样的操作：如果字典没有‘k1’这个键，那么就创建这个‘k1’这个键和
对应的值（该键值设为空列表），并将列表li中的索引位为奇数对应的元素，添加到‘k1’
这个键对应的值中
'''
dic = dict()

l= []
li = [1,2,3,'a','b','4','c']
dic = {}
print(dic.get("k1","k1"))
l.append([li[1],li[3],li[5]])

dic["k1"]=l




print(dic)
'''
#6.组合嵌套题，有如下列表，按照要求实现每一个功能
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
<1> 将列表lis中的‘tt’变成大写（两种方式）
<2> 将列表lis中数字3变成字符串‘100’（两种方式）
<3>将列表中‘1’变成数字101（两种方式）
'''

lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
#<1>
l1 = lis[0][1][2]
print(l1)



for key in l1.keys():
	print(key)
for value in l1.values():
	print(value)
s = value[0]
print(s)
s1 = s.upper()
print(s1)
'''方法二
if  ord(s)>= ord("a")and ord(s) <= ord('z'):
	print("TT")
'''
#<2>
s1 = value[1]
s1 = '100'
print(s1)
value[1] = '100'
print(s1)
#<3>
s2 = value[2]
s2 = 101
print(s2)
value[2] = '101'
print(s2)

#7.请删除字典中的键'k5',如果不存在键'k5',则输出"对不起！不存在你要删除的元素

d ={}
print(d.pop("k5","对不起!不存在你要删除的元素"))
#8.删除元祖中的所有重复的元素，并生成一个列表



l =(1,2,3,5,5,3,1,4,7)
s = set(l)
m = list(s)
print(type(m),m)

