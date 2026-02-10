"""
Guessing Game Requirements.

1. At least one loop
2. three functions with one that pass parameters to another function
3. use a list comprehension to generate a list of numbers and randomly select
   from this list a number

"""
import random


def generate_number():
    """Generate a random number from given range. Default to 100 on failure."""
    try:
        _range = int(input("Please Select the range of numbers you'd like to "
                           "guess from (Upper Bound): "))
    except ValueError:
        print("your value must be an integer. Defaulting to 100")
        _range = 100

    _range_arr = [x for x in range(_range)]
    _rand_number = random.choice(_range_arr)
    return _rand_number


def guessing_loop(_actual):
    """Primary guessing loop."""
    _guessing = True
    _counter = 30
    while _guessing and _counter > 0:
        try:
            _guess = int(input("Please select a integer "))
            _guessing = check_win(_guess, _actual, _counter)
            _counter -= 1
        except ValueError:
            print("Your input must be an integer")
    if _guessing:
        print("BAH BAH.... the number was " + str(_actual))


def check_win(_guess, _actual, _counter):
    """Dheck to see if number selected matches the guess -return boolean."""
    if _guess > _actual:
        print("Too Large")
        print("Remaining Guesses: " + str(_counter - 1))
    elif _guess < _actual:
        print("Too Small")
        print("Remaining Guesses: " + str(_counter - 1))
    else:
        print("WINNER WINNER CHICKEN DINNER")
        return False

    return True


def main():
    """Start game."""
    print("This is a number guessing Game.")
    guessing_loop(generate_number())


if __name__ == "__main__":
    main()
