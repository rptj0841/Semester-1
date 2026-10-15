# Worksheet 1.2: Task 2 Solution

import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

print(f"Minimum = {min(numbers)}")
print(f"Maximum = {max(numbers)}")
print(f"Mean = {sum(numbers)/len(numbers)}")

numbers.sort()

if len(numbers) % 2 != 0:
    print(f"Median = {numbers[len(numbers)//2]}")
else:
    median = (numbers[len(numbers)//2] + numbers[len(numbers)//2 -1] ) / 2
    print(f"Median = {median}")