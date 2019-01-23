import json

# json.dumps returns a JSON STRING:

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# results in '["foo", {"bar": ["baz", null, 1.0, 2]}]'


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


# A HACKY WAY OF CONVERTING A CLASS INSTANCE INTO A JSON STRING
c = Cat('Mosh', 'Koshka')
json_cat = json.dumps(c.__dict__)
# results in '{"name": "Mosh", "breed": "Koshka"}'
print(json_cat)
