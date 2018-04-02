#2. d = {"name":"python", “age”:18, “fun”:"all"},生成一个列表["name=python",  “age=18”, “fun=all”]


d = {"name":"python", "age":18, "fun":"all"}
l = []
for key, value in d.items():

	l.append(str(key) + "=" + str(value))
print(l)






