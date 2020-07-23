class RationalNumber:

	def __init__(self, n, d):
		self.n = n
		self.d = d

	def addition (self, other):
		n = self.n*other.d + self.d*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def substraction (self, other):
		n = self.n*other.d - self.d*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def multiplication (self, other):
		return RationalNumber(n, d)

	def true_division (self, other):
		return RationalNumber(n, d)

	# complete this first!
	def print_number (self):
		return str(self.n)+'/'+str(self.d)


a = RationalNumber(1, 2)
b = RationalNumber(1, 3)

a.addition(b)
print(a.addition(b))

def main():
	a = RationalNumber(1, 2)
	b = RationalNumber(1, 3)
	print(a) # 1/2
	print(b) # 1/3
	print(a+b) # 5/6
	print(a-b) # 1/6
	print(a*b) # 1/6
	print(a/b) # 3/2
