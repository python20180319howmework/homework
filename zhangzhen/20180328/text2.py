'''
计算l = ["172.16.3.1", “172.16.1.5”, “172.15.2.0”, “172.16.3.1”, “172.16.3.1”, “172.16.1.5”]
不需要定义函数，统计在此列表中每一个ip出现的次数，并输出出现频率最高的成员
'''
'''
l = ["172.16.3.1", "172.16.1.5", "172.15.2.0", "172.16.3.1", "172.16.3.1", "172.16.1.5"]
l1 = []

for i in range(0,5):
	l1.append(l.count(l[i]))
	print(l.count(l[i]))
if 	l1[i]== max(l1):
	print("频率最高的是{}，总计{}次".format(l[i],l1[i]))


#ip做key  用字典的话 最后打印的是  ××出现了多少次
'''
l = ["172.16.3.1", "172.16.1.5", "172.15.2.0", "172.16.3.1", "172.16.3.1", "172.16.1.5"]
#集合去重复
s = set()
ls = list(s)#ls 列表中的所有的元素不重复
#定义一个字典
d = dict()
for i in ls:
	n = ls.count(i)# 用n 储存一下次数
	d[i] = n 
print(d)
res = []
print(d.keys()# 打印出来的是列表
max_cnt = -1#没有-1 
for k in d.keys():
	if d[k] == max_cnt:
		res.append(k)
	elif d[k]> max_cnt:
		res = []
		res.append(k)
		max_cnt = d[k]
print(res) 
