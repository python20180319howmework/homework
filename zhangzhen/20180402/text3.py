'''
3. 利用map()函数将用户输入的不规范的英文名字,变为首字母大写,其他字符小写的形式
   1) 假定用户输入的是["lambDA", “LILY”, “aliCe”]
'''

def xiugai(x):
	return x[0].upper() +x[1:].lower()
r = map(xiugai,["lambDA","LILY","aliCe"])
l = list(r)
print(l)





