
#5. 使用filter筛选序列中所有回文数,假定序列是[132, 12321, 11, 9989, 666]
#第一种方法：
def hw(n):
	res = 0
	s = n
	while n > 0:
		res = res * 10 + n % 10 
		n //= 10
	if s == res:
		return 1
	else:
		return 0

f = filter(hw,[132,12321,11,9989,666])
print("回文整形数有：",list(f))



#第二种方法：
def huiwen(n):
    return n == n[::-1]

f = filter(huiwen,["132","12321","11","9989","666"])
print("回文整形数有：",list(f))


