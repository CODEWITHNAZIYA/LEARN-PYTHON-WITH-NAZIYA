# ==========================================
# Mini Project - Student Management System
# Learn Python With Naziya
# ==========================================

students = []

# -------------------------------
# Add Student
# -------------------------------
def add_student():
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    student = {
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)

    print("\n✅ Student Added Successfully!\n")


# -------------------------------
# View Students
# -------------------------------
def view_students():
    if len(students) == 0:
        print("\nNo student records found.\n")
        return

    print("\n===== Student Records =====")

    for index, student in enumerate(students, start=1):
        print(f"\nStudent {index}")
        print("Name   :", student["Name"])
        print("Age    :", student["Age"])
        print("Course :", student["Course"])


# -------------------------------
# Search Student
# -------------------------------
def search_student():
    search_name = input("Enter Student Name: ")

    found = False

    for student in students:
        if student["Name"].lower() == search_name.lower():
            print("\nStudent Found")
            print("Name   :", student["Name"])
            print("Age    :", student["Age"])
            print("Course :", student["Course"])
            found = True
            break

    if not found:
        print("\nStudent Not Found.")


# -------------------------------
# Delete Student
# -------------------------------
def delete_student():
    delete_name = input("Enter Student Name: ")

    for student in students:
        if student["Name"].lower() == delete_name.lower():
            students.remove(student)
            print("\nStudent Deleted Successfully.")
            return

    print("\nStudent Not Found.")


# -------------------------------
# Main Menu
# -------------------------------
while True:

    print("\n" + "=" * 40)
    print("   STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank you for using the program.")
        break

    else:
        print("\nInvalid Choice! Please try again.")