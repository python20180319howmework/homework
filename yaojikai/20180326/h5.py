#5
mystr = str(input("请输入字符串："))
DX = 0
XX = 0

for s in mystr:
	if ord('a')<= ord(s) <= ord('z'):
		XX+=1
		
for s in mystr:
	if ord('A') <= ord(s) <= ord('Z'):
		DX+=1


print("{}中有{}个大写{}个小写".format(mystr,DX,XX))





