'''
2. d = {"name":"python", “age”:18, “fun”:"all"},生成一个列表["name=python",  “age=18”, “fun=all”]
'''
d={"name":"python","age":18,"fun":"all"}
#l=[(key,value) for key,value in d.items()]
l=[str(key)+"="+str(value) for key in d.keys() for value in d.values()]
print(l)
