#定义一个函数，实现字符串的len方法









def zifuchuan(l):
	dig_cnt, up_cnt, low_cnt = 0, 0, 0
	z = 0 
		
	for s in l:
		if s.isdigit() == True:
			dig_cnt += 1	
		elif ord(s) >= ord("A") and ord(s) <= ord('Z'):
			up_cnt += 1
		elif s.islower() == True:
			low_cnt += 1
		
		z = dig_cnt + up_cnt + low_cnt
	return z

l =str(input("请输入字符串"))
z=zifuchuan(l)
print("字符串个数为{}".format(z))








