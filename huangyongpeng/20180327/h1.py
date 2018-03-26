from math import *
tizhong = int(input("输入体重："))
shengao = int(input("输入身高："))
BMI=tizhong/shengao*shengao
if BMI < 18.5:
	print("你这么瘦，可以肆无忌惮的大吃大喝啦")
	
elif 18.5<= BMI and BMI< 25:
	print("兄弟！你离模特就差八块腹肌了")
	
elif 25<=BMI<30:
	print("控制你自己哦！脂肪有点多啦！")
	
else:
	print("不能再吃了！跑几圈去吧，你也可以是男神")


