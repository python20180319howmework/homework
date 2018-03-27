#7,请删除字典中的键'k5',如果不存在键'k5',则输出"对不起！不存在你要删除的元素"
dic = {  }

num = 0

for key in dic.keys():
	num += 1

if num >= 5:
	dic.pop(k5)
else   :
	print("对不起！不存在你要删除的元素。")


