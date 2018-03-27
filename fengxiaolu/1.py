a=input("请输入身高")
b=input("请输入体重")
a=float(a)
b=float(b)

BMI=b/(a*a)
print("%d" % BMI)

if (BMI < 18.5):
	print("你这么瘦，可以肆无忌惮的大吃大喝了")
elif (18.5 <=BMI < 25):
	print("兄弟！你离模特就差八块腹肌了")  
elif (25 <= BMI < 30):
	print("控制你自己哦！脂肪有点多啦")
else:
	print("不能在吃了！跑几圈去吧，你也可以是男神")
