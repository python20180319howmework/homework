'''
1.编写一个计时器,将计时结果显示出来
'''
'''
import time
for i in range(100):
	t = time.time()
	tl = time.localtime(t)
	ts = time.strftime("%Y-%m-%d %H:%M:%S",tl)
	time.sleep(1)
	print(ts, end='\r')
'''
'''
随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出
'''
'''
import random
h = random.randint(1,100)
print(h)
l = []
s = 0
l1 = ['二进制']
print(type(l))
for  i in range(7):
	if h > 0:
		s = h % 2
		h = h // 2
		l1.insert(0,s)
		print(l1)
'''
'''
用户任意输入他的生日，判断他输入00后，90后，还是80后
'''
'''
year = int(input("请输入出生年份"))
month = int(input("请输入出生月份"))
day = int(input("请输入出生日期"))
if year > 2000:
	print("你是00后")
elif year > 1990:
	print("你是90后")
elif year > 1980:
	print("你是80后")
else:
	print("没啥说的")
'''
'''
5.现在有一个列表，li = [1,2,3,'a','b','4','c'],有一个字典（此字典是
动态生成的，并不知道里面有多少键值对，所以用 dic = {} 模拟此字典 ）；
现在需要完成这样的操作：如果字典没有‘k1’这个键，那么就创建这个‘k1’这个键和
对应的值（该键值设为空列表），并将列表li中的索引位为奇数对应的元素，添加到‘k1’
这个键对应的值中
'''
'''
li = []
print(type(li))
li = [1,2,3,'a','b',4,'c']
o = print(li[1])
u = print(li[3])
y = print(li[5])
d = dict()
print(type(d))
t = input("请输入求得的字符串")
print("k1的对应值为",t)
'''
'''
6.组合嵌套题，有如下列表，按照要求实现每一个功能
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
<1> 将列表lis中的‘tt’变成大写（两种方式）
<2> 将列表lis中数字3变成字符串‘100’（两种方式）
<3>将列表中‘1’变成数字101（两种方式）
'''
'''
第一种
'''
'''
lil = []
print(type(lil))
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
print(lis)
print(lis[0])
lit =(lis[0])
lis.pop(0)
print(lit[1])
lip = (lit[1])
lit.pop(1)
print(lip[2])
lio =(lip[2])
lip.pop(2)
d = dict()
print(type(d))
d2 = lio
d2["k1"]="'TT',100,101"
print(d2)
lip.insert(2,d2)
print(lip)
lit.insert(1,lip)
print(lit)
lis.insert(0,lit)
print(lis)
'''
'''
第二种
'''
'''
lil = []
print(type(lil))
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
lip = [['k',['qwe',20,{'k1':['TT',100,'101']},89],'ab']]
lis = lip
print(lis)
'''
'''
7.请删除字典中的键'k5',如果不存在键'k5',则输出"对不起！不存在你要删除的元素"
'''
'''
d.pop('k5')
print(d.pop('k5','对不起!不存在你要删除的元素')
'''
'''
8.删除元祖中的所有重复的元素，并生成一个列表
'''
'''
q = (1,2,3,4,5,6,5,4,3,2,1)
w = set(q)
e = list(w)
print(type(e))
print(e)
'''
'''
4.总结整型、浮点、字符串、列表、元祖、字典、集合的常用方法，且比较各自擅长的领域
'''
'''
整型常常进行进制转换和数学运算
浮点通常进行数学运算
字符串通常被用来赋值,连接
列表是一个有序序列的集合,列表中的元素可以是任意类型,元素可进行增删改查
元祖一个不可变的有序序列,元祖是一旦初始化后，成员不能改变的序列,元祖内逗号才是元祖的符号,利用元祖实现两个数的交换,
字典是一个可变的无序的键值对组成的,有0个或多个(key, value)组成的无序序列,用空间换时间,占空间大,搜索快
集合是一个无序的可变序列,set 无序可变不重复,能够去重复
'''




