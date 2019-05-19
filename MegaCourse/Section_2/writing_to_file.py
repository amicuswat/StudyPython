def create_new_file(name, data):
	new_file = open(name, "w")
	print("New file created " + name)
	for item in data:
		new_file.write(item + "\n")
		print("Added " + item + " to file " + name)
	new_file.close()
	return True

names = ["Viktor", "Anna", "Lilia", "John"]
file_name = "test.txt"
if create_new_file(file_name, names):
	print("File " + file_name + " is created successfully!")
	print("It's content is the following:")
	created_file = open(file_name)
	content = created_file.read()
	content = content.splitlines()
	for line in content:
		print(line)
else: 
	print("Error, something went wrong, file is not created!")