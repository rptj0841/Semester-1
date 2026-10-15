# Worksheet 1.2: Task 1 Solution

import sys

try:
    grade = int(input("Enter grade in range 0-100: "))
    if grade < 0 or grade > 100:
        sys.exit("Error: Grade must be an integer between 0 and 100")
    
    if grade < 40:
        print(f"{str(grade)} is a Fail")
    elif grade < 70:
        print(f"{str(grade)} is a Pass")
    else:
        print(f"{str(grade)} is a Distinction")
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100")
