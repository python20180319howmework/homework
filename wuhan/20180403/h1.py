'''
如果有两个字符串"hello" 和 “world”，生成一个列表，列表中元素["hw", "eo", "lr"]
'''

m = 'hello'
n = 'world'
s = []
for i in range(len(m)):
	s.append(m[i]+n[i])

print(s)
