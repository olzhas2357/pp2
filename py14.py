
s = input()
l = s.find('h')
r = s.rfind('h')

print(s[: l +1] + s[ r -1:l:-1] + s[r:])
