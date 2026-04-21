from PIL.SpiderImagePlugin import isInt


def flatten_list(flat_list, original_list):
    for item in original_list:
        if isinstance(item, list):
            flatten_list(flat_list, item)
        else:
            flat_list.append(item)
    return flat_list

nst_lst = [
    10, 11, 23,
    [1, 2, 3],
    'a', 'b', 'c', False, 'z', True, 'w',
    [4, 5, 6],
    [True, 'q', 'r', 23.12, 'e', 14.5605],
    [7, 8, 9],
    10, 11, 23,
    [1, 2, 3],
    'a', 'b', 'c', False, 'z', True, 'w',
    [4, 5, 6],
    [True, 'q', 'r', 23.12, 'e', 14.5605],
    [7, 8, 9],
    89, 54, 'c', 10,
    [0, 0, 0, 0, 0, 0]
]

def breakup_list_by_type(original_list):
    int_list = []
    str_list = []
    bool_list = []
    fl_list = []

    for item in original_list:
        if isinstance(item, int):
            if str(item) == "False" or str(item) == "True":
                bool_list.append(item)
            else:
                int_list.append(item)
        elif isinstance(item, str):
            str_list.append(item)
        elif item != '':
            try:
                item = float(item)
                fl_list.append(item)
            except:
                pass
        else:
            print("Failure")

    return int_list, str_list, bool_list, fl_list

flat_lst = []

flat_lst = flatten_list(flat_lst, nst_lst)

print(nst_lst)
print ("\n flattened \n")
print(flat_lst)

print("\n\n")

int_list, str_list, bool_list, fl_list = breakup_list_by_type(flat_lst)


print(int_list)
print(str_list)
print(bool_list)
print(fl_list)

print(len(int_list) + len(str_list) + len(bool_list) + len(fl_list))
print(len(flat_lst))