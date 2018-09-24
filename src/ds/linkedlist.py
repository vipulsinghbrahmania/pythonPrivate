class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

class LinkedList:
	def __init__(self):
		self.head = None

	# reverse using recursion
	def reverse(self, node):
		if node.getNext() == None:
			self.head = node
			return

		self.reverse(node.getNext())
		temp = node.getNext()
		temp.setNext(node)
		node.setNext(None)

