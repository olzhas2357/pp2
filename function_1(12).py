#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(l):
    s = "".join(l)
    if "33" in s:
        print("True")
    else:
        print("False")
l = list()
n = int(input())
for i in range(n):
    c = int(input())
    l.append(str(c))
has_33(l)