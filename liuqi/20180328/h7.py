"""
7.请删除字典中的键'k5',如果不存在键'k5'
  则输出"对不起！不存在你要删除的元素"
"""
dirs = {}
a = print(dirs.get("k5",-1))
if a == -1:
	print(dirs.pop("k5"))
else:
	print("对不起！不存在你要删除的元素！")
