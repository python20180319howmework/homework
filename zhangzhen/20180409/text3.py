#3.现有任务要去打印所有的三位数中的水仙花数,
# 要求最多的任务进程不超过4个

from multiprocessing import Pool, Process

def printnum(n):
	res= 0
	l= n 
	while n > 0:
		m = n % 10
		n = n // 10
		res += m**3
	if res == l:
			print("{}是水仙花数".format(res))
if __name__ == '__main__':
    p = Pool(4)
    for i in range(100,1000):
        p.apply_async(printnum,args= (i,))
    p.close()
    p.join()



