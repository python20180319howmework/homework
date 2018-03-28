#1.编写一个计时器，将计时结故果显示出来
import time
for i in range(100):
   print(time.strftime("\r%Y-%m-%d %H:%M:%S",time.localtime(time.time())),end="")
   time.sleep(1)

#2.二进制表达
import random 
num=random.randint(1,10)
print(num)
l=[]
while (int(num/2)!=0):
   n=num%2
   num=num//2
   l.append(n)
l.append(1)
l1=list(reversed(l))
print(l1)
#3.
year=int(input("请输入年："))
month=int(input("请输入月："))
day=int(input("请输入日："))
if(2000<year):
  print("00后")
if(1990<=year<2000):
  print("90后")
else:
  print("80后")
'''
#4.
整型：abs(),max(),min(),pow(),bin(),oct(),hex()
浮点：hex()
字符串："" ''\ str[start:end:step] + * upper() lower() split() format() > < ^  *^ :.2f :b :d :o :x :X  
列表：[] append() insert() l[0] l[1]="123" pop()末刪 pop(2)指定位置刪       remove(100)刪除此值
元祖：, 交換 count() index(value,star,stop)
字典：{key:value}  直接給key賦值修改value   直接新增key及對應value pop(key) pop(key,-1) key in dict dict.get(key,-1) key是不可變對象
集合：set() add() pop()前刪 remove(value) difference()
'''
#5.
li=[1,2,3,'a','b','4','c']
dic={}
if("k1" not in dic.keys()):
   dic["k1"]=l
   l=[]
for i in li:
   for index(i)%2!=0:
      l.append(i) 
print(dic["k1"])
#6.
lis=[['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
for value in lis[0][1][2].values():
     print(value[0].upper())
     print(value[1]="100")
     print(value[2]=101)
#7.
dic=dict(input("輸入字典："))
if "k5" in dic.keys():
   dic.pop("k5")
else:
   print("对不起！不存在你要删除的元素")
#8.
t=tuple(input("输入元祖"))
print(t)
l=list(tuple.set(t))
print(l)
