
m = float (input("请输入身高（m）"))
k = float(input("请输入体重(kg)"))
m =  m ** 2
BMI = k / m
if BMI < 18.5:
	print("{:.2f} 你这么瘦，可以肆无忌惮的大吃大喝啦".format(BMI))
elif 18.5 <= BMI < 25:
	print("{:.2f} 兄弟！你立模特就差八块腹肌了".format(BMI))
elif 25 <= BMI < 30:
	print("%s 控制你自己哦！脂肪有点多啦" % BMI)
elif BMI >= 30:
	print("%s 不能再吃了！跑几圈去吧，你也可以是男神" % BMI)










