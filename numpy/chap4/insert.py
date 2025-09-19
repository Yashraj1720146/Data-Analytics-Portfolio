import numpy as np

# #For 1D array
# arr=np.array([10,20,30,40,50,60])
# newArray=np.insert(arr,2,70,axis=0)
# print(newArray)


towdArr=np.array([[10,20,30],[40,50,60],[100,110,120]])
new2dArray=np.insert(towdArr,2,[70,80,90],axis=1)
print(new2dArray)