def mean(numList):
    """ This function accepts a list of integers and returns the mena average of the list"""
    total = 0
    for i in range(len(numList)):
        total += numList[i]
    average = total / len(numList)
    return average

numbers = [2, 5, 7, 8, 8, 3, 23, 12]
print(f"The average of the numbers in the list is {mean(numbers)}")