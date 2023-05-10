"""
argsort Method
"""
import numpy as np

mtrx = np.matrix('[-1, 2, 3; 4, -5, 6; 7, -8, 9]')
res = mtrx.argsort()
print(res)