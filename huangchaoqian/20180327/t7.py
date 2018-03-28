#删除元祖中的所有重复的元素，并生成一个列表
t=(5,"t",8,3,8,5,6,6,3,4,8,2,6,1)
'''
l=[]
for i in t:
	if t.count(i)>1:
		l.append(i)
print(l)
while 1:
	i=0
	if l.count(i)>1:
		l.remove(i)
		print(l)
'''
s=set(t)
l=list(s)
print(l)
