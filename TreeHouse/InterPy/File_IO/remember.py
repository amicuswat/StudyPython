import sys

def rememberer(thing):
    #open file
#    file = open('database.txt', 'a')
    #write thing to file
#    file.write(thing+'\n')
    #close file
#    file.close()
    with open('database.txt', 'a') as file:
        file.write(thing+'\n')

def show():
    #open file
    #print out each line in the file
    #close file
    pass

if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        rememberer(' '.join(sys.argv[1:]))
    rememberer(input("What should I remember > "))
