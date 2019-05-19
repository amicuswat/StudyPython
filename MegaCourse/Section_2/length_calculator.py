def string_length(mystring):
	if type(mystring) == int:
		return "Sorry, ints don't have length"
	elif type(mystring) == float:
		return "Sorry, floats don't have length"
	else: 
		return len(mystring)

print(string_length(1.5))