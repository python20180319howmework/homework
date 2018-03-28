总结整型、浮点、字符串、列表、元祖、字典、集合的常用方法，且比较各自擅长的领域
整型：可进行加减乘除，使用方便
hex(num)
print(h)

o = oct(num)
print(o)

print(abs(-100))

a, b = 10, 90
max2num = max(a, b, 100, 40, 178, 2)
print(max2num)

c = 2
print(pow(a, c)) # a ** c
print(pow(a, c, 3)) #a ** c % 3

python对于数据运算专门提供了数学库（math）,所谓库称为模块
如果我们要使用ptyhon所提供的库，有以下方法
	import math
		math.fabs()
	from math import *
		fabs()
	from math import fabs, xxx

from math import *

ceil_floorn = 1.93
print(ceil(ceil_floorn))
print(floor(ceil_floorn))


n = True
# 获得变量类型
print(type(n))
print(type(num))
print(isinstance(n, int))  #bool属于int

# 运算符

a, b = 10, 15

print(b / a)
print(b // a)


print(a > b and b) # “短路逻辑”
print(a < b and b) # a < b为真,and表达式的值取决于b

print(a or b) 
print(not a or b) 

print(a ** b) #pow(a, b)

a += b # a = a + b
print(a, b)

# 以下两种方式 效果一样的
print(2< a < 15)
print(a > 2 and a < 15)

#b = a
b = 25
c = 25
print(a is b)
print(b is not c)

浮点：#num = 1.2  #浮点 100.2==>1.002 * 10^2===>1.002e2m = 1.2  
# 浮点
myfloat = 1.2345
print("{0:.2f}".format(myfloat))
print("{0:.2}".format("hello"))
字符串：# 字符串: ""/ ''由一个或多个字符组成的

name = "caohuan" # unicode
school = 'hua\
dian'
item = '''计算机科学
与技术系'''  

专业 = "软件工程" #不建议

print(name, school, item, 专业)

# 字符串中每一个字符的索引从0开始
stu = "么济恺希雅abc"

# stu[start:end:step]
print("****************************")
print(stu)
print("{}".format(stu[0:]))
print("{}".format(stu[0::3]))
print("{}".format(stu[-1:0:-3]))
print("****************************")

print("{}大人,好好学习".format(stu[0]))
print("{}同志，辛苦了".format(stu[1:]))
print("{}好同学哈哈，你是最帅的".format(stu[1:-3])) #在序列中[a, b]  a<= <b
print("{}同志，辛苦了".format(stu[5::-3])) #在序列中[a, b]  a[5] 从a[5]倒叙数到-3
print("{}同志，辛苦了".format(stu[-1]))

#stu[2] = "欢" 字符串是个常量，不能改变

# 与字符串相关联的运算符
statement = "python"

stu += statement
print(stu)
print(stu+statement)  #连接
print(10 * statement)  #复制
statement *= 5
print(statement)  

# BIF
print(len(statement))

s2 = statement.upper() #大写
print(s2, statement)

print(s2.lower()) #小写

stringS1 = "大家好 我是reala 我最爱语言就是    python"
print(stringS1.split())
print(stringS1.split(sep="是"))  #分割字符串， sep指明分隔符

#format方法
mystrf = "学好Python"
fstr = "改变世界"
print("{},你就能{}".format(mystrf, fstr)) #{}槽
print("{1},你就能{0}".format(mystrf, fstr)) #{}槽

# "学好Python          "
print("{0:20}".format(mystrf))  #左对齐
print("{0:>20}".format(mystrf)) #右对齐
print("{0:^20}".format(mystrf)) #居中对齐
print("{0:*^20}".format(mystrf)) #居中对齐，并补*
print("{0:+^20}".format(mystrf))
列表：列表是一个有序序列的集合
列表中的元素可以是任意类型
元素可进行增删改查
 
# 列表的定义
l = []
print(type(l))
l1 = ['lucy', 'lilei', 'hanmeimei']
print(l1)

# 迭代列表
for i in l1:
	print(i)

# 末尾增
l1.append(100)
print(l1)
l1.append(['小胖', '可爱'])
print(l1)

print("{:-^20}".format("查找"))
# 查 列表的索引从0开始的
print(l1[4][0])
print(l1[2])

print("{:-^20}".format("增加"))
# 任意位置增
l1.insert(1, '永鹏')
print(l1)

print("{:-^20}".format("修改"))
# 改
l1[1] = '曹欢'
print(l1)

print("{:-^20}".format("删除"))
# 删
l1.pop() #末尾删除
print(l1)
l1.pop(2) #指定位置删除
print(l1)
l1.remove(100)
print(l1)

print("\n{:-^20}".format("list"))
l2 = list()
print(type(l2))
l2 = list((2, 3))
print(l2)

元祖：元祖一个不可变的有序序列
#建议使用中，如果能用tuple替换list，则替换，以保证数据安全

# tuple :元祖是一旦初始化后，成员不能改变的序列
t = tuple()
print(type(t))
l = [1, "你好", 100]
t2 = tuple(l)
print(t2)

# 空元祖
t3 = ()
print(type(t3))

# t4 = (1)  t4是一个整型
# 元祖内,号才是元祖的符号
t4 = (1,)
print(type(t4))

# 利用元祖实现两个数的交换
a = 100
b = 200
a, b = b, a #(200, 100)
print(a, b)

#
tnew = (1, 2, 3, 2, 1, 7, 9, 2, 1)
print(tnew.count(1)) #统计元祖tnew中所有1的个数
print(tnew.index(2, 1, 5)) #得到从下标1到下标5第一次出现值2的索引
#tnew[1] = 100 元祖是不可变的
字典：字典是一个可变的无序的键值对组成的


# 字典(dict)：有0个或多个(key, value)组成的无序序列

# 空字典
d = dict()
print(type(d))

d2 = {"前景色":"red", "背景色":"blue"}
print(d2)

# 查 字典无序，所以无index
print(d2["前景色"])

print("{:#^10}".format("key"))
# 获得字典中所有的key
for key in d2.keys():
	print(key)
	print(d2[key])

print("{:#^10}".format("value"))
for value in d2.values():
	print(value)

print("{:#^10}".format("item"))
for item in d2.items():
	print(item)


# 改
d2["前景色"] = "yellow"
print(d2)

# 增
d2["字体颜色"] = "purple"
print(d2)

print("{:#^20}".format("delete"))
# 删除
d2.pop("前景色")
print(d2)

print(d2.pop("新颜色", -10))
print(d2)

# 检验字典中是否含有某一个key
print("python" in d2)
print("背景色" in d2)

print(d2.get("python", -1))
print(d2.get("背景色", -1)) #如果字典中有key“背景色”则返回对应的value，如果没有返回-1,默认返回None


# 注意：字典中的Key一定是不可变对象(整型数，浮点数，元祖，字符串) value 没要求

#key = [1,2]
key = (1,2)
d2[key] = [11,22,33] 
print(d2)
d2[3] = "test"
d2[5.8] = "test2"
print(d2)

num = 10
d2[num] = "integer"
print(d2)

num = 20
print(d2)

集合：集合是一个无序的可变序列


# set 无序可变不重复

# 去重复
s = set([1,2,2,3,4,5,7,6,5,4,3,2])
print(s)

# 增
s.add(100)
print(s)

# 删
s.pop()
print(s)

s.remove(3)
print(s)

s2 = {10, 19, 5, 7, 4, 20, 25}
print(s, s2)
print(s2.difference(s))


