'''
利用reduce实现列表中元素求积
'''
from functools import reduce


def my_add(l):
	print(reduce(lambda x,y : x * y,l ))


if __name__ == '__main__':
	

	my_add([1,2,3,4])
