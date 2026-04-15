import numpy as np

# Create an array
arr = np.array([10, 20, 35, 50, 80])

# Find difference between consecutive elements
result = np.diff(arr)

# Print results
print("Original Array:", arr)
print("Difference between consecutive elements:", result)