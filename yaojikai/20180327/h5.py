'''
现在有一个列表，li = [1,2,3,'a','b','4','c'],有一个字典（此字典是动态生成的，并不知道里面有多少键值对，所以用 dic = {} 模拟此字典 ）；现在需要完成这样的操作：如果字典没有‘k1’这个键，那么就创建这个‘k1’这个键和对应的值（该键值设为空列表），并将列表li中的索引位为奇数对应的元素，添加到‘k1’这个键对应的值中
'''
li = [1,2,3,'a','b','4','c']

dic = {}

l2 = []

if dic.get('k1',-1) == -1:
	dic['k1'] = ''

for i in range(len(li)):
	if i % 2 != 0 :
		l2.append(li[i])

dic['k1'] = l2

print(dic)








print()