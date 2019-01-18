# while True:
#   try:
#     num = int(input("Please enter a number:"))
#   except ValueError:
#     print("Oops! That's not a number")
#   else:
#     print("Good Job! You entered a number")
#     break
#   finally:
#     print("Runs no matter what")
# print("Rest of the program")

def divide(a,b):
  try:
    result = a/b
  except (ValueError, TypeError, ZeroDivisionError) as err:
    print("Something went wrong ...")
    print(f"Error: {err}")
  else:
    return f"{a}/{b} = {result}"

print(f"Output: {divide(1,0)}")
print(f"Output: {divide(1,2)}")
