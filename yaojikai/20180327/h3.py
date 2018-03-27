#3,用户任意输入他的生日，判断他输入00后，90后，还是80后

data = input("请输入你的生日：")

year = int(data[0:4])

if year >= 2000 :
	print("你是00后阿！")

elif 1990 <= year < 2000:
	print("你是90后阿！")

elif 1980 <= year < 1990:
	print("你是80后阿！")

else:	
	print("你啥都不是！")
