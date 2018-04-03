
#4. 利用reduce实现列表中元素求积


from functools import reduce
k = eval(input("请输入列表中的元素："))   #eval识别将输入的元素记到一个元组中
#print(type(k))
l = list(k)    #将元组转换为列表
r = reduce(lambda x, y : x * y,l)     #  利用reduce求所有元素的积
print("{}的所有元素的积为{}".format(l,r))



