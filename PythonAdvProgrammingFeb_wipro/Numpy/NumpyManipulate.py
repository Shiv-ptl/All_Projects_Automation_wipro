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


a = np.array([[1,2],[3,4]])
b =np.array([[5,6],[7,8]])

print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=1))


#stack - join the array along the new axis
#adds a new diamention
a = np.array([1,2,3])
b=np.array((['x','y','z']))

print(np.stack((a,b),0))

print(np.stack((a,b),1))

#hstack - stacks arrays horizontally(column wise)

print(np.hstack((a,b)))
print(np.concatenate((a,b),axis=0))


#vstack
print(np.vstack((a,b)))
a = np.array([[1,2],[3,4]])
b =np.array([[5,6],[7,8]])
print(np.vstack((a,b)))


#column stack() - stack 1d array into 2D array

a = np.array([1,2,3])
b=np.array((['x','y','z']))
print(np.column_stack((a,b)))


print(np.hstack((a,b)))
print(np.vstack((a,b)))


import numpy as np

arr = np.array([1,2,3,4,5,6])

result = np.split(arr, 3)
print(result)


arr2 = np.array([[1,2,3,4],
                 [5,6,7,8]])

print(np.hsplit(arr2, 2))


arr3 = np.array([[1,2],
                 [3,4]])

print(np.vsplit(arr3, 2))


import numpy as np

# ----------------------------------------
# 1. SPLIT (Equal division only)
# ----------------------------------------
print("\n--- np.split() ---")

arr = np.array([1,2,3,4,5,6])
result = np.split(arr, 3)

print("Split into 3 equal parts:")
print(result)


# ----------------------------------------
# 2. ARRAY_SPLIT (Unequal allowed)
# ----------------------------------------
print("\n--- np.array_split() ---")

arr2 = np.array([1,2,3,4,5])

# This works even if not divisible equally
result2 = np.array_split(arr2, 3)

print("Split into 3 parts (unequal allowed):")
print(result2)


# ----------------------------------------
# 3. HSPLIT (Horizontal split - columns)
# ----------------------------------------
print("\n--- np.hsplit() ---")

arr3 = np.array([[1,2,3,4],
                 [5,6,7,8]])

result3 = np.hsplit(arr3, 2)

print("Horizontal split:")
print(result3)


# ----------------------------------------
# 4. VSPLIT (Vertical split - rows)
# ----------------------------------------
print("\n--- np.vsplit() ---")

arr4 = np.array([[1,2],
                 [3,4]])

result4 = np.vsplit(arr4, 2)

print("Vertical split:")
print(result4)


# ----------------------------------------
# 5. DSPLIT (Depth split - 3D arrays)
# ----------------------------------------
print("\n--- np.dsplit() ---")

arr5 = np.array([[[1,2],
                  [3,4]],

                 [[5,6],
                  [7,8]]])

result5 = np.dsplit(arr5, 2)

print("Depth split:")
print(result5)

#resize()- returns a new array with a special shape
arr = np.array([1,2,3,4,5,6,7,8,9])
nw_arr = np.resize(arr,(2,5))
print(nw_arr)

#append()

arr = np.array([1,2,3,4,5,6,7,8,9])
new_arr =np.append(arr,[4,5])
print(new_arr)

a = np.array([[1,2],[3,4]])
b =np.array([[5,6],[7,8]])
np.append(a,b,0)

arr = np.array([10,20,30])
new_arr = np.insert(arr,2,15)
print(new_arr)

arr = np.array([10,20,30])
new_arr = np.delete(arr,2)
print(new_arr)


arr = np.array([1,2,3,4,4])
print(np.unique(arr))

#repeating
#repeat is used tp repeat each element of an array a specified number of times

arr = np.array([1,3,5])
print(arr)

print(np.repeat(arr,3))

#different repeats for each element
arr= np.array([10,15,20,25])
print(arr)

print(np.repeat(arr,[1,2,3,1]))

arr = np.array([[2,3],[4,5]])
print(arr)
print(np.repeat(arr,2,0))

my_array = np.array([1,2,3])
tiled_array = np.tile(my_array,2)
print("Original array:\n",my_array)
print("Tiled array :\n",tiled_array)


arr= np.array([10,15,20,25])
print(arr)
print(np.flip(arr))


arr = np.array([[2,3],[4,5]])
print(arr)
print(np.flip(arr,0))#flip rows
print(np.flip(arr,1))#flip columns


arr = np.array([[2,3,1],[4,5,7]])
print(arr)
print(np.fliplr(arr))#flip left rigth(axis=1) - works only on 2D array

print(np.flipud(arr))# Flip Up-Down(axis=0)

print(np.roll(arr,2,None))#roll - rotate elements along given axis


#Sorting and Searching

# ----------------------------------------
# 1. sort() → Returns sorted copy of array
# ----------------------------------------
arr = np.array([5, 2, 9, 1])

sorted_arr = np.sort(arr)

print("Sorted Array:")
print(sorted_arr)


# ----------------------------------------
# 2. argsort() → Returns indices of sorted order
# ----------------------------------------

arr = np.array([5, 2, 9, 1])

sorted_arr = np.sort(arr)
print("\nSorted Array:")
print(sorted_arr)

indices = np.argsort(arr)

print("Indices that would sort the array:")
print(indices)


# ----------------------------------------
# 3. lexsort() → Multi-level sorting
# Sort by 'a' first, then by 'b'
# Sorting happens from RIGHT → LEFT
# ----------------------------------------

a = np.array([1, 1, 0, 0])
b = np.array([1, 0, 1, 0])

result = np.lexsort((b, a))

print("\nLexsort Result (multi-level sort):")
print(result)


#Changing Dimensions
