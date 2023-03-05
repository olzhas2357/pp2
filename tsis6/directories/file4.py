# Write a Python program to count the number of lines in a text file.

with open('file1.py', 'r') as f:
    l = len(f.readlines())
print(l)