'''
利用map()函数将用户输入的不规范的英文名字,变为首字母大写,其他字符小写的形式
   1) 假定用户输入的是["lambDA", “LILY”, “aliCe”]
'''
def mychar(s):
	return s[0].upper()+s[1:].lower()
print(list(map(mychar,["lambDA","LILY","aliCe"])))
	


