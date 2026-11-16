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
student_grades = enter_grades()
print("Entered Grades:", student_grades) # display the entered grades

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

show_results(student_grades) # display the results of the entered grades