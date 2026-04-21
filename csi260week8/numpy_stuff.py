import numpy as np

#Source: https://devopscube.com/numpy-practical-examples/
#Open source reference: https://numpy.org

myarr = [
    [1,2,3,4],
     [1,2,3,3],
     [3,1,1,3]
]

#Max/min search of an array
# Creating 5x4 array
array = np.arange(20).reshape(5, 4) #First value is the length, second is row value
print("The array based on the dimensions provided: ")
print(array)
print() #Forces a space

# If no axis mentioned, then it works on the entire array
print("Max of an array: ",np.argmax(array))

# If axis=1, then it works on each row
print(np.argmax(array, axis=1))

# If axis=0, then it works on each column
print(np.argmax(array, axis=0))

'''
Numpy sorting
'''
# Sort the whole array
print("The entire array (list):",np.sort(array, axis=None))

# Sort along each row
print("The entire array (list) according to the dimensions set:")
print(np.sort(array, axis=1))

# Sort along each column
print(np.sort(array, axis=0))

array = np.array([28, 13, 45, 12, 4, 8, 0])
print(array)

print(np.argsort(array)) #This printed a sorted list of index values, max to min
print()
'''
How to find the mean of every array (list)
'''
list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]

result = []
for i in range(len(list)):
    result.append(np.mean(list[i]))
print("The means are:",result)
print()
'''
How to add an additional array (list) to a collection
'''
array = np.array([
    [3, 2, 8],
    [4, 12, 34],
    [23, 12, 67]
])

newRow = np.array([2, 1, 8])
newArray = np.vstack((array, newRow))
print(newArray)

'''
How to add a column to the data
'''
array = np.array([
    [3, 2, 8],
    [4, 12, 34],
    [23, 12, 67]
])

newColumn = np.array([2, 1, 8])
newArray = np.column_stack((array, newColumn))
print([3, 2, 8])
print([4, 12, 34])
print([23, 12, 67])
print("Wow, your instructor is a genius!")
print(newArray)
print()
'''
How to reverse a Numpy array
'''
array = np.array([3, 6, 7, 2, 5, 1, 8])
reversedArray = np.flipud(array)
print(reversedArray)

'''
How to multiply two matrices
'''
matrix1 = [
    [3, 4, 2],
    [5, 1, 8],
    [3, 1, 9]
]

matrix2 = [
    [3, 7, 5],
    [2, 9, 8],
    [1, 5, 8]
]

result = np.dot(matrix1, matrix2)
print('The product of the two matrices equals')
print(result)


'''
The problem statement is given n, print the checkerboard pattern
for a nxn matrix considering that 0 for black and 1 for white.
'''
n = 8
print()
# Create a nxn matrix filled with 0
matrix = np.zeros((n, n), dtype=int)

# fill 1 with alternate rows and column
matrix[::2, 1::2] = 1
matrix[1::2, ::2] = 1

# Print the checkerboard pattern
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()