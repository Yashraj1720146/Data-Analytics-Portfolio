import numpy as np

# # ================================
# # 🔹 Section A: Array Creation & Basics
# # ================================

# # Q1. Create a 1D NumPy array from 1 to 20.
# arry1D=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# print(arry1D)


# # Q2. Create a 2D array (3x3) with values from 1 to 9.
# array2D=np.arange(10,100,10).reshape(3,3)
# print(array2D)

# # Q3. Create an array of 10 zeros and 10 ones.
# import numpy as np

# zeros_ones_array = np.concatenate([np.zeros(10, dtype=int), np.ones(10, dtype=int)])
# print(zeros_ones_array)


# # Q4. Create an identity matrix of size 5.
# identity_matrix=np.eye(5)
# print(identity_matrix)

# # Q5. Use np.linspace() to generate 15 values between 0 and 5.
# arr = np.linspace(0, 5, 15)
# print(arr)

# #Create an array of numbers from 2 to 20 with a step size of 3
# arr = np.arange(2, 21, 3)   # start=2, stop=21 (exclusive), step=3
# print(arr)

# # ================================
# # 🔹 Section B: Array Properties
# # ================================

# # Q6. For the array arr = np.array([[2,4,6],[8,10,12],[14,16,18]]):
# #     - Find its shape, size, ndim, dtype.

# arr = np.array([[2,4,6],[8,10,12],[14,16,18]])
# print(arr.shape)
# print(arr.size)
# print(arr.ndim)
# print(arr.dtype)

# # Q7. Reshape the above array into (9,1).
# arr = np.array([[2,4,6],[8,10,12],[14,16,18]])
# reshaped_arr = arr.reshape(9, 1)
# print(reshaped_arr)

# # Q8. Flatten it into a 1D array.
# import numpy as np

# arr = np.array([[2,4,6],[8,10,12],[14,16,18]])
# flattened = arr.flatten()
# print(flattened)

# # Q9. Stack two arrays a = [1,2,3] and b = [4,5,6] vertically and horizontally.
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# v_stack = np.vstack((a, b))
# print(v_stack)
# h_stack = np.hstack((a, b))
# print(h_stack)

# # Q10. Split np.arange(1,13) into 3 equal parts.

# arr = np.arange(1, 13)  # 1 to 12
# splits = np.split(arr, 3)
# print(splits)

# # ================================
# # 🔹 Section C: Array Operations
# # ================================

# # Q11. For arr = np.array([10,20,30,40]):
# #      - Add 5 to each element
# #      - Multiply each element by 2
# #      - Divide all elements by 10

# arr = np.array([10,20,30,40])
# print(arr+5)
# print(arr*2)
# print(arr/10)

# # Q12. Create two arrays and perform element-wise addition, subtraction, multiplication, and division.
# arr1=np.array([2,4,6,8,10])
# arr2=np.array([1,3,5,7,9])
# print(arr1+arr2)
# print(arr1-arr2)
# print(arr1*arr2)
# print(arr1/arr2)


# # Q14. Sort the array [15,2,9,23,7,10].
# arr = np.array([15, 2, 9, 23, 7, 10])
# sorted_arr = np.sort(arr)
# print(sorted_arr)

# # Q15. Extract only the even numbers from np.arange(1,21).
# import numpy as np

# arr = np.arange(1, 21)   # numbers from 1 to 20
# even_numbers = arr[arr % 2 == 0]
# print(even_numbers)


# # ================================
# # 🔹 Section D: Aggregation Functions
# # ================================

# # Q16. Find sum, mean, min, max, std, var, median of arr = np.array([5,10,15,20,25,30]).
# arr = np.array([5,10,15,20,25,30])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.std(arr))
# print(np.var(arr))
# print(np.median(arr))






# Q17. Find row-wise and column-wise sums for:
#      arr = np.array([[1,2,3],
#                      [4,5,6],
#                      [7,8,9]])



# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])

# print("Row-wise sum:", np.sum(arr, axis=1))
# print("Column-wise sum:", np.sum(arr, axis=0))



# Q18. Generate 20 random integers between 1 and 100 and find their mean and median.

# arr = np.random.randint(1, 101, 20)
# print(arr)
# print(np.mean(arr))
# print(np.median(arr))

# Q19. Compare mean vs median for the array [5,7,9,100]. Why are they different?
# Q20. Find the mode of the array [1,2,2,3,4,4,4,5] (hint: use scipy.stats.mode or write logic).
