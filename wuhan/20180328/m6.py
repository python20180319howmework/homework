
dic = {"k5":"red","k4":"blue"}
if dic.__contains__('k5'):
    dic.pop('k5')
else:
    print("对不起！不存在你要删除的元素")
print(dic)
