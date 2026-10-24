"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""
try:
    destination = input("Where are you going to? ")

    distance_miles_input = int(input("How many miles will you travel? "))
    time_hours_input = int(input("How many hours will the journey take? "))

    # TODO: calculate the average speed in miles per hour
    averageSpeed = distance_miles_input/time_hours_input
    # TODO: print a summary message using an f-string
    print(f"You will reach your destination, {destination}, at and average speed of {averageSpeed:.2f} miles per hour.")
except ZeroDivisionError:
    print("Sorry, can't divide by 0.")
# Extension: add validation for zero or negative values
