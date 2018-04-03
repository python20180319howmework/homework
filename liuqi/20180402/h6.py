"""
6. 有这样一个字典
   d = {"chaoqian":87, “caoxu”:90, “caohuan”:98, “wuhan”:82, “zhijia”:89}
   1)将以上字典按成绩排名 
"""
d = {"chaoqian":87, "caoxu":90, "caohuan":98, "wuhan":82, "zhijia":89}

print(sorted(d.items(),key = lambda x:x[1],reverse=True))
