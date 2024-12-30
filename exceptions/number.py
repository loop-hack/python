'''x = int(input("What's x? "))
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
'''

#to create function of above feature

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else :
            break
    return x

main()

# instead of break we can use return bcz return has default feature to break out of loop

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else :
            return x
    
main()

#we can shorten this up

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    try:
        return int(input("What's x? "))
    except ValueError:
        print("x is not an integer")

main()

#use of pass to ignore error and ask them again to give integral value

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    try:
        x = int(input("What's x? "))
    except ValueError:
        pass
    else:
        return x

main()

#making def get_int() more general so that it ask watever main is asking it to ask

def main():
    x = int(input("What's x? "))
    print(f"x is {x}")

def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        pass

main()