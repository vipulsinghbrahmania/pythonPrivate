class Stack:
	def __init__(self):
		self.items = []

	def push(self, data):
		self.items.append(data)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)
