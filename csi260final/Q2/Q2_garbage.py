import numpy as np

str_stuff = []
fl_stuff = []
bool_stuff = []
int_stuff = []

int_array = []

int_lst= [9, 6, 7, False,
          14, 5, 'a', 'Z', 2,
          3, False, 28, 1, 'm',
          10, True, 'b', 14.02,
          11, 'f', 'r', 42, 13,
          34, 25, 46]

def q2_Output(mixed_lst):
    """
    Separate items from list into respective datatype lists
    """
    int_list = []
    float_list = []
    str_list = []
    bool_list = []

    for item in mixed_lst:
        if isinstance(item, int) and not isinstance(item, bool):
            int_list.append(item)
        elif isinstance(item, bool):
            bool_list.append(item)
        elif isinstance(item, float):
            float_list.append(item)
        elif isinstance(item, str):
            str_list.append(item)

    return int_list, str_list, float_list, bool_list

def calculate_metrics(int_array):
    mean = np.mean(int_array)
    median = np.median(int_array)
    variance = np.var(int_array)
    std_dev = np.std(int_array)

    return mean, median, variance, std_dev


def print_results(int_stuff, str_stuff, fl_stuff, bool_stuff,
                  int_array,
                  mean, median, variance, std_dev):
    print("PART 1 RESULTS")
    print(int_stuff)
    print(str_stuff)
    print(fl_stuff)
    print(bool_stuff)

    print('\n\nPART 2 RESULTS')
    print(int_array)

    print("\n\nPART 3 RESULTS")
    print(f'Average/Mean: {mean}')
    print(f'Median: {median}')
    print(f'Variance: {variance}')
    print(f'Standard Deviation: {std_dev}')


int_stuff, str_stuff, fl_stuff, bool_stuff = q2_Output(int_lst)
int_array = np.array(int_stuff).reshape(4,4)
mean, median, variance, std_dev = calculate_metrics(int_array)
print_results(int_stuff, str_stuff, fl_stuff, bool_stuff,
                  int_array,
                  mean, median, variance, std_dev)
