class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, data):
		self.items.insert(0, data)

	def dequeue(self):
		return self.items.pop()

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def showQ(self):
		for i in self.items:
			print(i, end = ' ')
		print('')

class Deque:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addRear(self, data):
		self.items.append(data)

	def addFront(self, data):
		self.items.insert(data)

	def removeFront(self):
		return self.items.pop(0)

	def removeRear(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def showQ(self):
		for i in self.items:
			print(i, end = ' ')
		print('')