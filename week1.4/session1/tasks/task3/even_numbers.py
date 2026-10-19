def even_numbers(num):
    """
    This function accepts an integer value
    and returns a list of even integers between 0 and that value
    """

    evenList = []
    for i in range(0,num+1,2):
        evenList.append(i)
    return evenList

num = int(input("Enter number: "))
print(f"Even numbers between 0 and {num} are {even_numbers(num)}")