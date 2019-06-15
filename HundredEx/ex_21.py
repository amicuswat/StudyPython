d = {"a": 1, "b": 2, "c": 3}
print({key:value for key, value in d.items() if value <= 1})
#dict((key, value) for key, value in d.items() if value <= 1)
#filtered_dict = {k:v for k,v in d.iteritems() if filter_string in k}
