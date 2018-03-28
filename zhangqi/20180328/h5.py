#5.定义一个函数，判断用户输入的成绩所属于的等级
 #  1) 90~100：A
  # 2) 80~89 :B
 #  3) 70~79:C
 #  4) 60~69:D
#   5) 0~59:E 
def grade(a):
	if  90<= a <= 100:
		print("A")
	elif 80<= a <= 89:
		print("B")
	elif 70<= a <= 79:
		print("C")
	elif 60<= a <= 69:
		print("D")
	else:
		print("E")
b = eval(input("请输入成绩"))
grade(b)





























