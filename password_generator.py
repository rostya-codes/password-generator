from random import randint as ri
from os import system as s

CHARS = ('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM`1234567890-=!@#$%^&*()_+|\\/[]{}:;<>?~')

n = int(input("Enter the number of characters in your password: "))

password = ""

for i in range(n):
    password = f'{password}{CHARS[ri(0, len(CHARS)-1)]}'

print(password)