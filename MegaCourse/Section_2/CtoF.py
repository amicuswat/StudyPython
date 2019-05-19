temperatures = [10, -20, 100]

def converter(degreesC):
	return degreesC * 9 / 5 + 32

for temp in temperatures:
	print(converter(temp))

#user_input = int(input("Input the degrees: "))
#print(str(converter(user_input)))