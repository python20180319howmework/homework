from math import *

lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
l2=lis[0]
l3=l2[1]
dic=l3[2]
dic['k1']=['TT',3,'1']

print(lis)
dic['k1']=['tt','100','1']
print(lis)
dic['k1']='tt',3,'101'
print(lis)
