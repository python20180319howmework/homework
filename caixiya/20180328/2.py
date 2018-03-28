'''
计算l = ["172.16.3.1", “172.16.1.5”, “172.15.2.0”, “172.16.3.1”, “172.16.3.1”, “172.16.1.5”]
不需要定义函数，统计在此列表中每一个ip出现的次数，并输出出现频率最高的成员'
l = ["172.16.3.1","172.16.1.5","172.15.2.0","172.16.3.1","172.16.3.1","172.16.1.5"]yy
dic={}
for i in range(len(l)):
	for j in l:
		if j not in dic:
			dic['j']='0'
print(dic)
'''
l = ["172.16.3.1","172.16.1.5","172.15.2.0","172.16.3.1","172.16.3.1","172.16.1.5"]
l1=[]
for i in l:
	if i not in l1:
		l1.append(i)
max1=l.count(l1[0])
n=0
for i in range(1,len(l1)):
	if l.count(l1[i])>max1:
		max1=l.count(l1[i])
		n=i
	else:
		max1=max1
		n=0
	
	print("{}出现的次数为{}".format(l[i],l.count(l1[i])))
print("{}出现的次数为{}".format(l[0],l.count(l1[0])))
print("{}输出出现频率最高是{}".format(l1[n],max1))
