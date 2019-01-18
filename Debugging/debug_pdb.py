# debugging using pdb module 

import pdb; pdb.set_trace()
""" Commands
    l (list)
    n (next line)
    p (print)
    c (continue - finishes debugging)
"""
first = "first"
second = 'second'
result = first + second
third = 'third'
result += third
print(result)

