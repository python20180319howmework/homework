#利用reduce实现列表中元素求积i

from functools import reduce

r = reduce(lambda x, y : x * y,(1,2,3,4,5,6,7,8,9))
print(r)






