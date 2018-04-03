'''
有这样一个字典d = {"chaoqian":87, “caoxu”:90, “caohuan”:98, “wuhan”:82, “zhijia”:89}
   1)将以上字典按成绩排
'''
d={"chaooqian":87,"caoxu":90,"caohuan":98,"wuhan":82,"zhijia":89}
l=[]
for v in d.values():
#	print(v)
	l.append(v)
print(l)
m=sorted(l)
l2=[]
for i in m:
	for y in d.keys():
		if d[y]==i:
			l2.append(y)
			break
print(l2)
dic={}
for i in range(len(l)):
	dic[l2[i]]=m[i]
print(dic)
