def histogram(l):
    for num in l:
        print("*"*num)
    print()

if __name__ == "__main__":
    l=[]
    for i in range(int(input())):
        l.append(int(input()))
    histogram(l)