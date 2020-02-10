
class ArrayQueue:
	def __init__(self):
		self.data = []
		self.sz = 0

	def enqueue(self, person):
		self.sz += 1
		self.data.insert(0, person)

	#return self.sz < max queue size
	def availableSpace(self):
		return self.sz < 20

	def dequeue(self):
		self.sz -= 1
		return self.data.pop()

	def size(self):
		return self.sz

	def isEmpty(self):
		return self.sz == 0

	def getQueue(self):
		return self.data

	def contains(self, person):
		s = self.size()
		i = 0
		while i < s:
			if self.data[i].id == person.id:
				return True
			i += 1
		return False