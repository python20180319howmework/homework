#1，
TZ = float(input("请输入你的体重："))
SG = float(input("请输入你的身高："))
BMI = TZ/(SG*SG)
if BMI < 18.5:
	print("你这么瘦，可以肆无忌惮的大吃大喝啦！")
elif 18.5 <= BMI < 25:
	print("兄弟！你离模特就差八块腹肌了！")
elif 25 <= BMI < 30:
	print("控制你自己哦！脂肪有点多啦！")
elif BMI >= 30:
	print("不能再吃了！跑几圈去吧，你也可以是男神！")





