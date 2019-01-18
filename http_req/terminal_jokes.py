from ascii_art import print_art
from http_request import get_res

url = "https://icanhazdadjoke.com"
cmd = None

def searched_joke():
  url_search = "https://icanhazdadjoke.com/search"
  term = input("Search for it: ")
  data = get_res(url_search, "application/json", term)
  index = None
  if data['total_jokes'] > 0:
    print(f"Found {data['total_jokes']} jokes\n Here is one ...\n")
    print(data['results'][0]['joke'])

  if data['total_jokes'] > 1:
    while True:
      print()
      index = int(input('Enter order number of the joke: '))

      if index == 0:
        print("Done! You are back to the main menu!")
        reset()

      if index < data['total_jokes']:
        print()
        print(data['results'][index-1]['joke'])
      
      if index > data['total_jokes']:
        print(f"\nThere isn't that many jokes for {term}")

  else:
    print(f"\nDammit, jokes for {term} not found! Try with some other words \n")

  


def random_joke():
  print("Hey, Want a joke? Here is a random one")
  data = get_res(url, "application/json")
  print(data['joke'])

def reset(cmd = None):
  print_art("Welcome to Terminal Jokes", 'white')


reset()
while cmd != '3':
  
  cmd = input("1 -> Random Joke | 2 -> Search: ")
  if cmd == '1':
    random_joke()

  elif cmd == '2':
    searched_joke()
  
  elif cmd == '3':
    print_art("Bye :(", 'red')

  else:
    print("\nYou entered a wrong command! Remember, 1.Random | 2.Search | 3.Quit\n")
