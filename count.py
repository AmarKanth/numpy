"""
count_nonzero Method
"""
import numpy as np

arr = np.array([[0,1,7,0,0],[3,0,0,2,19]])
res1 = np.count_nonzero(arr, axis=0)
res2 = np.count_nonzero(arr, axis=1)
print(res2)