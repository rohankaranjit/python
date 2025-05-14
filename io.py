# READS THE CONTENT IN READ ALL CONTENT AND IN READLINE ONE BY ONE
f = open("practice.txt", "r")
content = f.readline()         # reads entire content
print(content)
f.close()


# APPENDING THE DATA
f = open("practice.txt", "a")
f.write("\nThis is new text.")
f.close()


# WE DONT NEED TO CLOSE FOR THIS 
with open("practice.txt", "r") as f:
    content = f.read()
    print(content)

# DELETION 
import os
os.remove("samples.txt")