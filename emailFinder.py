#! /usr/bin/python3
import re, pyperclip

emailRegex = re.compile(r"[\w+.'\"-]+@\w+\.[a-zA-Z]{2,4}")

text = pyperclip.paste()

allMail = emailRegex.findall(text)
mailText  = '\n'.join(allMail)
pyperclip.copy(mailText)
print("Successfully extracted email addresses to clipboard")