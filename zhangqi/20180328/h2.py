
#2.计算l = ["172.16.3.1", “172.16.1.5”, “172.15.2.0”, “172.16.3.1”, “172.16.3.1”, “172.16.1.5”]
#不需要定义函数，统计在此列表中每一个ip出现的次数，并输出出现频率最高的成员


l = ["172.16.3.1","172.16.1.5","172.1..2.0","172.16.3.1","172.16.3.1","172.16.1.5"]
t = []
for i in range(5):
	t.append(l.count(l[i]))
	print(l.count(l[i]))
if t[i]== max(t):
	print("列表中出现频率的最高的是{},共{}次".format(l[i],t[i]))












