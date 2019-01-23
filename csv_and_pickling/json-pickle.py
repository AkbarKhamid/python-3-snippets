import jsonpickle


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


cat = Cat("Mosh", "Koshka")

# # To JSONPICKLE 'c' the cat:
# with open("cat.json", "w") as file:
#     frozen = jsonpickle.encode(cat)
#     file.write(frozen)

# To bring back 'cat' instance using JSONPICKLE
with open("cat.json", "r") as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)
