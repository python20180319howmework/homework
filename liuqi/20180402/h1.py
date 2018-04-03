"""
1. 如果有两个字符串"hello" 和 “world”，
   生成一个列表，列表中元素["hw", "eo", "lr"]
"""
l = [i+j for i in "hello"for j in "world"]
print(l)
