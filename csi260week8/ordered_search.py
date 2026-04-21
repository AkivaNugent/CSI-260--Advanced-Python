#Data Validation - string functions
'''
All functions return either a True or False
isalpha() - Confirm that the data contains only letters AND is not blank

isalnum() - Confirm that the data contains only letters and/or numbers AND is not blank

isdecimal() - Confirms the data contains only integers AND is not blank

isspace() - Confirms the data contains only spaces, tabs and new lines AND is not blank

istitle() - Confirms the data is all string and the first letter is upper case followed by lower case letters AND no
blanks
'''

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
#Identify the search item's data type. Pass
# the results of this function to checkValue()
def dataType():
    inp = input("What is the search criteria?")
    if(inp.isdigit()):
        inp = int(inp)
        print("Integer conversion successful")
    elif(inp == "True" or inp == "true"):
        inp = True
        print("Boolean conversion to True successful")
    elif (inp == "False" or inp == "false"):
        inp = False
        print("Boolean conversion to False successful")
    elif(inp.isalpha()):
        print("String value.")
    elif (inp.isalnum()):
        print("Garbage input, you're done.")
    elif (inp != ''):
        try:
            inp = float(inp)
            print("Float conversion successful")
        except:
            pass
    else:
        print("Failure")
    return inp

#dataType()
'''
#Convert input to its proper data type
def checkValue():
    pass
'''

#Based on the value and its data type, search
#for it in the data set

def searchItem():
    x = dataType()
    count = 0
    for i in nst_lst:
        if (isinstance(i, list)):
            for j in i:
                if (x == j and type(j) == type(x)):
                    count += 1
                else:
                    pass
        elif (i == x and type(i) == type(x)):
            count += 1
        else:
            count += 0
    if (count == 0):
        print("Element not found")
    elif (count > 0):
        print("The element", x, 'was found', count, 'times.')
    else:
        print("Process failed.")

searchItem()