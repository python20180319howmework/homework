def nain(year):
    if year%4==0 and year%100!=0 or year%400==0:
       return 	True
    else:
       return False

def jisuan(year):
    sum1=0
    for i in range(1990,year):
#        print(i)
        if nain(i):
           sum1+=366
        else:
           sum1+=365
    return sum1


'''def jieguo(year,month,day):   
    n=0
    if nain(year):
       l=[31,29,31,30,31,30,31,31,30,31,30,31]
       for j in l[:month-1]:
           n+=j
    else:
       l=[31,28,31,30,31,30,31,31,30,31,30,31]
       for j in l[:month-1]:
           n+=j
    n+=day
    return (n+jisuan(year))%7
print(jieguo(2018,3,28))'''
