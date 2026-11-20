with open("students.txt", "w") as file:
    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("Enter student name: ")
        usn = input("Enter USN: ")
        file.write(name + " " + usn + "\n")

with open("students.txt", "r") as file:
    print("\nStudent Details:")
    print(file.read())
