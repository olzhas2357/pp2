# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

import time
import math

def time_square(m, n):
    l = math.sqrt(n)
    time.sleep(m / 1000)
    return "Square root of {} after {} miliseconds is {}".format(n, m, l)
n = float(input())
m = int(input())
print(time_square(m, n))