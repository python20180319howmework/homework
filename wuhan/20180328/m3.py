birthyear = int(input("请输入你的出生年份"))
if birthyear % 1000 % 100 //10 == 0:
	print("你是00后")
elif birthyear % 1000 % 100 //10 == 9:
	print("你是90后")
elif birthyear % 1000 % 100 //10 == 8:
	print("你是80后")
else:
	print("你out了")	
