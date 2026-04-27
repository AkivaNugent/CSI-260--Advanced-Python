import math
#squares = [1, 4, 9, 25, 36, 49, 64, 81, 100]
sq_rts = [math.sqrt(n) for n in range(1, 100)]

'''
code above was provided so i didn't want to change it, but the list
comprehension does not give us sqrt(100) as the line above indicates but does 
give sqrt(16) which is another unlisted perfect square. 
'''


def filter_whole(lst):
    """
    Take in a list of floats and returns only numbers who are whole.
    """
    return [x for x in lst if x == int(x)]

filtered_sq_rts = filter_whole(sq_rts)

for sqr in filtered_sq_rts:
    print(sqr)
