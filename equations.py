def comb():
	n = input("Please define n: ")
	r = input("Please define r: ")
	
	result = fact(int(n)) / (fact(int(n) - int(r)) * fact(int(r)))
	
	return int(result)
	
def comb(n, x):
	result = fact(int(n)) / (fact(int(n) - int(x)) * fact(int(x)))
	
	return int(result)
	
def perm():
	n = input("Please define n: ")
	r = input("Please define r: ")
	
	result = fact(int(n)) / fact(int((int(n) - int(r))))
	
	return int(result)
	
def binDist():
	n = input("Please define n: ")
	x = input("Please define x: ")
	p = input("Please define p: ")
	
	result = comb(int(n), int(x)) * (float(p)**int(x)) * ((1 - float(p))**(int(n) - int(x)))
	
	return float(result)
	
def negBin():
	z = input("Please define z: ")
	r = input("Please define r: ")
	p = input("Please define p: ")
	
	result = comb(int(z) - 1, int(r) - 1) * (float(p)**int(r)) * ((1 - float(p))**(int(z) - int(r)))
	
	return float(result)
	
# FACTORIAL COMPUTATION
def fact(a):
	b = a - 1
	
	while b > 0:
		a *= b
		b = b - 1
		
	return int(a)
