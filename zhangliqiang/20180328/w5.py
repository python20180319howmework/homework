


#5.定义一个函数，判断用户输入的成绩所属于的等级

def chengji(s):
	if  90 <= s <= 100: 
		print("A")
	if 80 <=  s <= 89:
		print("B")
	if 70 <= s <= 79:
		print("C")
	if 60 <= s <= 69:
		print("D")
	if  0 <= s <=59:
		print("E")




s = int(input("请输入成绩"))
z = chengji(s)

