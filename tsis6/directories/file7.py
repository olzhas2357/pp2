# Write a Python program to copy the
# contents of a file to another file

with open("A.txt", 'r') as firstfile, open('B.txt', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)