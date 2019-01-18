class DickDict(dict):
  def __repr__(self):
    print(" YEAH, I AM A DICT")
    return super().__repr__()
  
  def __missing__(self, key):
    print(f"WELL, {key} AIN'T HERE!")
  
  def __setitem__(self, key, value):
    print("WHY YOU CAN'T KEEP YOUR WORD, DAMIT!\n ALIRGHT,  ALRIGHT")
    super().__setitem__(key, value)
  

d = DickDict({'first': 'dick', 'last': 'dict'})
print(d)
d['hello'] = 'world'
print(d)