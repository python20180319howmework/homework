

#4. 利用reduce实现列表中元素求积


from functools import reduce
r = reduce(lambda x, y : x * y, (1,3,5))
print(r)
