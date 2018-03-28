
'''
请删除字典中的键'k5',如果不存在键'k5',则输出"对不起！不存在你要删除的元素"
'''
dic={}
num =dic.pop("k5",-1)
while num ==-1:
	print("对不起！不存在你要删除的元素")
	break
else:
	print("成功")
