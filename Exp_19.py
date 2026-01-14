# Simulate Virtual File System.


# Simple Virtual File System simulation in Python
# Dictionary to store the virtual file system


vfs = {"root": {}} # root directory


# Function to create a new directory
def create_directory(path, dirname):
   if path in vfs:
       vfs[path][dirname] = {}
       print(f"Directory '{dirname}' created in '{path}'")
   else:
        print(f"Path '{path}' does not exist")



# Function to create a new file
def create_file(path, filename, content=""):
        if path in vfs:
           vfs[path][filename] = content
           print(f"File '{filename}' created in '{path}'")
        else:
            print(f"Path '{path}' does not exist")



# Function to list contents of a directory
def list_directory(path):
    if path in vfs:
        print(f"Contents of '{path}':")
 
        for name in vfs[path]:
           print(name)
    else:
      print(f"Path '{path}' does not exist")






# Function to read file content
def read_file(path, filename):
    if path in vfs and filename in vfs[path]:
        print(f"Content of '{filename}': {vfs[path][filename]}")
    else:
        print(f"File '{filename}' does not exist in '{path}'")



# Function to write to a file
def write_file(path, filename, content):
    if path in vfs and filename in vfs[path]:
          vfs[path][filename] = content
          print(f"Content written to '{filename}'")
    else:
       print(f"File '{filename}' does not exist in '{path}'")




# --- Simulate usage ---
create_directory("root", "docs")
create_file("root", "readme.txt", "This is the root file")
create_file("root/docs", "notes.txt", "These are some notes")
list_directory("root")
list_directory("root/docs")
read_file("root", "readme.txt")
write_file("root/docs", "notes.txt", "Updated notes content")
read_file("root/docs", "notes.txt")



