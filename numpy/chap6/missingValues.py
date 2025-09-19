import numpy as  np

#isnan function
# arr=np.array([1,2,np.nan,4,5])
# print(np.isnan(arr))

#nan_to_num Function
# arr=np.array([1,2,np.nan,4,5])
# # cleanedarr=np.nan_to_num(arr,nan=2)
# # print(cleanedarr)
# print(np.nan_to_num(arr,nan=2))


# #isinf Function
# arr=np.array([1,2,np.inf,4,5])
# print(np.isinf(arr))

#relacing infinet valuse with other valuse
arr=np.array([1,2,np.inf,4,5,-np.inf])
cleanedarr=np.nan_to_num(arr,posinf=2000,neginf=2000)
print(cleanedarr)