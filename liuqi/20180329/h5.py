"""
5.定义一个函数，判断用户输入的成绩所属于的等级
   1) 90~100：A
   2) 80~89 :B
   3) 70~79:C
   4) 60~69:D
   5) 0~59:E 
"""
def judge(gra):
	
	if  90 <= gra <=100:
		return "A"
	elif 80 <= gra < 90:
		return "B"
	elif 70 <= gra < 80:
		return "C"
	elif 60 <= gra < 70:
		return "D"
	elif 0 <= gra < 60:
		return "E"
	else:
		return "输入错误！"

gra = int(input("请输入成绩："))
level = judge(gra)
print("你成绩的等级是：{}".format(level))
