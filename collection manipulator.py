students = []

while True:
    print("\n--- Student Data Organizer ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        print("\nEnter Student Details")

        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth: ")

        subject_input = input("Subjects (comma-separated): ")
        subjects = set(subject_input.split(","))

        # Tuple for ID and DOB
        details = (student_id, dob)

        # Dictionary for student data
        student = {
            "details": details,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(student)

        print("Student added successfully!")

    # Display Students
    elif choice == "2":
        print("\n--- All Students ---")

        for student in students:
            student_id, dob = student["details"]

            print(
                f"ID: {student_id} | "
                f"Name: {student['name']} | "
                f"Age: {student['age']} | "
                f"Grade: {student['grade']} | "
                f"Subjects: {', '.join(student['subjects'])}"
            )

    # Update Student
    elif choice == "3":
        student_id = int(input("Enter Student ID: "))

        for student in students:
            if student["details"][0] == student_id:
                student["age"] = int(input("Enter new age: "))
                student["grade"] = input("Enter new grade: ")

                print("Student updated successfully!")
                break
        else:
            print("Student not found.")

    # Delete Student
    elif choice == "4":
        student_id = int(input("Enter Student ID: "))

        for i in range(len(students)):
            if students[i]["details"][0] == student_id:
                del students[i]
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    # Display Subjects
    elif choice == "5":
        all_subjects = set()

        for student in students:
            all_subjects.update(student["subjects"])

        print("\nSubjects Offered:")
        print(", ".join(all_subjects))

    # Exit
    elif choice == "6":
        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice!")
