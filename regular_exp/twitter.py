#taking twitter url from user and then extracting username from it

url = input("URL: ").strip()

username = url.replace("https://twitter.com/","")
print(f"Username: {username}")


'''using re.sub() for replace and refining'''
'''re.sub(pattern,replace,string,count=0,flags=0)'''

import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)

print(f"Username: {username}")

'''thers bug above if twitter.com/ is given that is no username'''
'''we can use re.search to make it necessary one or more character after /'''

import re

url = input("Url: ").strip()

matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)",url,re.IGNORECASE)

if matches:
    print(f"Username:",matches.group(3))

'''shorting code using walrus operator := '''

import re

url = input("Url: ").strip()

if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)",url,re.IGNORECASE):
    print(f"Username:",matches.group(3))

'''there's problem above that if user give any of https and www but not both then matches.group(2) will be in print'''
'''same if both given then (3) , simple solution is not to capture both as group at all'''

import re

url = input("Url: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)",url,re.IGNORECASE):
    print(f"Username:",matches.group(1))

'''username format taking in account '''

import re

url = input("Url: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)",url,re.IGNORECASE):
    print(f"Username:",matches.group(1))