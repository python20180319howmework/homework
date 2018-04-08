from enum import Enum,unique

@unique
class Tel(Enum):
	查找电话号码 = 1
	增加联系人 = 2
	删除联系人 = 3
	修改联系人 = 4
	退出通讯录 = 5

for i,member in Tel.__members__.items():
	print(i,member.value)

dict1 = {"王占森":"123455556","刘淇":"222222333335","张三":"1456789","李四":"4567812"}

while True:

	n = input("输入指令:")

	if n == "1":
		key = input("请输入联系人姓名:")
		if key not in dict1:
			print("不存在该联系人,请重新输入:")
		else:
			print(key +"   "+dict1[key])

	elif n == "2":
		key = input("请输入联系人姓名:")
		if key in dict1:
			print("已存在联系人")
		else:
			value = input("请输入电话号码:")
			dict1[key] = value
			print(key +"   "+dict1[key])

	elif n == "3":
		key = input("请输入联系人姓名:")
		if key not in dict1:
			print("不存在该联系人,请重新输入:")
		else:
			dict1.pop(key)	
			print("已删除")
		print("通讯录为：")
		for key,value in dict1.items():
			print(key +"   "+dict1[key])

	elif n == "4":
		key = input("请输入联系人姓名:")
		if key in dict1:
			print("已存在联系人")
			a = input("是否修改联系方式(y/n):")
			if a == "y":
				value = input("请输入电话号码:")
				dict1[key] = value
			else:
				break

	elif n == "5":
		break

	else:
		print("输入错误")
