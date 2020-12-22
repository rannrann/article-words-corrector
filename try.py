import re
str="there are books neatly 111-2223 arranged on top of desk18"

obj = re.findall(r'[0-9]*$',str)
print(obj)
