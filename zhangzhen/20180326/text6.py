
while True:
	try:
		num =  input("请输入1~100之间的整型数：")
		num = int(num)
		print(num,"你好棒阿！继续努力")
		break
	except ValueError:
		print("乖乖，你咋这么不听话呢")






