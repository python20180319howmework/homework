def digui(num):
    l=[]
   
    for i in range(num):
        if i==0 or i==1:
           l.append(1)
        else:
           l.append(l[i-2]+l[i-1])
    return l[num-1]
n=int(input("please:"))
print(digui(n))
