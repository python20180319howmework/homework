#1.编写一个计时器,将计时结果显示出来
'''
from time import *

for i in range(100):
	print(strftime("\r%H:%M:%S",localtime(time())),end="")
	
	sleep(1)
'''
#2.随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出
from random import *

num= randint(1,10)
print(num)
l=[]
while num>0:
	l.append(num%2)
	num//=2
else:
	l.reverse()
	print(l)
#3.用户任意输入他的生日，判断他输入00后，90后，还是80后
birth=input("请输入你的生日：")
if 1990<=int(birth[:4])<=1999:
	print("你是90后")
elif 1980<=int(birth[:4])<=1989:
	print("你是80后")
elif int(birth[:4])>=2000:
	print("你是00后")	
'''
4.总结整型、浮点、字符串、列表、元祖、字典、集合的常用方法，且比较各自擅长的领域
列表l=list() 可变 有序 有索引
	<1>增 list.append() 末尾增
	      list.insert() 任意位置增
	<2>删 list.pop()   末尾位置删
          list.pop(2)  把索引2号位置内容删除
          list.remove(value) 删除指定内容
	<3>改 list[]=" "  
	<4>查 list[][]..
    <5>扩展list1.extend(list2) 把list2的内容加入到list1中

元祖  l=(a,b,...)
	不可变 有序 有索引
字典  l={key:value,...} 可变 无序
  字典中的Key一定是不可变对象(整型数，浮点数，元祖，字符串) value 没要求
	<1>增 dict[newkey]=" value"
	<2>删 dict.pop(key)
	<3>改 dict[key]="value"
	<4>查
		查字典中否含有某一个key    "key" in l     l.get("key",-1)
	<5> 获得字典中所有的key
		for key in l.keys():
			print(key)
	<6>获得字典中所有的value
		for value in .values():
			print(value)
	<7>获得字典中所有的item
		for item in d2.items():
			print(item)
集合   set
	<1>集合无序可变不重复无索引	
	<2>去重复			s = set([1,2,2,3,4,5,7,6,5,4,3,2])
	<3>增			s.add()用于增加一个元素值
s.update([])，用于增加多个元素值，参数为list，注意如果用add增加多个值，会报参数类型错误。
	<4>删    s.pop()  当集合是由列表和元组组成时,set.pop()是从左边删除元素的,对于是字典和字符转换的集合是随机删除元素的.
	s.remove(value) 删除指定内容
remove()用于删除一个set中的元素，这个值在set中必须存在，如果不存在的话，会引发KeyError错误。
discard()用于删除一个set中的元素，这个值不必一定存在，不存在的情况下删除也不会触发错误。
    <5>清空函数  s.clear(),将set全部清空。
字符串	str 不可变 有序 有索引
	<1>以字母跟下划线开头
	<2>字符串中每一个字符的索引从0开始	
	<3>stu[start:end:step]
	<4>字符串之间+表示连接,数字与字符串之间*表示复制
	<5>str.upper()	大写
	   str.lower()	小写
	   str.split(sep="是")  分割字符串， sep指明分隔符
    <6>len(str)
浮点类型和整数类型的区别主要在取值范围和精度上
'''
'''
5.现在有一个列表，li = [1,2,3,'a','b','4','c'],有一典（此字典是
动态生成的，并不知道里面有多少键值对，所以用 dic = {} 模拟此字典 ）；
现在需要完成这样的操作：如果字典没有‘k1’这个键，那么就创建这个‘k1’这个键和
对应的值（该键值设为空列表），并将列表li中的索引位为奇数对应的元素，添加到‘k1’
这个键对应的值中
'''
l = [1,2,3,'a','b','4','c']
dic = {}
l1 = []
if dic.get('k1',-1) == -1:
	dic['k1'] = ''
for i in range(len(l)):
	if i % 2 !=0:
		l1.append(l[i])
dic['k1'] = l1
print(dic)
'''
6.组合嵌套题，有如下列表，按照要求实现每一个功能
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
<1> 将列表lis中的‘tt’变成大写（两种方式）
<2> 将列表lis中数字3变成字符串‘100’（两种方式）
<3>将列表中‘1’变成数字101（两种方式）
'''
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
l2=lis[0]
l3=l2[1]
dic=l3[2]
dic['k1']=['TT',3,'1']

print(lis)
dic['k1']=['tt','100','1']
print(lis)
dic['k1']=['tt',3,101]
print(lis)

lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
#第一种方法
l = list(lis[0][1][2].keys())
print(l[0])
lis[0][1][2][l[0]] = ['TT',3,'1']
print(lis)
lis[0][1][2][l[0]] = ['tt','100','1']
print(lis)
lis[0][1][2][l[0]] = ['tt',3,101]
print(lis)

#第二种方法
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
lis = [['k',['qwe',20,{'k1':['TT',3,'1']},89],'ab']]
print(lis)
lis = [['k',['qwe',20,{'k1':['tt','100','1']},89],'ab']]
print(lis)
lis = [['k',['qwe',20,{'k1':['TT',3,101]},89],'ab']]
print(lis)
#7.请删除字典中的键'k5',如果不存在键'k5',则输出"对不起！不存在你要删除的元素"
dic = {}
for key in dic.keys():
	if key=='k5':
		dic.pop(k5)
else:
	print("对不起！不存在你要删除的元素。")
#8.删除元祖中的所有重复的元素，并生成一个列表
a = (1,2,3,1)  #定义一个元祖
l = list(a)   #将元组转换为列表

l2 = []      #定义一个空列表用来存放去重后的字符串

for i in l:   #遍历去重
	if not i in l2:
		l2.append(i)   #将字符串添加到空列表里

print("元组为{}转换成列表为{}去重后为{}".format(a,l,l2))

s=(1,2,3,4,1,2,5)
l= list(set(s))
print(type(l),l)
