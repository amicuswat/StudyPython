temperatures = [10, -20, -289, 100]

def writer(temperatures, filepath):
    with open(filepath, "w") as file:
        for c in temperatures:
            if c > -273.15:
                f = c * 9 / 5 + 32
                file.write(str(f) + "\n")

writer(temperatures, "temperatures_F.txt")

'''
def c_to_f(c):
    if c < -273.15:
        return "This temperature doesn't make sense!"
    else:
        f = c * 9 / 5 + 32
        return f

with open("temperatures_F.txt", "w") as myfile:
    for value in temperatures:
        line = "%s in C - %s in F \n" % (value, c_to_f(value))
        myfile.write(line)
        print(line)
'''
