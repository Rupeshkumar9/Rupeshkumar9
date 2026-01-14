# a Python program to display total memory, used memory, and available memory using the psutil library.

import psutil

memory = psutil.virtual_memory()
print(f"Total Memory: {memory.total / (1024 ** 2):.2f} MB")
print(f"Used Memory: {memory.used / (1024 ** 2):.2f} MB")
print(f"Available Memory: {memory.available / (1024 ** 2):.2f} MB")




















