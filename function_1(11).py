# Write a function that accepts string from user and print all permutations of that string.
from itertools import permutations
def permutation(s):
    str = permutations(s)
    for i in list(str):
        print(list("".join(i)))
    print(len(list(permutations(i))))

if __name__ == "__main__":
    s = input()
    permutation(s)