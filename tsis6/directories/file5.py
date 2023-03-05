import os

l = ["olzhas ", " is ", " very ", " strong ", "and", "smart"]
with open("5.txt", "w+") as f:
    f.writelines(l)