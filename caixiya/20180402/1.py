'''
1. 如果有两个字符串"hello" 和 “world”，生成一个列表，列表中元素["hw", "eo", "lr"]
'''
str1="hello"
str2="world"
l=[x+y for x in str1 for y in str2]
print(l)
