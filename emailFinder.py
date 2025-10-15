#! /usr/bin/python3
import re, pyperclip

emailRegex = re.compile(r'\w+@\w+\.[a-zA-Z]{2,4}')

#napisi i za fon i dodaj u clipboard
phoneRegex = re.compile(r''' ''')

text = pyperclip.paste()

allMail = emailRegex.findall(text)
mailText  = '\n'.join(allMail)
pyperclip.copy(mailText)
print(mailText)