

from random import *
year=int(input("请输入出生年份："))
if (year//10)%10==9:
	print("你是90后")
elif  (year//10)%10==8:
	print("你是80后")
else:
	print("你是00后")


