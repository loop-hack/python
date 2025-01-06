#fixing name we are given by users

'''lets say some given us by habbit lastname, firstname'''

name = input("What's your name? ").strip()

if "," in name:
    last,first = name.split(", ")
    name = f"{first} {last}"

print(f"hello, {name}")

'''using regular exp we can do more refining'''

import re

name = input("What's your name? ").strip()

matches = re.search("^(.+), *(.+)$",name)

if matches:
    last,first = matches.groups()
    name = f"{first} {last}"

print(f"hello, {name}")


'''we can shorten this up'''

import re

name = input("What's your name? ").strip()

matches = re.search("^(.+), *(.+)$",name)

if matches:
    name = matches.group(2) + matches.group(1)

print(f"hello, {name}")