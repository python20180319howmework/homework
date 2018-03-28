#1
def l(name):
    count=0
    for i in name:
        if i=="":
           break
        else:
           count+=1
    return count
print(l("lii"))
#2
l=["172.16.3.1","172.16.105","172.15.2.0","172.16.3.1","172.16.3.1"]
l1=[]
for i in l:
    if i not in l1:
       l1.append(i)
for j in range(len(l1)):
     print("{}出现次数：{}".format(l[j],l.count(l[j])))
   
#print(l1[0].count(l))
#3
def zhishu(num):
    for i in range (2,num):
        if num%i==0:
           return False
           break
        else:
           return True
def k(num):
    if zhishu(num):
       print("是质数")
    else:
       print("不是质数")
k(3)
#4
def shu(num1,num2):
    sum1=0
    sum2=0
    for i in range(num2):
        sum2+=num1*(pow(10,i))
        sum1+=sum2
    return sum1
print(shu(3,5))
#5
def panduan(grade):
    if grade>=90 and grade<=100:
       return "A"
    if grade>=80 and grade<=89:
       return "B"
    if grade>=70 and grade<=79:
       return "C"
    if grade>=60 and grade<=69:
       return "D"
    if grade<=59:
       return "E"
print(panduan(95))
         

  
    
    
