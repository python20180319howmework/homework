#作业还没写完，先交这几题，其余等下我在看看今晚能不能写完。

#1.编写一个计时器,将计时结果显示出来
'''
import time

t = time.time()

for i in range(100):
	t1 = time.localtime(i)
	t2 = time.strftime("%S", t1)
	print(t2)        
	time.sleep(0.5)

'''

#2.随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出
'''
import random

a = random.randint(1, 100)
print("十进制为:",a)
print("二进制为:",bin(a))
'''

#7.请删除字典中的键'k5',如果不存在键'k5',则输出"对不起！不存在你要删除的元素"
'''
d = {"g1":"green","r1":"red","b1":"blue","b2":"black"}
print(d.pop("k5","对不起！不存在你要的元素"))
'''
#8.删除元祖中的所有重复的元素，并生成一个列表



b = (1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9)






























