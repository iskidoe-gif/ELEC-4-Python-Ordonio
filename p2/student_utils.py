# JONATHAN L. ORDONIO
# IV-BSIT-B
# P2: Custom Module: student_utils
# Nov. 19, 2026

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
