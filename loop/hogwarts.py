#using list for for loop

students = ["Hermione", "Harry","Ron"]
for student in students:
    print(student)

#using len and i for for loop iteration

students = ["Hermione", "Harry","Ron"]
for i in range(len(students)):
    print(students[i])

#we can do more with this like i can add rank like whose 1,2,3

students = ["Hermione", "Harry","Ron"]
for i in range(len(students)):
    print(i + 1, students[i])


#dictionary {}

students = { "Hermione":"Griffindor",
            "Harry":"Griffindor",
            "Ron":"Griffindor",
            "Draco":"Slytherin" }

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

#improvement in code 

students = { "Hermione":"Griffindor",
            "Harry":"Griffindor",
            "Ron":"Griffindor",
            "Draco":"Slytherin" }

for student in students:
    print(student) 


"""only key will print from here we can say 
in students elements are only key not value both together
"""

# to print both house and name of students we should do

students = { "Hermione":"Griffindor",
            "Harry":"Griffindor",
            "Ron":"Griffindor",
            "Draco":"Slytherin" }

for student in students:
    print(student,students[student],sep=", ")


students = [
    {"name":"Hermione","House":"Gryffindor","patronus":"Otter"},
    {"name":"Harry","House":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","House":"Gryffindor","patronus":"Jack Russell terrier"},
    {"name":"Draco","House":"Slytherin","patronus":None}
]

for student in students:
    print(student["name"],student["House"],student["patronus"],sep=", ")