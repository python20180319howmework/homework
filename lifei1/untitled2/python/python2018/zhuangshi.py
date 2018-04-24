import functools

def log(mystr):
	def funargs(fun):
		@functools.wraps(fun)
		def wrapper(*args,**kw):
			print("%s" % mystr)
			return fun(*args,**kw)
		return wrapper
	return funargs
@log("要吃饭啦")
def now():
	print("2018.04.04")
now()
print("%s" % now.__name__)
