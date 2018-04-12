from multiprocessing import  Process
def count1(t):
    f=open(t,'r')
    for i in f.readlines():
        l.append(i)
    print(len(l))
    f.close()
def count2(t):
    f=open(t,'r')
    for i in f.readlines():
        l.append(i)
    print(len(l))
    f.close()
def count3(t):
    f=open(t,'r')
    for i in f.readlines():
        l.append(i)
    print(len(l))
    f.close()
if __name__ == '__main__':
    l=[]
    p=Process(target=count1,args=("/etc/passwd",))
    p.start()
    p1=Process(target=count2,args=("/etc/group",))
    p1.start()
    p2=Process(target=count3,args=("/etc/bashrc",))
    p2.start()