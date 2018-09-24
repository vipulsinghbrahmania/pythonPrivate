from ds.queue import Queue

# applying monkey patch
def dequeue(self):
	return self.items.pop(0)

def reverse(inputList):
	q = Queue()
	Queue.dequeue = dequeue # over-ride using monkey patch
	retList = []
	for i in inputList:
		q.enqueue(i)
	
	while not q.isEmpty():
		retList.append(q.dequeue())

	return retList
