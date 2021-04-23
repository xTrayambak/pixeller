import time

class o:
	def sub(a, b):
		return a - b

	def add(a, b):
		return a + b

	def mult(a, b):
		return a * b

	def div(a, b):
		try:
			return a / b
		except ZeroDivisionError:
			return a * b / 1


class PRNG():
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c


		self.operationTranslate = {'mult': o.mult, 'div': o.div, 'add': o.add, 'sub': o.sub}
		self.operations = ['mult', 'div', 'add', 'sub']
		self.nos = [self.a, self.b, self.c]
		self.types = {'int': int, 'float': float, 'str': str}

	def _change(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def _gen(self, res, max_size):
		result = 0 # max calculated
		final_result = 0 # limited
		for x in range(int(time.time()*50)):
			extraNo = x * self.c * 2 or x / self.c * 2
			x += 1

			if extraNo < 1:
				print(x)
				result += x * (x * (time.time()-3) * self.x * (time.time()+2) * self.c, (time.time()*74))
			elif extraNo > 1:
				result += (time.time()) * (time.time()*3), (time.time()*12-2)


		return self.types[res](result)