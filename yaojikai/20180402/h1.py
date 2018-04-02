#1. 如果有两个字符串"hello" 和 “world”，生成一个列表，列表中元素["hw", "eo", "lr"]
str1 = "hello"
str2 = "world"
l = []
for i in range(len(str1)):
	l.append(str1[i]+str2[i])

print(l)

