class Creature:
  
  def speak(self):
    raise NotImplementedError("Subclass should have its own")

class Cat(Creature):
  def speak(self):
    return 'meow'

class Human(Creature):

  def speak(self):
    return 'Yo, What up!'

cat = Cat()
cat.speak()
me = Human()
me.speak()
fish = Creature()
#fish.speak() # error 