#请删除字典中的键'k5',如果不存在键'k5',则输出"对不起！不存在你要删除的元素"
dic={}
if dic.get("k5",0)=="k5":
	dic.pop("k5")	
else:
	print("对不起！不存在你要删除的元素")
