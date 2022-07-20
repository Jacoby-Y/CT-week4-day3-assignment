class BST():
	def __init__(self,value):
		self.value = value # Current Value
		self.left = None
		self.right = None
	def insert(self, value):
		if value < self.value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)
		return self
	def contains(self,value):
		"""
			This method accepts an int for its value
			The value parameter is what we are looking for inside of the BST structure
		"""
		if value < self.value: # if passed value is less than current value
			if self.left is None:
				return False
			else:
				return self.left.contains(value)
		elif value > self.value:
			if self.right is None:
				return False
			else:
				return self.right.contains(value)
		else:
			return True
	def get_min_value(self):
		if self.left is None:
			return self.value
		else:
			return self.left.get_min_value()
	def get_max_value(self):
		if self.right is None:
			return self.value
		else:
			return self.right.get_max_value()
	def print_all(self):
		if self.left != None:
			self.left.print_all()
		print(self.value)
		if self.right != None:
			self.right.print_all()
	def invert(self):
		self.left, self.right = (self.right, self.left)
		if self.left != None:
			self.left.invert()
		if self.right != None:
			self.right.invert()

bst_example = BST(39)
bst_example.insert(40)
bst_example.insert(43)
bst_example.insert(56)
bst_example.insert(33)
bst_example.insert(23)
bst_example.insert(12)
bst_example.insert(756)
# print(bst_example.get_max_value())
# print(bst_example.contains(40))
print('='*10)
bst_example.print_all()
print('='*10)
bst_example.invert()
bst_example.print_all()