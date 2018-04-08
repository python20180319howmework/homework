'''
3. 根据字典的特性模拟一个通讯录,完成一下功能,用户根据输入的数选择功能
   1) 1.查找电话号码
   2) 2.增加联系人
   3) 3.删除联系人
   4) 4.修改联系人的电话号码
   5) 5.退出通讯录,并将所有联系人写入文件,要求写入文件后的格式为
         例如:
                王占森   123455556
                刘淇  222222333335
        尝试使用面向对象编程
'''

from enum import Enum, unique

@unique
class Num(Enum):
	查找电话号码 = 1
	增加联系人 = 2
	删除联系人 = 3
	修改联系人的电话号码 = 4
	退出通讯录 = 5

for i,member in Num.__members__.items():
	print(i,member.value)

d = {"王占森":"123455556","刘琪":"222222333335"}
#print(d)

while True :
	n = input("请输入您想要实现的功能序号：")
	if n == "1":
		key = input("请输入您要查找的姓名：")
		if key in d :
			print(key + d[key])
		else:
			print("您还没有添加此人哦")
	elif n == "2":
		key = input("请输入要增加的联系人姓名：")
		if key in d :
			print("该联系人已经存在了哦")
		else :
			value = input("请输入联系电话：")
				
			d[key]= value
			print("您已成功添加联系人")
	elif n == "3":
		key = input("请输入要删除的联系人的姓名：")
		if key in d :
			d.pop(key)
			print("您已删除成功")
		else:
			print("您还没有添加此人哦")
	elif n == "4":
		key = input("请输入您要修改的联系人姓名：")
		if key in d:
			value = input("请输入电话号码：")
			d[key]= value
			print("您已修改成功")
		else :
			print("您还没有添加此人哦")
	elif n == "5":
		print("您已成功退出")
	else:
		print("您好像输错了哦")












