def weihun(num1):
	s=str(num1)
	for i in range(len(s)):
		if s[i]!=s[len(s)-i-1]:
			return False
	return True
print(list(filter(weihun,[132,12321,11,9989,666])))
