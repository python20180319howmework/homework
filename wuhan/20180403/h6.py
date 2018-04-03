":87, “caoxu”:90, “caohuan”:98, “wuhan”:82, “zhijia”:89}
   1)将以上字典按成绩排名 
'''
# sorted 排序
d = {"chaoqian":87,"caoxu":90,"caohuan":98,"wuhan":82,"zhijia":89}
print(sorted(d.items(),key = lambda i:i[1],reverse = True))


