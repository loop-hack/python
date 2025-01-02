names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")


#open() is used to store data given in terminal

name = input("What's your name? ")
file = open("name1.txt","w")
file.write(name)
file.close()


#"a" for appending that will store ever input given

name = input("What's your name? ")
file = open("name2.txt","a")
file.write(name)
file.close()


"""output : AnkitDavidRam bcz 'a' 
doesn't add new line after each input"""

name = input("What's your name? ")
file = open("name3.txt","a")
file.write(f"{name}\n")
file.close()


# to read "r"

with open("name3.txt","r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,",line.rstrip())
