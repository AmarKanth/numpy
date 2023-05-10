"""
sort Method
"""
import numpy as np

arr = np.array([[12, 15], [10, 1]])
sorted = np.sort(arr, axis=0)
print(sorted)

arr = np.array([[10, 15], [12, 1]])
sorted = np.sort(arr, axis=1)
print (sorted)

arr = np.array([[12, 15], [10, 1]])
sorted = np.sort(arr, axis = None)


"""
sort Function
"""
import numpy as np

arr = np.array([12, 15, 10, 1])
arr.sort()
print(arr)

mtrx = np.matrix('[4, 1; 12, 3]')
mtrx.sort()
print(mtrx)


"""
argsort Method
"""
import numpy as np

arr = np.array([9, 3, 1, 7, 4, 3, 6])
sorted_indices = np.argsort(arr)
res = np.zeros(len(sorted_indices), dtype=int)
for i in range(0, len(sorted_indices)):
    res[i] = arr[sorted_indices[i]]
print(res)


"""
lexsort Method
"""
import numpy as np

a = np.array([9, 3, 1, 3, 4, 3, 6])
b = np.array([4, 6, 9, 2, 1, 8, 7])
sorted_indices = np.lexsort((b,a))
print(sorted_indices)