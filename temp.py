"""
fromrecords Method
"""
import numpy as np

columns = "Rollno, Name, Age"
rows = [(101, 'Jitender', 21), (102, 'Deepak', 20)]
arr = np.core.records.fromrecords(rows, names=columns)
print(arr)
print(arr.Rollno)