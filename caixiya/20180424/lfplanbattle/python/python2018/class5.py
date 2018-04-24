class A(object):
	def __init__(self):
		print("init A is called")

class B(A):
	def __init__(self):
		print("init B is called")
		#A.__init__(self)
		super(B,self).__init__()
class C(A):
	def __init__(self):
		print("init C is called")
		#A.__init__(self)
		super(C,self).__init__()

class D(B,C):
	def __init__(self):
		#B.__init__(self)
		#C.__init__(self)
		super().__init__()

d=D()
