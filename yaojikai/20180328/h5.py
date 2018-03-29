
'''
5,定义一个函数，判断用户输入的成绩所属于的等级
1) 90~100：A
2) 80~89 :B
3) 70~79:C
4) 60~69:D
5) 0~59:E 
'''

def yjkpd(num):
	if 90 < num <= 100:
		print("A")
	elif 80 < num <= 90:
		print("B")
	elif 70 < num <= 80:
		print("C")
	elif 59 < num <= 70:
		print("D")
	elif 0 <= num <= 59:
		print("E")
	else:
		print("请输入正确的成绩！")


n = int(input("请输入成绩："))

yjkpd(n)




