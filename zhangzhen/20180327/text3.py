
'''3. 输入一个三位整型数，判断它是否是一个水仙花数(比如153 = 1*1*1 + 5*5*5 + 3*3*3)
    计算出有多少个水仙花数
'''
num = int(input("请输入一个三位整型数字："))
n3 = num % 10
n2 = num /10 % 10
n1 = num /100 % 10 
if num ==n1*n1*n1+ n2*n2*n2 + n3*n3*n3 :
	print ("它是一个水仙花数")	
else:
	print("它不是一个水仙花数")
con = 0 
for i in range(100,1000):
	i3 = i % 10
	i2 = i//10 % 10
	i1 = i//100 % 10 
	if i == i1*i1*i1+ i2*i2*i2+ i3*i3*i3:
		con = con + 1
	else:
		continue
print(con)





































