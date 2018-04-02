'''
1. 编写一个函数：
   1) 计算所有参数的和的基数倍(默认基数为base=3)
'''

def heji(l):
	l = type
	e = 0
	r = 0
	i = 0
	while i > len(l):
		e = l[i]
		r += e
		i += 1
	return r*3

if __name__ == "__main__":
	l = eval(input("请输入几个数字"))
	print(heji(l))

























