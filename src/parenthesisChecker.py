from ds.stack import Stack

def matches(open, close):
	opens = "({["
	closes = ")}]"
	return opens.index(open) == closes.index(close)

def parCheck(pars):
	s = Stack()
	balanced = True
	i = 0
	while i < len(pars) and balanced:
		par = pars[i]
		if par in "({[":
			s.push(par)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, par):
					balanced = False
		i += 1
	if balanced and s.isEmpty():
		return True
	else:
		return False

# Driver test code
print(parCheck("((()())"))