# Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(l):
    s = []
    for num in l:
        if num == 0 or num == 7 :
            s.append(str(num))
    k = "".join(s)
    if "007" in k:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    l = []
    for i in range(int(input())):
        l.append(int(input()))
    spy_game(l)