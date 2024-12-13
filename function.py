#function creation

def add_numbers(a, b):
      sum = a + b
      return sum

result= add_numbers(5,3)
print(result)

#printing name and assigning variable the input given by users:

name= input("What is your name? ")
print(f"Hello, {name}")


#using strip() and capitalize() function

name= input("What is your name? ")
name = name.strip()
name= name.capitalize()
print(f"Hello, {name}")

#using strip() and title() for capitalizing name and making it redable

name= input("What is your name? ").strip().title()
print(f"Hello, {name}")

#using split()

name = input("What is your name? ").strip().title()
first,last = name.split(" ")
print(f"Hello, {first}")
