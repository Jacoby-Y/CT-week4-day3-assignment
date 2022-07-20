# Implement a function that receives a string, and lets you extend it with repeated calls. When no argument is passed you should return a string consisting of space-separated words you've received earlier.

# Note: there will always be at least 1 string; all inputs will be non-empty.

# For example:



def create_message(string):
	joined = [ string ]
	def inner(s=None):
		if s == None:
			return " ".join(joined)
		joined.append(s)
		return inner
	return inner

print(create_message("Hello")("World!")("How")("are")("you?")())


