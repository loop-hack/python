"""# while lopp

i = 3
while i != 0:
    print("Meow")
    i = i - 1


#for loop

for i in [0,1,2]:
    print("meow")

#we are not using i in code thats why replce it by _

for _ in range(3):
    print("meow")


#for print meow 3 times we can also do

print("meow"*3)  #output meowmeowmeow

print("meow\n"*3) #output one extra newline bcz by default print has newline

print("meow\n"*3,end="")


#when u take users input of specific type

while True:
    n = int(input("What's n? "))
    if n>0:
        break
for _ in range(n):
    print("meow")
"""


#lets do the same problem by defining a function

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n>0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()