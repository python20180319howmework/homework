'''
#1 编写一个计时器,将计时结果显示出来
import time 
for t in range(100):
	t=time.time()
	t1=time.localtime(t)
	t2=time.strftime("\r%Y-%M-%D %H:%M:%S",t1)
	time.sleep(1)
	print(t2,end=" ")
'''

'''
#2 随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出
import random
l=[]
n=random.randint(0,1000)
print(n)
for i in range(0,500):
	if n > 1:
		y = n%2
		n = n//2
		i=i+1
		l.insert(0,y)
else:
	l.insert(0,n)
print(l)

'''

'''
#3 用户任意输入他的生日，判断他输入00后，90后，还是80后

year=int(input("请输入你出生的年份"))
if 1980 <= year <=1989: 
print("你是80后")
elif 1990 <= year <= 1999:
print("你是90后")
elif 2000 <=year <=2099:
print("你是00后")
else:
print("你out了")


'''
#4请删除字典中的键'k5',如果不存在键'k5',则输出"对不起！不存在你要删除的元素"
dic={}

if dic.get("k5",0)=="k5":
	dic.pop("k5")	
else:
	print("对不起！不存在你要删除的元素")
'''

#5除元祖中的所有重复的元素，并生成一个列表
t=(5,"t",8,3,8,5,6,6,3,4,8,2,6,1)
'''
l=[]
for i in t:
	if t.count(i)>1:
		l.append(i)
print(l)
while 1:
	i=0
	if l.count(i)>1:
		l.remove(i)
		print(l)
'''
s=set(t)
l=list(s)
print(l)

'''




