import  numpy as np

a = np.arange(1,7)
print("Original array: ",a)

reshaped = a.reshape(6,1)#reshape the array
print("reshaped array: ",reshaped)

arr = np.array([[1,2],[3,4]])
for x in arr.flat:
    print(x)

arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.flatten()#returns a copy of the array collapsed in one diamention
print(at_arr)

arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.ravel()#returns a flattened array
print(at_arr)

#pad - Returns a padded array with shape increased according to pad_width
arr = np.array([1,2,3,4])
print(arr)

padded = np.pad(arr,3,mode='constant')
print(padded)
padded = np.pad(arr,3,mode='symmetric')
print(padded)
padded = np.pad(arr,3,mode='reflect')
print(padded)

''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)
# transpose = arr.transpose()
# print(transpose)
#
# #2 ndarray.T
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)
# transpose = arr.T
# print(transpose)
#
# #rollaxis - Rolls the specified axis backwards
#
# arr = np.zeros((2,3,4))
# print(arr)
#
# # 2 is the blocks - axis 0
# # 3 - rows - axis 1
# # 4 columns - axis 2
#
# #(0,1 ,2) - (2,3,4)
# #(2,0,1) - (4,2,3)
#
# #arr[block][row][column]
#
# new_arr = np.rollaxis(arr, 2)
# print(new_arr)
#
# #swapaxes() - Interchanges two axes of an array.
# #$Axis 0 and Axis 2 swapped.
# arr = np.zeros((2,3,4))
# print(arr)
#
# new_arr = np.swapaxes(arr, 0 , 2)
# print(new_arr)
# # (4 3, 2)
#
# #moveaxis() - Moves specified axes to new positions.
# arr = np.zeros((2,3,4))
# print(arr)
# new_arr = np.moveaxis(arr, 0, -1)
# print(new_arr)
#
# # (3 ,4 2)


# 1 Tanspose
# reorder the dimention of an array

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original array:\n",arr)
transpose=arr.T
#transpose=arr.transpose()
print("Transposed array: \n",transpose)


arr = np.zeros((2,3,4))
print(arr)

print("\n\t-----Roll axis-----\n")

new_arr = np.rollaxis(arr,2)
print(new_arr)


arr = np.zeros((2,3,4))
print(arr)

print("\n\t-----Swapaxes-----\n")

new_arr = np.swapaxes(arr,0,2)
print(new_arr)


arr = np.zeros((2,3,4))
print(arr)

print("\n\t-----move axis-----\n")

new_arr = np.moveaxis(arr,0,-1)
print(new_arr)