import re

text_file = open("The Mysterious Affair at Styles.txt", 'r')
text = text_file.read()

#pattern = r'"([A-Za-z0-9_\./\\-]*)"'
pattern = r"'[^']*'"
m = re.findall(pattern, text)
