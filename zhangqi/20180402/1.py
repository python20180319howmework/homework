# 如果有两个字符串"hello"和"world",生成一个列表，列表中元素["hw","eo","lr","ll","od"]
mystr = "hello"
mystr1 = "world"
l = []
for i in range(len(mystr)):
	l.append(mystr[i]+mystr1[i])

print(l)






















