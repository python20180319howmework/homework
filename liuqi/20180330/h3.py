"""
3. 编写一个函数:
   1)此函数可以传递任意一组键值对，函数将所有的键存放到一个列表中，返回
   2) 升级以上函数，使得用户必须有的键值为：name:"xxx"   city:"xxxx"
"""

def keys(mykey):
	
	l = []
	for i in mykey.keys():#遍历字典中的键
		l.append(i)
	return l

def stu(height,*,name,city):
		
	print("height",height,"name",name,"city",city)

if __name__ == "__main__":

	mydict = {"name":"李华","city":"北京","age":18,"weight":100,"height":180}
	print(keys(mydict))
	
	stu(189,name="小沈阳",city = "邢")
