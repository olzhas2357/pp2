print("number: ")
a = int(input())

i = 0
while i < a:
    i += 1
    if i == 3 or i == 5:
        continue
    print("this is number you need", i)