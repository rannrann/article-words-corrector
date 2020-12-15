import re
str="[01:45.00]B She is ready across the robd.(4)\n"

obj = re.findall(r'\(.*\)',str)
str=str.replace(obj[0],'')
print(str)
