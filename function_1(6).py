def unique(str):
    l = []
    for i in range(len(str)):
        if str[i] not in l:
            l.append(str[i])
    s = "".join(l)
    print(s)
if __name__=="__main__":
    str = input()
    unique(str)