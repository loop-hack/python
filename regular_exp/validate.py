#checking correct email given by users

email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")

else:
    print("Invalid")

'''more precious checking'''

email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain: 
    #Note: statement 1 :if username exist and "." present in domain
    print("Valid")

else:
    print("Invalid")

'''checking specific(here .edu) email'''

email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")

else:
    print("Invalid")

# importing regular library which helps in checking

'''just for learning use of re.search()'''
import re

email = input("What's your email? ").strip()

if re.search("@",email):
    #format of re.search, re.search(pattern,string,flags=0)
    print("Valid")

else:
    print("Invalid")

#using special simple for pattern in re.search()

import re

email = input("What's your email? ").strip()

if re.search(".+@.+",email):
    print("Valid")

else:
    print("Invalid")

'''creating code that checks .edu ending as well'''

import re

email = input("What's your email? ").rstrip()

if re.search(r".+@.+\.edu",email):
    print("Valid")

else:
    print("Invalid")

'''to restrict only one @in email'''

import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu",email):
    print("Valid")

else:
    print("Invalid")

''' simplifying and checking a group like com edu'''

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(edu|com|git)",email):
    print("Valid")

else:
    print("Invalid")


'''using flag to ignore cases,multiline[re.MULTILINE]'''

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(edu|com|git)",email,re.IGNORECASE):
    print("Valid")

else:
    print("Invalid")


'''what if my email is  malan@cs50.harvard.edu'''

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|git)",email,re.IGNORECASE):
    print("Valid")

else:
    print("Invalid")