'''
利用reduce实现列表中元素求积
'''
from functools import reduce
k = eval(input("输入列表中的元素：")) 
l = list(k)   
r = reduce(lambda x, y : x * y,l) 
print(r)

