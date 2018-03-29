

#3. 编写一个函数:
#   1)此函数可以传递任意一组键值对，函数将所有的键存放到一个列表中，返回
#   2) 升级以上函数，使得用户必须有的键值为：name:"xxx"   city:"xxxx"
def student(a):
	l = []
	for key in a.keys():
		l.append(key)
	return l
def student2(height,*,name,city):
	print("height",height,"name",name,"city",city)
if __name__=='__main__':
	a = eval(input("请输入剪子对"))
	print(student(a))
	student2(189,name="小沈阳",city = "邢台")
