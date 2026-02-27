import numpy as np
'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
'''


a = np.zeros(5)
print(a)

a_2D = np.zeros((4,3))
print(a_2D)

a = np.ones(5)
print(a)

a_2D = np.ones((4,3))
print(a_2D)

a= np.arange(10)
print(a)


a= np.arange(1,10,2)
print(a)

a= np.linspace(0,10,num=5,endpoint=False)
print(a)

a= np.linspace(0,10,num=5,endpoint=True)
print(a)


a=np.random.rand(5)
print(a)

a=np.random.rand(2,3)
print(a)


a=np.random.rand(2,3,4)
print(a)


a=np.empty((2,3),int)
print(a)

a = np.full((2,4),3)
print(a)

#numpy.eye()
#create identity matrix-have 1 in diagonal elements
identity_matrix = np.eye((4))
print(identity_matrix)


#square identitu matrix
identity_matrix = np.identity((5))
print(identity_matrix)

Matrix = np.array([[10,20,30],[40,50,60],[70,80,90]])
print("\nOriginal matrix: \n",Matrix)
Diagonal_elements = np.diag(Matrix)
print("\nDiagonal elements : ",Diagonal_elements)


matrix = np.array([2,3,4,5])
print(matrix)
print(np.diag(matrix))


