from ds.stack import Stack

def baseConverter(inputNum, base):
	remainderStack = Stack()

	while inputNum > 0:
		remainder = inputNum % base
		remainderStack.push(remainder)
		inputNum //= base

	converted = ""
	while not remainderStack.isEmpty():
		converted += str(remainderStack.pop())

	return converted

# Driver test code
print(baseConverter(25, 2))
print(baseConverter(25, 8))
print(baseConverter(25, 10))
print(baseConverter(25, 16))
