"""
1. 如果有两个字符串"hello" 和 “world”，
   生成一个列表，列表中元素["hw", "eo", "lr"]
"""
l = [i+j for i,j in zip("hello","world")]
print(l)


print("---------------------------")
l1 = [i for i in "hello"]
l2 = [j for j in "world"]
l3 =  []
for i in range(0,len(l1)):
	l3.append(l1[i]+l2[i])

print(l3)


