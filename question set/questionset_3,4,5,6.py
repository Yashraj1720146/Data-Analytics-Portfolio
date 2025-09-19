import numpy as np

# -------------------------------
# Indexing, Slicing & Masking
# -------------------------------

# Q1. Create a 1D array of numbers 10–19. Extract:
#     - First 3 elements
#     - Last 3 elements
#     - Every 2nd element
#     - Reverse array


# arr1 = np.arange(10, 20) 

# print(arr1)
# print(arr1[:3])
# print(arr1[-3:])
# print(arr1[::2])
# print(arr1[::-1])




# Q2. Create a 2D array (4x4) with values 1–16. Extract:
#     - 2nd row
#     - 3rd column
#     - A sub-matrix of first 2 rows and last 2 columns

# arr2=np.arange(1,17).reshape(4,4)
# print(arr2)
# print(arr2[1])
# print(arr2[:,2])
# print(arr2[2:,:-2])



# Q3. Use fancy indexing to extract elements at positions (0,0), (1,1), (2,2) from a 3x3 matrix.
# arr3=np.arange(10,100,10).reshape(3,3)
# print(arr3)
# print(arr3[[0,1,2], [0,1,2]])


# Q4. From arr = np.array([5,10,15,20,25,30]), 
#     use Boolean masking to extract:
#     - Elements greater than 15
#     - Even elements only
#     - Elements between 10 and 25 (inclusive)

# arr4 = np.array([5,10,15,20,25,30])
# print(arr4[arr4>15])
# print(arr4[arr4%2==0])
# print(arr4[(arr4 >= 10) & (arr4 <= 25)])



# -------------------------------
# Reshaping & Manipulating Arrays
# -------------------------------

# Q5. Create an array of values 1–12. Reshape it into:
#     - A (3,4) array
#     - A (2,6) array

# arr4=np.arange(1,13)
# print(arr4)
# a=arr4.reshape(3,4)
# b=arr4.reshape(2,6)
# print(a)
# print(b)


# Q6. Flatten the above (3,4) array using:
#     - .ravel()
#     - .flatten()
#     Compare difference.

# arr5=np.arange(1,13).reshape(3,4)

# print(arr5.ravel())
# print(arr5.flatten())
# print(arr5)

# Q7. Insert the value 99 at index 2 of arr = [10,20,30,40].

# arr6=np.array([10,20,30,40])
# newArray=np.insert(arr6,2,99)
# print(newArray)

# Q8. Append [50,60] to arr = [10,20,30,40].

# arr7=np.array([10,20,30,40])
# newArray=np.append(arr7,[50,60])
# print(newArray)

# Q9. Concatenate two arrays: [1,2,3] and [4,5,6].
# arra=np.array([1,2,3])
# arrb=np.array([4,5,6])
# newArray=np.concatenate((arra,arrb),axis=0)
# print(newArray)

# Q10. Remove the 2nd element from arr = [11,22,33,44,55].

# arr7=np.array([11,22,33,44,55])
# NewArray=np.delete(arr7,1)
# print(NewArray)

# Q11. Stack arrays vertically and horizontally:
#      a = [[1,2],[3,4]], b = [[5,6],[7,8]]

# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))

# Q12. Split np.arange(1,13) into 3 equal parts.

# arr8=np.arange(1,13)
# print(arr8)
# print(np.split(arr8,3))


# -------------------------------
# Broadcasting & Vectorization
# -------------------------------

# Q13. Create a 3x3 matrix with values 1–9.
#      Add [10,20,30] to each row using broadcasting.

# arr9=np.arange(1,10).reshape(3,3)
# print(arr9)
# print(arr9+[10,20,30])


# Q14. Multiply [1,2,3] with [10,20,30] element-wise (vectorized).
# arr10=np.array([1,2,3])
# print(arr10*[10,20,30])

# Q15. Why does adding arrays of shapes (3,3) and (2,3) fail? Try it and explain.

# Q16. Create an array [5,10,15,20,25]. 
#      Add 5 to each element, multiply each by 2, and divide by 5 using vectorization.

# arr11=np.arange(5,26,5)
# print(arr11)
# cal=(arr11+5)
# print(cal)
# cal=(arr11*2)
# print(cal)
# cal=(arr11/5)
# print(cal)



# arr11 = np.arange(5,26,5)
# print(arr11)
# result = ((arr11 + 5) * 2) / 5
# print(result)



# -------------------------------
# Handling Missing & Special Values
# -------------------------------

# Q17. arr = [1,2,np.nan,4,np.nan,6]
#      - Find which values are NaN
#      - Replace NaN with 0 using np.nan_to_num()


# arr12=np.array([1,2,np.nan,4,np.nan,6])
# print(np.isnan(arr12))

# newArray=np.nan_to_num(arr12,nan=0)
# print(newArray)

# Q18. arr = [1, -2, np.inf, -np.inf, 5]
#      - Detect which values are infinite
#      - Replace infinities with 999


# arr13=np.array([1, -2, np.inf, -np.inf, 5])
# print(np.isinf(arr13))
# newArray=np.nan_to_num(arr13,posinf=999,neginf=999)
# print(newArray)

# Q19. arr = [10, 20, np.nan, 40]
#      - Calculate sum while ignoring NaN
#      - Calculate mean while ignoring NaN



# arr15 = np.array([10, 20, np.nan, 40])

# print(np.nansum(arr15))
# print(np.nanmean(arr15))
