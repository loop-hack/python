with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


"""instead of storing splitted string in list we can use it by storing it veriable"""

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        print(f"{name} is in {house}")