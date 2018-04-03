'''
3. 利用map()函数将用户输入的不规范的英文名字,变为首字母大写,其他字符小写的形式
   1) 假定用户输入的是["lambDA", “LILY”, “aliCe”]
'''
l=["lambDA","LILY","aliCe"]
print(list(map([i[:1].upper()+i[1:].lower()for i in l,l])))	
