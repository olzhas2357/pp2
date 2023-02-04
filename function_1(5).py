# Write a function that computes the volume of a sphere given its radius.
import math
from math import pow
def valume(r):
    v = (4/3)*math.pi*(pow(r, 3))
    return v

if __name__=="__main__":
    r = int(input())
    print(valume(r))