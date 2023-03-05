import os

print("Test a path exists or not: ")
path = r"C:\Users\Olzhas\PycharmProjects\pp2-22B030628\mycode\tsis6\directories\file1.py"

if os.path.exists(path):
    print("YES, File exists")
    print(f"File name of the path:  {os.path.basename(path)}")
    print(f"Dir name of the path: {os.path.dirname(path)}")
else:
    print("NO")
