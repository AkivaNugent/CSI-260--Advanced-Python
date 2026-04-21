import numpy as np

array = [
    [1, 34, 67, 2, 3],
    [1, 0, 2, 9, 10],
    [5, 8, 5, 6, 2],
    [4, 0, -999, 23, 8]
]
'''
print("Total number of rows equals:",len(array))
print("Total number of columns equals:",len(array[0]))
print("Total number of elements equals:",len(array)*len(array[0]))
print("The index positions to reference lie between 0 and ",len(array)*len(array[0])-1)

print("Look at this value:",array[1][2])

print("Max of an array: ",np.argmax(array))
print(array[0][2])
print("Min value of the array: ",np.argmin(array))

# If axis=1, then it works on each row
print('The max value for each row is in the following index positions:',np.argmax(array, axis=1))

# If axis=0, then it works on each column
print('The max value for each column is in the following index positions:',np.argmax(array, axis=0))
'''
#Confirm all data is an integer data type
n = 2
count = 0
for i in array:
    for j in i:
        if(type(j) != type(n)):
            count += 1
        else:
            pass
if(count == 0):
    print("Clean integer data")
else:
    print("Data cleanup required")