'''
2.计算l = ["172.16.3.1", “172.16.1.5”, “172.15.2.0”, “172.16.3.1”, “172.16.3.1”, “172.16.1.5”]
不需要定义函数，统计在此列表中每一个ip出现的次数，并输出出现频率最高的成员
'''
l = []
print(type(l))
l1 = ["172.16.3.1","172.16.1.5","172.15.2.0","172.16.3.1","172.16.3.1","172.16.1.5"]
q = 0
p = 1
for i in range(1,6):
	if l1[0] == l1[i - q]:
		l1.pop(i - q )
		q += 1
		p += 1
z = p
print(z)
print(l1[0])
l1.pop(0)
print(l1)
r = 0
e = 1
for i in range(1,3):
	if l1[0] == l1[i - r]:
		l1.pop(i -r)
		r += 1
		e += 1
w = e
print(w)
print(l1[0])
l1.pop(0)
print(l1)
























