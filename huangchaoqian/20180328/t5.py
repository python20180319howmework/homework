#定义一个函数，判断用户输入的成绩所属于的等级
def grade():
	n=eval(input("please input score:"))
	if 90<=n<=100:
		print("A")
	elif 80<=n<90:
		print("B")
	elif 70<=n<80:
		print("C")
	elif 60<=n<70:
		print("D")
	elif 0<=n<60:
		print("E")
	else:
		print("error!")
grade()
