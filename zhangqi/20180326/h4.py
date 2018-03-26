#读入用户输入的一个字符串，普安段字符串中有多少各大写字母，多少各数字
#多少个小写字母

mystr = input("请输入一个字符串")
n = 0
N = 0
num = 0
for s in range(len(mystr)):
	if 97<= ord(mystr[s]) <= 122:
		n = n + 1
	elif 65 <= ord(mystr[s]) <= 90:
		N = N + 1
	elif mystr[s].isdigit():
		num = num + 1
print ("大写字母有%s个" % N)
print ("小写字母有%s个" % n)
print ("数字有%s个" % num)





























