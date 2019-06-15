my_dict = {'a':1, 'b':2}
my_dict1 = dict(a=1, b=2, c=3)

def print_dict(some_dict):
    for key, value in some_dict.items():
        print('key "{}": value "{}"'.format(key, value))

print_dict(my_dict)
print_dict(my_dict1)
