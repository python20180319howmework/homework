
'''
2.计算l = ["172.16.3.1", “172.16.1.5”, “172.15.2.0”, “172.16.3.1”, “172.16.3.1”, “172.16.1.5”]
不需要定义函数，统计在此列表中每一个ip出现的次数，并输出出现频率最高的成员
'''
l=['172.16.3.1','172,16.1.5','172.15.2.0','172.16.3.1','172.16.3.1','172.16.1.5']
dic={}
count=0
count1=0
count2=0
for i in range(6):
	dic[i]=l[i]
	
print(dic)
for  value in dic.values():
	if value=='172.16.3.1':
		count+=1
	elif value=='172.16.1.5':
		count1+=1
	else :
		count2+=1
print("'172.16.3.1'的次数是{}'172.16.1.5'的次数是{}'17215.2.0'的次数是{}".format(count,count1,count2))

tu=tuple(l)
a=tu.count('172.16.3.1')
b=tu.count('172.16.1.5')
c=tu.count('172.15.2.0')
if a>b:
	if a>c:
		print("172.16.3.1")
	else:
		print("172.15.2.0")
else:
	if b>c:
		print("172.16.1.5")
	else :
		print("172.15.2.0")
