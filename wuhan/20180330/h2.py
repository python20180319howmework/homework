def huiwen(name):
	for i in range(len(name)):
		if name[i]!= name[len(name)-i-1]:
			return False
	else:
		return True

def wu(name):
	if huiwen(name):
		print("这个数是回文数")
	else:
		print("这个数不是回文数")
wu("12345")
