# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
# It will print whichever items that are present in both sets.

both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
# It prints all the items in both sets but becasue one of them is in both, it will only output it once.

food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("strawberry")
print(fruit)

# Remove an item from vegetables
vegetables.discard("leek")
print(vegetables)

# Find and display symmetric difference of the two sets
# This returns what is in either list but not in the intersection

fruit.symmetric_difference(vegetables)