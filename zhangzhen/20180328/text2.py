'''
计算l = ["172.16.3.1", “172.16.1.5”, “172.15.2.0”, “172.16.3.1”, “172.16.3.1”, “172.16.1.5”]
不需要定义函数，统计在此列表中每一个ip出现的次数，并输出出现频率最高的成员
'''
l = ["172.16.3.1", "172.16.1.5", "172.15.2.0", "172.16.3.1", "172.16.3.1", "172.16.1.5"]
l1 = []

for i in range(0,5):
	l1.append(l.count(l[i]))
	print(l.count(l[i]))
if 	l1[i]== max(l1):
	print("频率最高的是{}，总计{}次".format(l[i],l1[i]))
