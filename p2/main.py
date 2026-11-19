# JONATHAN L. ORDONIO
# IV-BSIT-B
# P2: Custom Module: student_utils
# Nov. 19, 2026

from student_utils import calculate_average
from student_utils import get_highest_grade
from student_utils import get_lowest_grade
from student_utils import check_status
import random

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
print("Entered Grades:", student_grades)

# Function to display the results
def show_results(grades):
    if len(grades) == 0:
        print("\nPlease enter grades first.")
        return

    print("\n===== GRADE RESULTS =====")
    print(f"Hello, {random.choice(['Allen', 'Mark', 'Gilbert', 'Juan', 'John'])}!, your grades are: {student_grades}") # Example usage of the built-in random module
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest: {get_highest_grade(grades):.2f}")
    print(f"Lowest: {get_lowest_grade(grades):.2f}")
    print(f"Status: {check_status(grades)}")

show_results(student_grades)