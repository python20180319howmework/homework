from multiprocessing import Process,Pool
def shui(n):
    g=n%10
    s=n//10%10
    b=n//100
    if pow(g,3)+pow(s,3)+pow(b,3)==n:
        print("%d是水仙花数" % n)
if __name__ == '__main__':
    p=Pool(4)
    for i in range(100,1000):
        p.apply_async(shui, args=(i,))
    p.close()
    p.join()