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


"""
argmax Method
"""
import numpy as np

arr = np.arange(12).reshape(3,4)
res1 = np.argmax(arr)
res2 = np.argmax(arr, axis=0)
res3 = np.argmax(arr, axis=1)
print(res3)


"""
nanargmax Method
"""
import numpy as np

arr = np.array([[np.nan, 4], [1, 3]])
res1 = np.nanargmax(arr, axis=0)
res2 = np.nanargmax(arr, axis=1)
print(res2)


"""
argmin Method
"""
import numpy as np

arr = np.arange(8).reshape(4,2)
res1 = np.argmin(arr, axis=0)
res2 = np.argmin(arr, axis=1)
print(res2)