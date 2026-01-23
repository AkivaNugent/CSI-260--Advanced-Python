'''
Guessing Game Requirements

1. At least one loop
2. three functions with one that pass parameters to another function
3. use a list comprehension to generate a list of numbers and randomly select from this list a number

'''
import random


def GenerateNumber():
    try:
        _range = int(input("Please Select the range of numbers you'd like to guess from (Upper Bound): "))
    except:
        print("your value must be an integer. Defaulting to 100")
        _range = 100

    _rangeArr = [x for x in range(_range)]
    _randNumber = random.choice(_rangeArr)
    return _randNumber


def GuessingLoop(_actual):
    _guessing = True
    _counter = 3
    while _guessing and _counter > 0:
        try:
            _guess = int(input("Please select a integer "))
            _guessing = CheckWin(_guess, _actual, _counter)
            _counter-= 1
        except:
            print("Your input must be an integer")


def CheckWin(_guess, _actual, _counter):
    if _guess > _actual:
        print("Too Large")
        print("Remaining Guesses: " + str(_counter - 1))
    elif _guess < _actual:
        print ("Too Small")
        print("Remaining Guesses: " + str(_counter - 1))
    else:
        print ("WINNER WINNER CHICKEN DINNER")
        return False

    return True


def main():
    print("This is a number guessing Game.")
    GuessingLoop(GenerateNumber())


'''
    _winningNumber = GenerateNumber()
    GuessingLoop(_winningNumber)
'''









if __name__ == "__main__":
    main()