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