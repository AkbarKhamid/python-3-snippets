class Human:
  def __init__(self, f_name, l_name, age):
    self.f_name = f_name
    self.l_name = l_name
    self._age = age
  
  @property # works as getter
  def age(self):
    return self._age
  
  @age.setter # works as setter
  def age(self, new_age):
    if new_age >= 0:
      self._age = new_age
    else:
      self._age = 0
      raise ValueError(f"Age can not be negative, passed {new_age}")
  



me = Human("Akbar", "Khamidov", 21)
print(me.age) # age is proxy for self._age
me.age = 22
print(me.age)