

'''
3.用户任意输入他的生日，判断他输入00后，90后，还是80后
'''
date = input("输入您的生日：")
bir = int(date[0:4])
if 1979<bir<1990:
	print("您是80后") 
elif 1989<bir<2000:
	print("您是90后")
elif bir >1999:
	print("您是00后")
else :
	print("您OUT了")

