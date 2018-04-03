
#2. d = {"name":"python", “age”:18, “fun”:"all"},生成一个列表["name=python",  “age=18”, “fun=all”]

d = {"name":"python","age":18,"fun" :"all"}
'''
for k,v in d.items() :
	print(str(k)+"="+str(v))
'''
print(list(str(k)+"="+str(v) for k,v in d.items()))



