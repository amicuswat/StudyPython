import json

with open('widget.json') as jsonfile:
    content = json.load(jsonfile)
    print(content['widget']['window'])
