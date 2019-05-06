#! python3
# bulletPointAdder.py adds wiki bullets
# at the beginnig of each line of text in the clipboard

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]    

text = '\n'.join(lines)

pyperclip.copy(text)