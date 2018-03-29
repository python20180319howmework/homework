'''
定义一个函数，判断用户输入的成绩所属于的等级
   1) 90~100：A
   2) 80~89 :B
   3) 70~79:C
   4) 60~69:D
   5) 0~59:E 
'''
def grade(score):
	if 90<=score<=100:
		return "A"
	if 80<=score<=89:
		return "B"
	if 70<=score<=79:
		return "C"
	if 60<=score<=69:
		return "D"
	if 0<=score<=59:
		return "E"
score=eval(input("请输入成绩："))
print("{}所属的等级为{}".format(score,grade(score)))
