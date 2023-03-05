# Write a Python program to delete file by specified path. Before deleting check
# for access and whether a given path exists or not

import os
string = input()
if not os.path.exists(string):
    print("Sorry i cannot delete file")
else:
    os.remove(string)