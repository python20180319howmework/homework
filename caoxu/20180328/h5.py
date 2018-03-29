'''定义一个函数，判断用户输入的成绩所属于的等级
   1) 90~100：A
   2) 80~89 :B
   3) 70~79:C
   4) 60~69:D
   5) 0~59:E'''

 
def gra(g):
	if 0 <= g <= 59:
		return 'E'
	elif 60 <= g <= 69:
		return 'D'
	elif 70 <= g <= 79:
		return 'C'
	elif 80 <= g <= 89:
		return 'B'
	elif 90 <= g <= 100:
		return 'A'


if __name__ == '__main__':
	s = int(input("输入成绩:"))
	print("你的成绩属于{}等级".format(gra(s)))
