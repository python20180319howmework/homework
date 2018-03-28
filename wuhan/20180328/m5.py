
li = [1,2,3,'a','b','4','c']
dic = {}
if dic.__contains__('k1') == False:
	dic["k1"]='{},{},{}'.format(li[1],li[3],li[5])

print(dic)
