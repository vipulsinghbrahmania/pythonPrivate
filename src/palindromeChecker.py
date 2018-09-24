from ds.queue import Deque

# regular approach
def palindromeChecker2(inputString):
	reverse = inputString[::-1] # get the reverse of the string
	if inputString == reverse:
		return True
	return False

# palindrome checker using Double ended queue
# remove from both ends of the queue
def palindromeChecker(inputString):
	dq = Deque()
	for char in inputString:
		dq.addRear(char)

	isMatch = True
	while dq.size() > 1 and isMatch:
		first = dq.removeFront()
		last = dq.removeRear()
		if first != last:
			isMatch = False

	return isMatch

# Driver test code
print(palindromeChecker2('madam'))
print(palindromeChecker2('papa'))

print(palindromeChecker('madam'))
print(palindromeChecker('papa'))
