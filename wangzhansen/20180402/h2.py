'''
2. d = {"name":"python", “age”:18, “fun”:"all"},生成一个列表["name=python",  “age=18”, “fun=all”]

'''
d =  {"name":"python","age":"18","fun":"all"}
l = list(d.keys())
print(l)
h = list(d.values())
print(h)
s = (x + "=" + y for x,y in  (list(l),list(h)))
print(s)














