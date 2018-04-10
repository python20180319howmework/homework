'''
1.创建3个任务进程,分别统计"/etc/passwd" “/etc/group” “/etc/bashrc”文件有多少行
'''

a = len(open(r"/etc/passwd",'rU').readlines())
print(a)
b = len(open(r"/etc/group",'rU').readlines())
print(b)
c = len(open(r"/etc/bashrc",'rU').readlines())
print(c)
