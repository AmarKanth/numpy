"""
Python does not have built-in support for Arrays, but Python lists can be used instead
"""

"""
Create New Numpy Array
"""
import numpy as np
res = np.array([[1,2],[3,4], [5,6]], dtype=float)
print(res)
print(res.size)
print(res.shape)
print(res.reshape(2,3))


"""
arange Method
"""
import numpy as np
np1 = np.arange(5)
np2 = np.arange(6).reshape(3,2)
print(np2)


"""
zeros Method
"""
import numpy as np
array = np.zeros([3, 3], dtype = int) 
print(array) 


"""
empty Method
"""
import numpy as np
array = np.empty((3, 4), dtype=int)
print(array)


"""
full Method
"""
array = np.full((3, 3), 55, dtype=int)
print(array)


"""
ones Method
"""
import numpy as np
array = np.ones([3, 3], dtype = int)
print(array)


"""
flatten the n*n matrix
"""
import numpy as np
np1 = np.array([[2, 3], [4, 5]])
f = np1.flatten()
r = np1.ravel()
print(r)