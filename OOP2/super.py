class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species
  
  def __repr__(self):
    return f"{self.name} is a {self.species}"
  
  def make_sound(self, sound):
    print(f"This animal says {sound}")
  
class Cat(Animal):
  def __init__(self, name, breed, toy):
    super().__init__(name, species ="cat")
    self.breed = breed
    self.toy = toy
  
  def play(self):
    return f"{self.name} plays with {self.toy}"

mosh = Cat("Mosh", "Scottish Fold", "String")
# print(mosh.make_sound("meow"))
# # print(mosh)
# #print(mosh.breed)
# #print(mosh.toy)
# #print(mosh.species)
# print(mosh.play())