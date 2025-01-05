'''with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


"""instead of storing splitted string in list we can use it by storing it veriable"""

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        print(f"{name} is in {house}")

#for shorting 

students = []

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
for student in sorted(students):
    print(student)

'''

"""previous code is not upto that mark because we are sorting whole sentece 
we want to short by name , we just got lucky bcs name was first in sentance"""

students = []

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students,key=get_name):
    print(f"{student['name']} is in {student['house']}")

'''we can shorten this up by shortening the way we have defined dictionary student{}'''

students = []

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        student = {"name": name, "house":house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

for student in sorted(students,key=get_name):
    print(f"{student['name']} is in {student['house']}")

"""for sorting by name of house from Z to A"""

for student in sorted(students,key=get_house,reverse=True):
    print(f"{student['name']} is in {student['house']}")

'''we are creating a function or not using it twice for this we can short these code
by using lmbda that creates instance function just like we used _ for unsuded variable in for loop'''

students = []

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        student = { "name": name,"house":house}
        students.append(student)

for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")


'''let's say we have more than one comma in line .. in our csv file we have data something like
1)Ankit,Ambedkarnagar , Budhauli,Sheikhpura [3comma](2)Ron,The Burrow [1 comma] then how we gonna print name and adress'''

import csv 

students = []

with open("students2.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        home = ", ".join(row[1:])
        students.append({"name":name,"home":home})

for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

'''we have some changes in our .csv file in first row i wrote name,house to make it useful for 
dictreader that is creating entire file into dictionary'''

import csv 

students = []

with open("students2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name":row['name'],"home":row['home']})

for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")