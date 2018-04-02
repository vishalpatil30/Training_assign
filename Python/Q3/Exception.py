class Myexception(Exception):
	def __init__(self,msg):
		self.msg=msg

level = -1

try:
	if level < 1:
		raise Myexception("Invalid level : {}".format(level))

except Myexception,e:
	print(e.msg)
