'''
5.定义一个函数，判断用户输入的成绩所属于的等级
   1) 90~100：A
   2) 80~89 :B
   3) 70~79:C
   4) 60~69:D
   5) 0~59:E 
'''
def qwe(fen):
	if 90 <= fen <=100:
		print("A")
	elif 80 <= fen <=89:
		print("B")
	elif 70 <= fen <=79:
		print("C")
	elif 60 <= fen <= 69:
		print("D")
	elif 0 <= fen <=59:
		print("E")

z = int(input("请输入数"))
qwe(z)
	





















