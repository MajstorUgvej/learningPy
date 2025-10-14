#! /usr/bin/python3
import pyperclip, sys

passwords = {'email': 'sifraEmail', 'blog': 'sifraBlog'}

if len(sys.argv) < 2:
    print("usage: ./passCopy.py [account] - copy account password")
    sys.exit(1)

# 0 je naziv programa
acc = sys.argv[1]

# Ako nadje kopira u clipboard da ne moras da kopiras duge generisanje sifre
if acc in passwords:
    pyperclip.copy(passwords[acc])
    print("Successfully copied to clipboard")
else:
    print("Unable to find account: " + acc)