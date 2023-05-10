"""
argmax Method
"""
import numpy as np

arr = np.arange(12).reshape(3,4)
res1 = np.argmax(arr)
res2 = np.argmax(arr, axis=0)
res3 = np.argmax(arr, axis=1)
print(res3)