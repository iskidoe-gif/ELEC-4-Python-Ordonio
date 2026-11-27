# JONATHAN L. ORDONIO
# IV-BSIT-B
# P1: Student Grade Calculator
# Nov. 16, 2026


# Accept and validate student grades
def enter_grades():
    grades = []

    while True:
        try:
            count = int(input("How many grades? ")) # Enter the number of grades to be entered
            if count > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.") # validate the input to ensure it is a valid integer

    for i in range(count): # Loop through the number of grades to be entered
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: ")) # Ask the grades input for the specific grade from the user (depends on the count of grades to be entered)

                if 0 <= grade <= 100:
                    grades.append(grade) # put the grade into the grades list if it is within the valid range of 0 to 100
                    break
                else:
                    print("Grade must be from 0 to 100.") # validate the input to ensure it is within the valid range of 0 to 100

            except ValueError:
                print("Invalid input. Enter a number.") # validate the input to ensure it is a valid number

    return grades

# Function to calculate the average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function to find the highest grade
def get_highest_grade(grades):
    return max(grades)


# Function to find the lowest grade
def get_lowest_grade(grades):
    return min(grades)


# Function to check if the student passed
def check_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function to display the results
def show_results(grades):
    if len(grades) == 0:
        print("\nPlease enter grades first.")
        return

    print("\n===== GRADE RESULTS =====")
    print("Grades:", grades)
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest: {get_highest_grade(grades):.2f}")
    print(f"Lowest: {get_lowest_grade(grades):.2f}")
    print(f"Status: {check_status(grades)}")



# Main function for the menu
def main():
    grades = []

    # Repeat the menu until the user exits
    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            grades = enter_grades()
            print("Grades saved successfully!")

        elif choice == "2":
            show_results(grades)

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
main()


# A local variable is created inside a function and can only
# be used within that function.
# For example, average is a local variable in check_status().
# A global variable is created outside functions and can be
# accessed by different functions.
# This program uses local variables and passes grades as
# parameters instead of using a global variable.