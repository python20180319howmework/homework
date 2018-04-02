#3. 利用map()函数将用户输入的不规范的英文名字,变为首字母大写,其他字符小写的形式
#   1) 假定用户输入的是["lambDA", “LILY”, “aliCe”]
def myf(a):
	for i in a:
		return a[:1].upper()+a[1:].lower()
l = ["lambDA","LILY","aliCe"]
l1 =list(map(myf,["lambDA","LILY","aliCe"]))
print(l1)




















