#3利用map()函数将用户输入的不规范的英文名字,变为首字母大写,其他字符小写的形式
#1) 假定用户输入的是["lambDA", “LILY”, “aliCe”]y

def daxiao(l):
	return l[0].upper() + l[1:].lower()
	
r = ["lambDA", "LILY", "aliCe"]
s = list(map(daxiao,r))
print(s)
