# find the last two digits of 2^n

def powerOf2(n):
	if n == 0: # base condition
		return 1
	return 2 * powerOf2(n -1)

def last2digits(num):
	powerValue = powerOf2(num) # get the value of 2^n
	last = powerValue % 10
	powerValue //= 10
	y = powerValue % 10 * 10 + last	
	print("last two digits of 2 ^", num, " = ", y)

# Driver test code
n = 72
last2digits(n)