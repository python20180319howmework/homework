'''
计算l = ["172.16.3.1", “172.16.1.5”, “172.15.2.0”, “172.16.3.1”, “172.16.3.1”,
 “172.16.1.5”]
不需要定义函数，统计在此列表中每一个ip出现的次数，并输出出现频率最高的成员
'''
l=["172.16.3.1","172.16.1.5","172.15.2.0","172.16.3.1","172.16.3.1","172.16.1.5"]
s=set(l)
l1=list(s)
#print(l1)
for i in l1:
#	print(i,end="  :")
	a=l.count(i)
	print("{}的出现次数为{}".format(i,a))
maxl=l.count(l1[0])
maxi=l1[0]
for i in l1[1:]:
	if maxl<l.count(i):
		maxl=l.count(i)
		maxi=i
print("{}的出现频率最高，次数为{}".format(maxi,maxl))
