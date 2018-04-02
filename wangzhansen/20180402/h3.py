'''
3. 利用map()函数将用户输入的不规范的英文名字,变为首字母大写,其他字符小写的形式
   1) 假定用户输入的是["lambDA", “LILY”, “aliCe”]
'''
def suibian(s):
	s = str(s)
	for i in range(s):
		a = 0
		b = 0
		if 'A' <= s[0] <= 'Z'and 'a' <= s[i] <= 'z':
			return s
		else :
			a = s[0].upper
			b = s[:1].lower
			return a + b

s = "lambDA"
print(suibian(s)) 
			


















