#1
import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))
#2
import re
def text_match(txt):
    patterns = '^ab+'
    if re.search(patterns, txt):
        return "Found a match"
    else:
        return "Not mathced"

txt = input()
print(text_match(txt))
#3
import re

def text_match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns, text):
        return 'Found a match'
    else:
        return 'Not matched'
text = input()
print(text_match(text))
#4
import re

def text_match(text):
    patterns = '^[A-Z]+[a-z]+$'
    if re.search(patterns, text):
        return 'Found a match'
    else:
        return 'Not matched'
text = input()
print(text_match(text))
#5
import re

def text_match(text):
    patterns = 'a.*?b$'
    if re.search(patterns, text):
        return 'Found a match'
    else:
        return 'Not matched'
text = input()
print(text_match(text))
#6
import re
def text_match(txt):
    x = re.sub("[ ,.]", ':', txt)
    return x

txt = 'olzhas is very smart, very strong and sportsman and decisive, responsible'
print(text_match(txt))
#7
#snake_case -> snakeCase

import re

def snake_to_canel(word):
    return ''.join(i.capitalize() or '_' for i in word.split('_'))

word = input()
print(snake_to_canel(word))

#8
import re
text = input()
print(re.findall('[A-Z][^A-Z]*', text))
#9
import re
txt = "ImportYouLearnEnglish"
x = re.sub(r"(\w)([A-Z])", r"\1 \2", txt)
print(x)
#10
#CamelCase -> snake_case
from re import sub
def snake_case(s):
    return '-'.join(
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        s.replace('_', ' ')
            )
        )
    .split()).lower()
s = input()
print(snake_case(s))
