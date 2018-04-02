'''
利用map()函数将用户输入的不规范的英文名字,变为首字母大写,其他字符小写的形式
   1) 假定用户输入的是["lambDA", “LILY”, “aliCe”]
'''


def my_up(s):
	return s[0].upper()+s[1:].lower()


if __name__ == '__main__':
	
	f = map(my_up,["lambDA", "LILY", "aliCe"])
	print(list(f))
