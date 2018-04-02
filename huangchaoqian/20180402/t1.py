#如果有两个字符串"hello" 和 “world”，生成一个列表，列表中元素["hw", "eo", "lr"]
l1=[x for x in "hello"]
l2=[x for x in "world"]
l=[]
for i in range(5):
	l.append(l1[i]+l2[i])


print(l[:3])	





