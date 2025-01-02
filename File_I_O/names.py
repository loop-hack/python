'''names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")
'''

#open() is used to store data given in terminal

name = input("What's your name? ")
file = open("name.txt","w")
file.write(name)
file.close()