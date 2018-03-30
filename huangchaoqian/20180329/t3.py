'''
编写一个函数:
   1)此函数可以传递任意一组键值对，函数将所有的键存放到一个列表中，返回
   2) 升级以上函数，使得用户必须有的键值为：name:"xxx"   city:"xxxx"
'''
def dic(**kw):
	print("kw",kw)
	l=[]
	for i in kw.keys():
		l.append(i)
	print(l)
	
if __name__=="__main__":
#	name=input("name:")
	dic(name="huang",city="hubei")
	


