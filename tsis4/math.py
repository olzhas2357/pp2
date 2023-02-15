import math
# 1
n = int(input("Введите число:"))
a = math.radians(n)
# print(f"Radian {a}")
#2
h = int(input("height: "))
a, b = int(input("Base, first value: ")), int(input("Base, second value: "))
print("S = ", (a+b)/2*h)
#3
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
a = l / (2 * math.tan(math.pi / n))
A =  0.5 * l * n * a
print(f"Area: {int(A)}")
#4
n = int(input("Length of base: "))
m = int(input("Height of parallelogram: "))
print(f"Area: {n * m}")