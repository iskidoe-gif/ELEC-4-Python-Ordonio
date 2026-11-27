# Jonathan L. Ordonio
# IV-BSIT-B
# P3: Student Record Manager
# Nov. 27, 2026

students = []
student_set = set()


# 1. Add a student
def add_student():
    name = input("\nEnter student name: ").strip() # Remove leading and trailing whitespace from the input name

    if not name:
        print("\n[!] Student name cannot be empty.")
        return

    normalized_name = name.casefold() # Normalize the name for case-insensitive comparison

    if normalized_name in student_set:
        print(f"\n[!] {name} already exists in the records.") # Check if the student already exists in the records
    else:
        students.append(name) # Add the student to the list
        student_set.add(normalized_name) # Add the normalized name to the set for future checks
        print(f"\n[+] {name} has been successfully added!")


# 2. Remove a student
def remove_student():
    name = input("\nEnter the student name to remove: ").strip()

    if not name:
        print("\n[!] Please enter a valid name.")
        return

    normalized_name = name.casefold()

    for student in students:
        if student.casefold() == normalized_name: # Check if the normalized name matches any student in the list
            students.remove(student) # Remove the student from the list 
            student_set.remove(normalized_name) # Remove the normalized name from the set
            print(f"\n[+] {student} has been removed successfully!")
            return

    print(f"\n[!] {name} was not found in the records.") 


# 3. Search for a student
def search_student():
    keyword = input("\nEnter student name or keyword: ").strip()  # search for a student by name or keyword

    if not keyword:
        print("\n[!] Please enter a search keyword.")
        return

    matches = [
        student for student in students
        if keyword.casefold() in student.casefold() # Check if the normalized keyword is present in the normalized student name
    ]

    # Display search results
    print("\n" + "=" * 45) 
    print("             SEARCH RESULTS")
    print("=" * 45)

    # Display the matching students
    if matches:
        for number, student in enumerate(
            sorted(matches, key=str.casefold), start=1
        ):
            print(f"  {number}. {student}")

        print(f"\n  Total matches: {len(matches)}")
    else:
        print("  No matching student found.")

    print("=" * 45)


# 4. Display all students
def display_students():
    print("\n" + "=" * 45)
    print("             STUDENT RECORDS")
    print("=" * 45)

    if not students:
        print("  No student records available.")
    else:
        sorted_students = sorted(students, key=str.casefold) # Sort the students in alphabetical order (case-insensitive)

        for number, student in enumerate(sorted_students, start=1): # Display the sorted students with their corresponding numbers
            print(f"  {number}. {student}")

        print("-" * 45) 
        print(f"  Total Students: {len(students)}") 

    print("=" * 45)

# Menu options
def menu():
    while True: 
        print("\n" + "=" * 45)
        print("             STUDENT RECORD MANAGEMENT")
        print("=" * 45)
        print("  1. Add Student")
        print("  2. Remove Student")
        print("  3. Search Student")
        print("  4. Display All Students")
        print("  5. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-5): ").strip() # remove leading and trailing whitespace from the input choice

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("\n[+] Exiting the program...")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()

# List can contain duplicate elements. Meanwhile, Set  contain only unique elements and removes duplicates automatically. 
# In this program, we use a list to store the student names in the order they were added,
# while we use a set to keep track of unique student names for quick existence checks. 
# This combination allows management of the student records while ensuring that no duplicate names are added.