# Jonathan L. Ordonio
# IV-BSIT-B
# P4: Safe Menu Program
# Nov. 27, 2026

def division():
    print("\n========== DIVISION CALCULATOR ==========")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    # Validate the input to ensure it is a valid number 
    except ValueError:
        print("\n[ERROR] Invalid input! Please enter numeric values.")
    # Validate the input to ensure it is not dividing by zero
    except ZeroDivisionError:
        print("\n[ERROR] Cannot divide a number by zero.")

    # If there are no exceptions, display the result of the division
    else:
        print(f"\n[RESULT] {num1} / {num2} = {result}")

    # This block will always execute, regardless of whether an exception occurred or not
    finally:
        print("\nDivision operation completed.")
        print("=========================================")

# division()

# 2. Open and Read File
def open_file():
    print("\n========== FILE READER ==========")

    filename = input("Enter file name: ").strip()

    try:
        with open(filename, "r") as file:
            contents = file.read()

    except FileNotFoundError:
        print(f"\n[ERROR] The file '{filename}' was not found.")

    else:
        print("\n[FILE CONTENTS]")
        print("---------------------------------")
        if contents:
            print(contents)
        else:
            print("The file is empty.")
        print("---------------------------------")

    finally:
        print("\nFile operation completed.")
        print("=================================")

open_file()