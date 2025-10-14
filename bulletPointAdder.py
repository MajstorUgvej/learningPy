#! /usr/bin/python3
import pyperclip

# uzima tekst in clipboarda
text = pyperclip.paste().rstrip('\n')

# dodaje '*' na pocetak reda da oznaci element niza
sentences = text.split('\n')
text = '*' + '\n*'.join(sentences)

# vraca novi text u clipboard
pyperclip.copy(text)

print('Successfully added bullet points')