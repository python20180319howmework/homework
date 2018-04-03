#d={name":"python", “age”:18, “fun”:"all"},生成一个列表["name=python",  “age=18”, “fun=all”]


l = []

mydic = {"name":"python","age":18,"fun":"all"}
for k,v in mydic.items():
	l.append(str(k)+"="+str(v))
print(l)



