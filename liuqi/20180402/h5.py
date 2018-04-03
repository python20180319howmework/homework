"""
5. 使用filter筛选序列中所有回文数,
   假定序列是[132, 12321, 11, 9989, 666]
"""

l = [132,12321,11,9989,666]


def huiwen(n):
	n = str(n)
	return n == n[::-1]

f = filter(huiwen,l)

print(list(f))

