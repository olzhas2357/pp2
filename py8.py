# put your python code here
a = input()
c = a.count('f')
l = a.find('f')
r = a.rfind('f')
if c == 0:
    print(-2)
elif c == 1:
    print(-1)
else:
    print(r, l)