students = []

while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        students.append({
            "name": name,
            "age": age,
            "course": course
        })

        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for i, student in enumerate(students, 1):
                print(f"\nStudent {i}")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])

    elif choice == "3":
        name = input("Enter student name: ")

        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                print(student)
                found = True

        if not found:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter student name to delete: ")

        for student in students:
            if student["name"].lower() == name.lower():
                students.remove(student)
                print("Student deleted!")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")