from  multiprocessing import Process,Lock
def c(arg):
    #with l:
        f=open("lfff.txt","a")
        f.write(arg*10)
        f.close()
if __name__ == '__main__':
   # l=Lock()
    f=open("lfff.txt","w")
    f.close()
    p=Process(target=c,args=("hello",))
    p1=Process(target=c,args=("world",))
    p.start()
    p1.start()
    p.join()
    p.join()