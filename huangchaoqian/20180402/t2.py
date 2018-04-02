'''
d = {"name":"python", “age”:18, “fun”:"all"},生成一个列表["name=python",
  “age=18”, “fun=all”]
'''
d={"name":"python","age":"18","fun":"all"}
l1=list(d)
l2=list(d.values())
l=[]
for i in range(3):
	l.append(l1[i]+"="+l2[i])
print(l)
#for x,y in d.items():
#	print(x,y)


