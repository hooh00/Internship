from numpy import *
arr1 = array([
  [1,2,3,6,2,9],
  [4,5,6,7,5,3]
  
])

arr2 = arr1.flatten()
#from 2 dimension to 1 dimension

arr3 = arr2.reshape(3,4)
#make it into a 3 dimensional array

print(arr1)
#print(arr1.dtype) know what type of data you're working with
#print(arr1.ndim) number of dimensions
#print(arr1.shape) number of rows and columns 
#print(arr1.size) size of the entire block

import numpy as np
A=np.array([[11,2,3],[4,5,6],[7,8,9]])
print(A)

B=np.matmul(A,A.T)
print(B)
