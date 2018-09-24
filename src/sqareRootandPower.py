def squareRoot(num):
	return num ** (1 / 2)

def cubeRoot(num):
	return num ** (1 / 3)

def power(num, pow):
	if pow == 0:
		return 1
	elif pow == 1:
		return num

	val = power(num, pow // 2)
	if pow % 2 == 0:
		return val * val
	return val * val * num
