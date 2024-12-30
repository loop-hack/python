x = int(input("What's x? "))
print(f"x is {x}")


""" Output: What's x? cat
  ValueError: invalid literal for int() with base 10: 'cat'
  this problem arises because we expected an integral value 
  from user but got cat ... to resolve this problem we can do -->
"""


#try except use:

try:
    x = int(input("What's x? "))
    print("x is {x}")
except ValueError:
    print("x is not an integer")

#more sodfisticated way to do this is

try :
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")


#let's create a loop where users will be asked if wrong input

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else :
        break

print(f"x is {x}")