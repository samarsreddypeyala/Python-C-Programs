 # Importing numpy as np
import numpy as np
# to get eig() function
from numpy import linalg as rkv 
#creating an array using diag function
A = np.array([[6, 1, 1],[4, -2, 5],[2, 8, 7]])
B = np.diag((1, 2, 3))
#array of complex numbers
com=np.array([[1, -2j], [2j, 5]])
#Print the created arrays
print("\nmatrix A:\n",A)
print("\nmatrix B:\n",B)
print("\ncomplex matrix:\n",com)
#Get the dimensions of arrays
print("\ndimention of matrix A:",A.ndim)
print("\ndimention of matrix B:",B.ndim)
print("\ndimention of complex matrix:",com.ndim)
#Get the shape of arrays
print("\nshape of matrix A:",A.shape)
print("\nshape of matrix B:",B.shape)
print("\nshape of complex matrix:",com.shape)
#Arithmetic operations using functions
print("\nADDITION of A,B matrices:\n",np.add(A,B))
print("\nSUBTRACTION of A,B matrices:\n",np.subtract(A,B))
print("\nMULTIPLICATION of A,B matrices:\n",np.matmul(A,B))
print("\nDIVISION of A,B matrices\n",np.divide(B,A))
# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))
# Trace of matrix A
print("\nTrace of A:", np.trace(A))
# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A))
# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))
print("\nMatrix A raised to power 3:\n",np.linalg.matrix_power(A, 3))
#calculation of eign values and vectors using eig() function
a,b = rkv.eig(A)
print("\nEigen values of matrix A are:\n",a)
print("\nEigen vectors of matrix A are:\n",b)
#calculation of eign values and vectors using eigh() function
c,d=rkv.eigh(com)
print("\nEigen values of complex matrix are:\n",c)
print("\nEigen vectors of complex matrix are:\n",d)
#Creating vectors
vector1 = 2 + 3j
vector2 = 4 + 5j
#dot product of martices A, B
product = np.dot(vector1, vector2)
print("\nDot Product :\n", product)
#dot product complex conjugate of A with B vector 
vproduct = np.vdot(vector1, vector2)
print("\nComplex conjugate Dot Product :\n ", vproduct)
# Solving eqautions using numpy.linalg.solve() method
print("\nSolution of linear equations:\n",np.linalg.solve(A,B))