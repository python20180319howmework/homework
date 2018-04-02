
'''
如果有两个字符串"hello" 和 “world”，生成一个列表，列表中元素["hw", "eo", "lr"]
'''

l=[i for i in 'hello' ]
l1=[i for i in 'world']
l3=[]
for i in range(5):
	l3.append(l[i]+l1[i])
print(l3[:3])
