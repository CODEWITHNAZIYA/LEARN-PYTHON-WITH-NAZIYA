# ==========================================
# Mini Project - Notes Manager
# Learn Python With Naziya
# ==========================================

FILE_NAME = "notes.txt"


# -----------------------------
# Add Note
# -----------------------------
def add_note():
    note = input("Enter your note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("\n✅ Note Saved Successfully!")


# -----------------------------
# View Notes
# -----------------------------
def view_notes():

    try:
        with open(FILE_NAME, "r") as file:

            content = file.read()

            if content.strip() == "":
                print("\nNo notes available.")

            else:
                print("\n========== YOUR NOTES ==========\n")
                print(content)

    except FileNotFoundError:
        print("\nNo notes found.")


# -----------------------------
# Clear Notes
# -----------------------------
def clear_notes():

    with open(FILE_NAME, "w") as file:
        pass

    print("\nAll notes cleared successfully.")


# -----------------------------
# Main Menu
# -----------------------------
while True:

    print("\n" + "=" * 40)
    print("         NOTES MANAGER")
    print("=" * 40)

    print("1. Add Note")
    print("2. View Notes")
    print("3. Clear Notes")
    print("4. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        clear_notes()

    elif choice == "4":
        print("\nThank you for using Notes Manager.")
        break

    else:
        print("\nInvalid Choice! Please try again.")