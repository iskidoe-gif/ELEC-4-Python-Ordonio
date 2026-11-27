# Jonathan L. Ordonio
# IV-BSIT-B
# P4: Safe Menu Program
# Nov. 27, 2026

# Division
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

# Open and Read File
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


# Main Menu
def main():
    while True:
        print("\n" + "=" * 45)
        print("          EXCEPTION HANDLING SYSTEM")
        print("=" * 45)
        print("  [1] Division Calculator")
        print("  [2] Open and Read File")
        print("  [3] Exit Program")
        print("=" * 45)

        choice = input("  Enter your choice (1-3): ").strip()

        if choice == "1":
            division()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("\nThank you for using the program!")
            print("Program terminated.")
            break

        else:
            print("\n[ERROR] Invalid menu choice!")
            print("Please select only from 1 to 3.")

# Run the program
if __name__ == "__main__":
    main()

