# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

n = input()
if n == n[::-1]:
    print("Yes")
else:
    print("No")
