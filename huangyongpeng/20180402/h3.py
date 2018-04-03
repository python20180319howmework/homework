
'''

利用map()函数将用户输入的不规范的英文名字,变为首字母大写,其他字符小写的形式
 1) 假定用户输入的是["lambDA", “LILY”, “aliCe”]

'''
l=['lambDA','LILY','aliCe']
l1=[]
def hy(m):
	return m.title()
r=map( hy,l)
for i in r:
	l1.append(i)
print(l1)



