import numpy as np
arr1=np.array([10,20,30,40])
arr2=np.array([1,2,3,4])
newArray=np.concatenate((arr1,arr2),axis=0)
print(newArray)