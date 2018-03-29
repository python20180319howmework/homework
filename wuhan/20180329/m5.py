def mygrade(g):
	if  90<=g<=100:
		print("你的成绩等级是A")

	if   80<=g<=89:
		print("你的成绩等级是B")
	if   70<=g<=79:
		print("你的成绩等级是C")
	if  60<=g<=69:
		print("你的成绩等级是D")
	if  0<=g<=59:
		print("你的成绩等级是E")

if __name__=='__main__':
	a=int(input('请输入成绩：'))	
	mygrade(a)
