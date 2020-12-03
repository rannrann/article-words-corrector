import re

stri="A.abc is good (1)"
matchobj = re.findall(r'([a-zA-Z][a-zA-Z]+[\sa-z\s]*)\((.*)\)', str(stri).lower())
str=''
for group in matchobj[0]:
    str+=group
matchobj=[str]
print(matchobj)