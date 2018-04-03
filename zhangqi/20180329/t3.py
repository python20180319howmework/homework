#3. 编写一个函数:
 #  1)此函数可以传递任意一组键值对，函数将所有的键存放到一个列表中，返回
 #  2) 升级以上函数，使得用户必须有的键值为：name:"xxx"   city:"xxxx"
def dct1(*,kw,vlu,age):
	print("kw", kw, "vlu", vlu, "age", age)

def dct2(**kw):
	l = []
	for i in kw.key():
		l.append(i)
	return l

if __name__ == "__main__":
	dct2(kw = "name",vlu = "city", age = "age")
	dct1(dct2())

	
























