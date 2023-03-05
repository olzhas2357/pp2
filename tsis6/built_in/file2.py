# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
n = input()
sum1, sum2 = 0, 0
for i in range(len(n)):
    if n[i].islower():
        sum1 += 1
    elif n[i].upper():
        sum2 += 1
        
print("Upper letter: ", sum1)
print("Lower letter: ", sum2)
