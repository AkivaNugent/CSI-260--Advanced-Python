import math
import numpy as np
'''
The first goal of this exercise is to triage the list above, named 'nst_lst', so that
a single array named 'new_array' holds only integer values. The second goal is to take
the list named 'new_array' and transform it into a Python array named 'int_array'. The
third goal is to analyze the array and determine the following:
1. its mean
2. the max value in each column
3. the max value in each row
4. The statistical variance of the entire array
5. the standard deviation of the entire array

variance: take each value and substract from it the mean and then square the results
for example, the mean = 12 and the value equals 14. The result is -2, squared = 4
Sum the 4 with all other results and then divide by (total elements -1).

standard deviation: square root of the variance.
'''

def flatten_list(flat_list, original_list):
    for item in original_list:
        if isinstance(item, list):
            flatten_list(flat_list, item)
        else:
            flat_list.append(item)
    return flat_list


def extract_integers(lst):
    int_list = []

    for item in lst:
        if isinstance(item, int) and not isinstance(item, bool):
                int_list.append(item)

    return int_list

def get_dimensions(arr):
    dim = []
    length = len(arr)
    for index in range(math.floor(math.sqrt(length))):
        res, mod = divmod(length, index+1)
        if mod == 0:
            dim.append([index+1, res])
    print(dim)

def basic_analysis(int_array):
    print(int_array)
    print(np.mean(int_array))
    print(np.min(int_array))
    print(np.max(int_array))
    print(np.var(int_array))
    print(np.std(int_array))


def main():
    nst_lst = [
        10, 11, 23,
        [1, 2, 3],
        'a', 'b', 'c', False, 'z', True, 'w',
        [4, 5, 6, 7],
        [True, 'q', 'r', 23.12, 'e', 14.5605],
        [7, 8, 9, 16],
        10, 11, 23,
        [1, 2, 3],
        'a', 'b', 'c', False, 'z', True, 'w',
        [4, 5, 6],
        [True, 'q', 'r', 23.12, 'e', 14.5605],
        [7, 8, 9],
        89, 54, 'c', 10, 2,
        [0, 0, 0, 0, 0, 0]
    ]
    flat_lst = []
    flat_lst = flatten_list(flat_lst, nst_lst)
    new_array = extract_integers(flat_lst)

    get_dimensions(new_array)

    rows = int(input("num of rows (pick from list of it will break. i didn't input validate): "))
    cols = int(len(new_array)/rows)

    int_array = np.array(new_array).reshape(rows,cols)

    basic_analysis(int_array)

if __name__ == '__main__':
    main()