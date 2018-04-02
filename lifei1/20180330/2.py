def mypow(m,n):
	if m==0 and n==0:
		return "error"
	if n==0:
		return 1
	if m>0 and n<0:
		return 1/(m*mypow(m,abs(n)-1))
	if m>0 and n>0:
		return m*mypow(m,n-1)
	if m<0 and n<0 and abs(n)%2==0:
		return 1/(abs(m)*mypow(abs(m),abs(n)-1))
	if m<0 and n<0 and abs(n)%2!=0:
		return -(1/(abs(m)*mypow(abs(m),abs(n)-1)))
	if m<0 and n>0 and n%2==0:
		return abs(m*mypow(m,n-1))
	if m<0 and n>0 and n%2!=0:
		return -m*mypow(m,n-1)
if __name__=="__main__":
	m,n=eval((input("m,n")))
	mypow(m,n)
	print(mypow(m,n))
	#print(mypow(m,n))
