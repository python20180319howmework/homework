
'''

 有这样一个字典d = {"chaoqian":87, “caoxu”:90, “caohuan”:98, “wuhan”:82, “zhijia”:89}
   1)将以上字典按成绩排名 
'''


d={'chaoqian':87,'caoxu':90,'caohuan':98,'wuhan':82,'zhijia':89}
l=[]
l3=[]
d2=dict()
for value in d.values():
	l.append(value)
l2=sorted(l,reverse=True)
for i in l2:
	for j in d.keys():
		if d[j]==i:
			l3.append(j)
for i in range(len(l3)):
	d2[l3[i]]=l2[i]
print(d2)

