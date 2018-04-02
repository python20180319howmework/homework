'''
如果有两个字符串"hello" 和 “world”，生成一个列表，列表中元素["hw", "eo", "lr"]
'''


s = [i+j for i,j in zip('hello','world')]

print(s)
