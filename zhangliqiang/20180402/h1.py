

#1. 如果有两个字符串"hello" 和 “world”，生成一个列表，列表中元素["hw", "eo", "lr"]

s1 = "hello"
s2 = "world"
c1 = []
c2 = []
c3 = []
for l1 in s1:
	 c1.append(l1)
	
	
for l2 in s2:
	c2.append(l2)
for i  in range(5):
	c3.append(c1[i]+c2[i])
	


print(c3)
#print(["hello","world"] for i in range (5))
