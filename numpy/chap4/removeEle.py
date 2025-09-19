import numpy as np

#for 1d
# arr1=np.array([10,20,30,40])
# newArray=np.delete(arr1,2,axis=None)
# print(arr1)
# print(newArray)

#for 2d array
import numpy as  np
twod_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
newtwod_array=np.delete(twod_array,0,axis=1)
newtwod_array2=np.delete(twod_array,0,axis=0)
print(twod_array)
print(newtwod_array)
print(newtwod_array2)