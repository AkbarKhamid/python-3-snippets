# ASSERTION TEST SYNTAX 
# NOTE! THIS TYPE OF TESTS MAY FAIL WHEN RUN IN            OPTIMIZED MODE
#       NOT GOOD

# def check(a,b):
#   assert a==b, f'{a} and {b} are not equal'
#   return True

# print(check('4',4))


#  DOCTEST SYNTAX
# CMD: python3 -m doctest -v file_name.py
# NOTE: Sytnax has to be exact the same
#       Strings should be in single quotes
#       Dictionary keys have to be in order
#       NOT GOOD

# def add(x,y):
#   """
#   adds x to y

#   >>> add(1,2)
#   3

#   >>> add(5,5)
#   10

#   >>> add(3,4)
#   7

#   >>> add(None, False)
#   Traceback (most recent call last):
#     ...
#   TypeError: unsupported operand type(s) for +: 'int' and NoneType'
#   """
#   return x+y