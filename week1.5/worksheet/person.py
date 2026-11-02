# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a Person, given their name and date of birth
        """
        # Write a constructor here to create and initialize name and
        # birth fields (see README.md for further details)
        
        if not isinstance(name, str):
            raise TypeError("Name has to be a string")
        if name == "":
            raise ValueError("Name can't be an empty string")

        if not isinstance(birth, date):
            raise TypeError("Date of birth must be a date object")

        self.name = name
        self.birth = birth


    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        """
        Returns a string of the first letters of each part of the given name to represent their initials.
        """
        string = ""
        next = True
        for i in range(len(self.name)):
            if next == True:
                string += (self.name[i].upper())
            if self.name[i] == " ":
                next = True
            else:
                next = False
        return string

    def is_birthday(self):
        """
        Returns True if today is the person's birthday, returns False otherwise
        """
        if self.birth.day == date.today().day and self.birth.month == date.today().month:
            return True
        else:
            return False


