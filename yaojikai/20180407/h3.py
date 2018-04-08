
'''
根据字典的特性模拟一个通讯录，完成以下功能，用户根据输入的数选择功能
1） 1.查找电话号码
2） 2.增加联系人
3） 3.删除联系人
4） 4.修改联系人的电话号码
5） 5.退出通讯录，并将所有联系人写入文件后的格式为
	例如：
		王占森  123455556
		刘其    222222335
	尝试使用面向对象编程

'''

from enum import Enum, unique

class Tel(Enum):
	查找电话号码 = 1
	增加联系人 = 2
	删除联系人 = 3
	修改联系人的电话号码 = 4
	退出通讯录 = 5

for i,member in Tel.__members__.items():
	print(i,member.value)

dict = {"刘琪":"12345556","王占森":"222222335"}

while True :
	n = input("请输入指令：")
	if n == "1":
		key = input("请输入查找姓名：")
		if key in dict:
			print(key + dict[key])
		else:
			print("空联系人")
	
	elif n == "2":
		key = input("请输入联系人姓名：")	
		if key in dict:
			print("以存在联系人")
		else :
			value = input("请输入电话号码：")
			dict[key] = value
			print(key + dict[key])

	elif n == "3":
		key = input("请输入联系人姓名")
		if key in dict:
			dict.pop(key)
			print("删除成功")
		else :
			print("通讯录中无此联系人")

	elif n == "4":
		key = input("请输入联系人姓名:")
		if key in dict:
			value = input("请输入电话号码:")
			dict[key] = value
		else :
			print("不存在此联系人")
	elif n == "5":
		break
	else :
		print("请输入正确的指令")






