"""
where Method
"""
import numpy as np

arr = np.array([10, 32, 30, 30, 50, 20, 82, 91, 45])
i = np.where(arr == 30)
print(i)


"""
searchsorted Method
"""
import numpy as np

arr = np.array([10, 32, 30, 30, 50, 20, 82, 91, 45])
left = np.searchsorted(arr, 30, side="left")
right = np.searchsorted(arr, 30, side='right')
print(right)