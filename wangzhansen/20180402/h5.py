'''
使用filter筛选序列中所有回文数,假定序列是[132, 12321, 11, 9989, 666]
'''


def hui(x):
	flag = True
	l = str(x)
	for i in range(len(l)):
		if l[i] != l[len(l)-i-1]:
			flag = False
	return flag



if __name__ == '__main__':
	

	s = filter(hui,[132, 12321, 11, 9989, 666])
	print("回文数为:{}".format(list(s)))




















