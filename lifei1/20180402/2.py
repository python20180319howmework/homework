d={"name":"python","age":"18","hun":"all"}
l1=list(d)
l2=list(d.values())
l=[]
for i in range(3):
	l.append(l1[i]+"="+l2[i])
print(l)
