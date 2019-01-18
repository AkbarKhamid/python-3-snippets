# file = open("File_I_O/story.txt")
# content = file.read() # reads everything or n chars
# print(content)
# file.seek(0) # moves the curser where spcified
# one_line = file.readline() # Reads untill it hits new line
# print(one_line)
# second_line = file.readline()
# print(second_line)
# third_line = file.readline()
# print(third_line)
# file.seek(0)
# list_content = file.readlines()
# print(list_content)
# file.close() # a must to free up system resources, DON'T FORGET!
# if file.closed:
#   print("-- FILE IS CLOSED! --")

#  SHORTER AND PREFERRED SYNTAX 
# with open('File_I_O/story.txt') as file:
#   content = file.read() # reads everything or n chars
#   print(content)
#   file.seek(0) # moves the curser where spcified
#   one_line = file.readline() # Reads untill it hits new line
#   print(one_line)
#   second_line = file.readline()
#   print(second_line)
#   third_line = file.readline()
#   print(third_line)
#   file.seek(0)
#   list_content = file.readlines()
#   print(list_content)
#   # no need to close the file. It is closed automatically by 'with syntax'
# if file.closed:
#   print("-- FILE IS CLOSED AUTOMATICALLY! --")