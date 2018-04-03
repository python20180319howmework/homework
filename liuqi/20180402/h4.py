"""
4. 利用reduce实现列表中元素求积
"""

from functools import reduce
	
l = [1,2,3]


r = reduce(lambda x , y :x*y,l)
print("列表中元素求积为：{}".format(r))
