#creating arryas uisng python list

import numpy as np

# pylist=np.array([1,2,3])
# print(pylist)

#creatring arrays with default values
#using zeros function

zeros_array=np.zeros((3,6))
print(zeros_array)

#using ones as default value
#ones function

ones_array=np.ones((2,4))
print(ones_array)

#using specific numbers as default valuse
#Full Function

def_arrays=np.full((3,4),6)
print(def_arrays)