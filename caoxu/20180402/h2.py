'''
d = {"name":"python", “age”:18, “fun”:"all"},生成一个列表["name=python",  “age=18”, “fun=all”]
'''

d = {"name":"python", "age":18, "fun":"all"}

l = [str(key)+"="+str(value) for key,value in d.items()]

print(l)
