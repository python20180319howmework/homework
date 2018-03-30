
import random
def cal(*arg,base = 4):
	sum1 = 0
	for i in arg:
		sum1+= i
	print(sum1* base)
l = []
for n in range(0,5):
	l.append(random.randint(0,10))
cal(l[0],l[1],l[2],l[3],l[4])

	
	
    























