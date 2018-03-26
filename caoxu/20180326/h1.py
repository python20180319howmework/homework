'''根据他的BMI指标合理的给出建议
BMI = 体重 / 身高*身高
 BMI < 18.5    “你这么瘦,可以肆无忌惮的大吃大喝啦"
 18.5 <= BMI < 25  “兄弟！你离模特就差八块腹肌了”
 25 <= BMI < 30  “控制你自己哦！脂肪有点多啦”
 BMI >= 30   “不能再吃了！跑几圈去吧，你也可以是男神” '''
from math import *
weight=float(input("输入你的体重(单位kg):"))
height=float(input("输入你的身高(单位m):"))
BMI=weight/(pow(height,2))
if 18.5<=BMI<25:
	print("你这么瘦,可以肆无忌惮的大吃大喝啦")
elif 25<=BMI<30:
	print("兄弟！你离模特就差八块腹肌了")
elif BMI>=30:
	print("不能再吃了！跑几圈去吧，你也可以是男神")
else:
	print("worry!!")
