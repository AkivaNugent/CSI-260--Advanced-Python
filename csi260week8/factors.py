import numpy as np

def find_factors():
    """
    Finds all factors of a given integer.

    Args:
        number: The integer for which to find factors.

    Returns:
        A list of factors.
    """
    factors = []
    # Loop from 1 up to and including the number
    try:
        number = int(input("Enter the total number of elements you want to insert into the array: "))
        for i in range(1, number + 1):
        #Check if 'number' is perfectly divisible by 'i'
            if number % i == 0:
                factors.append(i)
            else:
                pass
        getElements(number, factors)

    except:
        l = len(factors)
        if (l > 0):
            getElements(number, factors)
        else:
            ValueError("Please enter a valid integer.")
            find_factors()


def getElements(number, factors):
    print("\nThe factors of",number," are: ",factors)
    selectElements(number)

def selectElements(number):
    rows = int(input("Enter number of rows: "))
    cols = int(number/rows)
    #cols = int(cols)
    print("Given the number of rows equals",rows, " the columns are set to ",cols)
    array = np.arange(number).reshape(rows, cols)  # First value is the length, second is row value
    print("The array based on the dimensions provided: ")
    print(array)

find_factors()