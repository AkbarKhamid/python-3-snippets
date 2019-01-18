from termcolor import *
from pyfiglet import *

def print_art(msg, color):
  valid_colors  = ('red', 'blue', 'yellow', 'white', 'magenta', "cyan", 'green')
  if color not in valid_colors:
    color = 'white'
  text = colored(figlet_format(msg), color)
  print(text)
  return text
  
# text = input("Enter a text: ")
# color = input("What color? ")

# print_art(text, color)