#1
from time import *
for i in range(100):
    print(strftime("\r%H:%M:%S",localtime(time())),end="")
sleep(1)
print("\n")
#2
import random
l=[]
i=0
num=random.randint(1,99)
print(num)
while(int(num/2)!=0):
     num1=num%2
     num=int(num/2)
    # print(num1)i
     l.append(num1)
l.append(1)
print(l)
l.reverse()
for i in l:
    print(i,end="")
    
print("\n")
#3
year =int(input("year"))
month =int(input("month"))
day =int(input("day"))
if year>=1980 and year<1990:
   print("80后")
if year>=1990 and year<2000:
   print("90后")
if year>=2000:
   print("00后")
#5
li=[1,2,3,'a','b','4','c']
dic={}
li1=[]
dic["k1"]=""
for i in range(len(li)):
#    print(i)
    if i%2!=0:
       li1.append(li[i])
dic["k1"]=li1
print(dic)
#6
lis=[['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
for value in lis[0][1][2].values():
    print(value[0].upper())
    value[1]="100"
    value[2]=101
   # print(value.get(3,"100"))
   # print(value.get("1",101))
#7
c={"k4":"li1","k5":"li2"}
#for key in c.keys():
if "k5" in c:
    c.pop("k5")
    print(c)
else:
     print("对不起")
     
#8
t=(1,'k',5,'k',4,6,5)
l=[]
#list(t))
for i in list(t):
    if i in l:
       continue
    else:
       l.append(i)
print(l)
