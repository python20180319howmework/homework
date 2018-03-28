"""
5.读入用户输入的一个字符串，判断字符串中有多少个大写字母
  多少个数字，多少个   小写字母
  提示：
   判断一个字符串是否是数字：isdigit()  例如"1".isdigit()为True
   得到单个字符串对应的值 ord("A") == 65
"""
print("请输入：")
text = input()
num1 = 0
num3 = 0
num2 = 0
for word in text:
	if word.isdigit()==True:
		num3 += 1
	elif ord("a") <= ord(word) <=ord("z"):
		num1 += 1
	elif ord("A")<= ord(word)<=ord("Z"):
		num2 += 1
	else:
		pass
print("字符串中有{}个小写字母".format(num1))
print("字符串中有{}个数字".format(num3)) 
print("字符串中有{}个大写字母".format(num2))


