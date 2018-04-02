'''
1)此函数可以传递任意一组键值对，函数将所有的键存放到一个列表中，返回
2) 升级以上函数，使得用户必须有的键值为：name:"xxx"   city:"xxxx"
'''
def jianzhi(**m):
	l=[]
	for key in m.keys():
		l.append(key)
	return l
def jianzhi2(xingbie,*,name,city):
	print("xingbie:",xingbie,"name:",name,"city:",city)	

if __name__=="__main__":
	print(jianzhi(k=130,j=12,f=456))
	jianzhi2("男",name="黄永鹏",city="beijing")



