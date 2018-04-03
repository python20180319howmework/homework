"""
2. d = {"name":"python", “age”:18, “fun”:"all"},
   生成一个列表["name=python",  “age=18”, “fun=all”]
"""
d = {"name":"python", "age":18, "fun":"alll"}

l = []

for k,v in d.items():
	l.append(str(k) + "=" + str(v) )

print(l)
