import numpy as np


# ================================
# 🔹 Section A: Array Creation & Basics
# ================================

# Q1. Create a 1D NumPy array from 1 to 20.
# Q2. Create a 2D array (3x3) with values from 1 to 9.
# Q3. Create an array of 10 zeros and 10 ones.
# Q4. Create an identity matrix of size 5.
# Q5. Use np.linspace() to generate 15 values between 0 and 5.

# ================================
# 🔹 Section B: Array Properties
# ================================

# Q6. For the array arr = np.array([[2,4,6],[8,10,12],[14,16,18]]):
#     - Find its shape, size, ndim, dtype.
# Q7. Reshape the above array into (9,1).
# Q8. Flatten it into a 1D array.
# Q9. Stack two arrays a = [1,2,3] and b = [4,5,6] vertically and horizontally.
# Q10. Split np.arange(1,13) into 3 equal parts.

# ================================
# 🔹 Section C: Array Operations
# ================================

# Q11. For arr = np.array([10,20,30,40]):
#      - Add 5 to each element
#      - Multiply each element by 2
#      - Divide all elements by 10
# Q12. Create two arrays and perform element-wise addition, subtraction, multiplication, and division.
# Q13. Use broadcasting to add a 1D array [1,2,3] to each row of a 3x3 matrix.
# Q14. Sort the array [15,2,9,23,7,10].
# Q15. Extract only the even numbers from np.arange(1,21).

# ================================
# 🔹 Section D: Aggregation Functions
# ================================

# Q16. Find sum, mean, min, max, std, var, median of arr = np.array([5,10,15,20,25,30]).
# Q17. Find row-wise and column-wise sums for:
#      arr = np.array([[1,2,3],
#                      [4,5,6],
#                      [7,8,9]])
# Q18. Generate 20 random integers between 1 and 100 and find their mean and median.
# Q19. Compare mean vs median for the array [5,7,9,100]. Why are they different?
# Q20. Find the mode of the array [1,2,2,3,4,4,4,5].

# ================================
# 🔹 Section E: Indexing, Slicing & Masking
# ================================

# Q21. Create a 1D array of numbers 10–19. Extract:
#      - First 3 elements
#      - Last 3 elements
#      - Every 2nd element
#      - Reverse array

# Q22. Create a 2D array (4x4) with values 1–16. Extract:
#      - 2nd row
#      - 3rd column
#      - A sub-matrix of first 2 rows and last 2 columns

# Q23. Use fancy indexing to extract elements at positions (0,0), (1,1), (2,2) from a 3x3 matrix.

# Q24. From arr = np.array([5,10,15,20,25,30]), 
#      use Boolean masking to extract:
#      - Elements greater than 15
#      - Even elements only
#      - Elements between 10 and 25 (inclusive)

# ================================
# 🔹 Section F: Reshaping & Manipulating Arrays
# ================================

# Q25. Create an array of values 1–12. Reshape it into:
#      - A (3,4) array
#      - A (2,6) array

# Q26. Flatten the above (3,4) array using:
#      - .ravel()
#      - .flatten()
#      Compare difference.

# Q27. Insert the value 99 at index 2 of arr = [10,20,30,40].

# Q28. Append [50,60] to arr = [10,20,30,40].

# Q29. Concatenate two arrays: [1,2,3] and [4,5,6].

# Q30. Remove the 2nd element from arr = [11,22,33,44,55].

# Q31. Stack arrays vertically and horizontally:
#      a = [[1,2],[3,4]], b = [[5,6],[7,8]]

# Q32. Split np.arange(1,13) into 3 equal parts.

# ================================
# 🔹 Section G: Broadcasting & Vectorization
# ================================

# Q33. Create a 3x3 matrix with values 1–9.
#      Add [10,20,30] to each row using broadcasting.

# Q34. Multiply [1,2,3] with [10,20,30] element-wise (vectorized).

# Q35. Why does adding arrays of shapes (3,3) and (2,3) fail? Try it and explain.

# Q36. Create an array [5,10,15,20,25]. 
#      Add 5 to each element, multiply each by 2, and divide by 5 using vectorization.

# ================================
# 🔹 Section H: Handling Missing & Special Values
# ================================

# Q37. arr = [1,2,np.nan,4,np.nan,6]
#      - Find which values are NaN
#      - Replace NaN with 0 using np.nan_to_num()

# Q38. arr = [1, -2, np.inf, -np.inf, 5]
#      - Detect which values are infinite
#      - Replace infinities with 999

# Q39. arr = [10, 20, np.nan, 40]
#      - Calculate sum while ignoring NaN
#      - Calculate mean while ignoring NaN
