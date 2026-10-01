# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

# Outputs the original string:
print(f"\nOriginal String: {user_string}")

# Outputs all the string as lower case characters:
print(f"Modified String 1: {user_string.lower()}")

# Outputs all the string as upper case characters:
print(f"Modified String 2: {user_string.upper()}")

# Gets rid of all trailing and leading spaces:
print(f"Modified String 3: {user_string.strip()}")

# Replaces one character with another:
print(f"Modified String 4: {user_string.replace('a', '@')}")

# Makes the first letter capital:
print(f"Modified String 5: {user_string.capitalize()}")

# Reverses the string:
print(f"Modified String 6: {user_string[::-1]}")

# Makes the first letter of every word a capital:
print(f"Modified String 7: {user_string.title()}")

# Outputs the number of characters in the string:
print(f"Modified String 8: {len(user_string)}")

# Outputs the position of the given character:
print(f"Modified String 9: {user_string.find('a')}")

# Outputs the number of the given character:
print(f"Modified String 10: {user_string.count('a')}")

# Outputs True if the string starts with the given word:
print(f"Modified String 11: {user_string.startswith('Hello')}")

# Outputs True if the string ends with the given character:
print(f"Modified String 12: {user_string.endswith('!')}")

# Outputs True if the string is all alphanumeric characters:
print(f"Modified String 13: {user_string.isalnum()}")

# Outputs True if the string is all alphabetic characters:
print(f"Modified String 14: {user_string.isalpha()}")

# Outputs True if the string is all numeric characters:
print(f"Modified String 15: {user_string.isdigit()}")



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!