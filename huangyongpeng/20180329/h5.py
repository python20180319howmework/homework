
'''
.定义一个函数，判断用户输入的成绩所属于的等级
   1) 90~100：A
   2) 80~89 :B
   3) 70~79:C
   4) 60~69:D
   5) 0~59:E 
'''
def dengji(m):
	if  90<=m<=100:
		print("你的成绩是A")

	if   80<=m<=89:
		print("你的成绩是B")
	if   70<=m<=79:
		print("你的成绩是c")
	if  60<=m<=69:
		print("你的成绩是D")
	if  0<=m<=59:
		print("你的成绩是E")





if __name__=='__main__':
	a=int(input('请输入成绩：'))	
	dengji(a)




