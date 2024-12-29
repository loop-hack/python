for _ in range(3):
    print("#")

#difining a function to make stack of block of certain height like 5 block

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()

#or we can also define function as this , its up to us

def main():
    print_column(3)

def print_column(height):
    print("#\n"*height,end="")

main()

#printing in rows like blocks in row

def main():
    print_row(4)

def print_row(length):
    print("?"*4)

main()


#how build grid of 3*3 of blocks

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()

main()