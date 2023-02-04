# Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
def reversed_let(s):
    l = s.split()
    for num in reversed(l):
        print(num, end = " ")
if __name__=="__main__":
    s = input()
    reversed_let(s)