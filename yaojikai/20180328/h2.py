'''
2.计算l = ["172.16.3.1", “172.16.1.5”, “172.15.2.0”, “172.16.3.1”, “172.16.3.1”, “172.16.1.5”]不需要定义函数，统计在此列表中每一个ip出现的次数，并输出出现频率最高的成员

'''

l = ["172.16.3.1","172.16.105","172.15.2.0","172.16.3.1","172.16.3.1"]
d = []


for i in range(0,5):   #运用count将每个元素出现的次数添加到一个新的列表
	d.append(int(l.count(l[i])))

if d[i] == max(d):   #找到出现频率最多的索引值，输出元列表中对应的 ip
	print("{}出现的次数最多,出现了{}次".format(l[i],max(d)))
#print(l)
#print(d)



