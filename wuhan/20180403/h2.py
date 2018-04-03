'''
 d = {"name":"python", “age”:18, “fun”:"all"},生成一个列表["name=python",  “age=18”, “fun=all”]
'''

d = {"name":"python","age":18,"fun":"all"}
l=[]
l1=[]
l2=[]
for item in d:
	l.append(item)
	l1.append(d[item])
for i in range(len(l)):
	l2.append(str(l[i])+ '='+str(l1[i]))
print(l2)
