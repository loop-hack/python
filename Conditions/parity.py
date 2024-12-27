# using % operator

"""x = int(input("What's x? "))
if x%2 == 0 :
    print("Even")
else :
    print("Odd")
"""

#Defining a function to determine even then calling it main 
#Using Boolean Datatype

def main() :
    x = int(input("What's x? "))
    if is_even(x) :
        print("Even")
    else :
        print("Odd")

def is_even(n) :
    if n%2 == 0 :
        return True
    else :
       return False

main()

#can be simplified as 

def main() :
    if is_even(x) :
        print("Even")
    else :
        print("Odd")

def is_even(n) :
    return True if n%2 == 0 else False

main()