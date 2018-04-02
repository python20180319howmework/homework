def huiwen(name):
    for i in range(len(name)):

        if name[i]!=name[len(name)-i-1]:
           return False
           break

        else:
           return True
def o(name):
    if huiwen(name):
       print("y")
    else:
       print("n")
o("123654")
    
