import random
l=[]
for i in range(10):
	l.append(random.randint(0,100))
print(l)
for j in range(9):
	for k in range(10-j-1):
		if l[k]>l[k+1]:
			l[k],l[k+1]=l[k+1],l[k]
print(l)
