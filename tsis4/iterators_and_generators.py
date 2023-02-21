
# Create a generator that generates the squares of numbers up to some number N
print([(i+1) **  2 for i in range(int(input()))])

#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console
s = [i for i in range(int(input())) if i % 2 == 0 ]
print(*s, sep = ', ')

#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
print([i for i in range(int(input())) if i % 3 == 0 or i % 4 == 0])

#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
s = [i ** 2for i in range(int(input()), int(input())+1)]
print(*s, sep = ", ")

# Implement a generator that returns all numbers from (n) down to 0.
n = [i for i in range(int(input()) + 1)]
print(n[::-1])