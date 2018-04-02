'''
4. 利用reduce实现列表中元素求积
'''
l1 = ['1','2','3','4']
l2 = [str(i) for i in l1]
l = ''.jion(l2)
print(reduce(lambda x,y :x * y , map( l)))




















