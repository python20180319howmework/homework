'''
利用map()函数将用户输入的不规范的英文名字,变为首字母大写,其他字符小写的形式
   1) 假定用户输入的是["lambDA", “LILY”, “aliCe”]
'''

def sha(l):
	for i in l:
		return i[:1].upper()+l[1:].lower()

a = ["lambDA","LILY","aliCe"]
print(list(map(sha,a)))
