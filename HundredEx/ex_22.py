from pprint import pprint
d = {}
d['a'] = [x for x in range(1, 10)]
d['b'] = [x for x in range(11, 20)]
d['c'] = [x for x in range(21, 30)]
pprint(d)
#print('{',"a: {a},\n b: {b},\n c: {c}".format(**d),'}')
