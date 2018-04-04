'''
5.定义一个函数，判断用户输入的成绩所属于的等级
   1) 90~100：A
   2) 80~89 :B
   3) 70~79:C
   4) 60~69:D
   5) 0~59:E 
'''

score = int(input("请输入您的成绩："))

def dengji(score):
	if score >= 90 and score <= 100:
		print("您的等级是：A")
		
	elif score >= 80 and score < 90:
		print("您的等级是：B")
		
	elif score >=70 and score < 80:
		print("您的等级是：C")
		
	elif score >= 60 and score < 70:
		print("您的等级是：D")
		
	else :
		print("您的等级是：E")
	return score

print(dengji(score))

'''
或者 
def get_level(grade)
	level = ["E","E","E","E","E","E","D","C","B","A","A"]
	return leve[gread//10]     # / 表示浮点
if __name__"__main__":
	yougrade = int(input("请输入你的成绩："))
	print(get_leve(yougrade))
