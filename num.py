# Every module in python in can be identified uniquely identical

# python --version
# Python 3.14.7

# import numpy
# print(numpy.__version__)
# 2.5.3

# Definition: NumPy Array is a collection os elemnets arranged in one or more dimensions. 

import numpy as np
mark = np.array([46,50,74,88,76,61])
print(mark)
[46 50 74 88 76 61]

>>> nested = np.array([1,2,3],[4,5,6])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    nested = np.array([1,2,3],[4,5,6])
TypeError: Field elements must be 2- or 3-tuples, got '4'
>>> nested = np.array([1,2,3,[4,5],6])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    nested = np.array([1,2,3,[4,5],6])
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (5,) + inhomogeneous part.

marks = np.array([ [45,56,76], [78,65,71] ])
print(marks)
[[45 56 76]
 [78 65 71]]

#np.arrange(startr, stop, num)
a = np.arange(1, 10, 3)
a
array([1, 4, 7])

#np.linspace(start, stop, num)
#generates a specified number of evenly spaced values between a starting value and an ending value 
b = np.linspace(1, 10, 3)
b
array([ 1. ,  5.5, 10. ])

c = np.linspace(1, 10, 4)
c
array([ 1.,  4.,  7., 10.]

#np.zeros()
# creata an array filled with zeros
# np.zeros(shape)
# np.zeros(shape,shape)
# np.ones()

# np.full(shape, value)
g = np.full((2,4),5)
g
array([[5, 5, 5, 5],
       [5, 5, 5, 5]])

# arr.ndim
# arr.shape
# arr.size - no of elements
# arr.dtype

marks = np.array([ [45,67,84],[56,98,61] ])
print("Array: ")
# Array: 
print(marks)
# [[45 67 84]
#  [56 98 61]]
print("Dimesntions: ", marks.ndim)
# Dimesntions:  2
print("Shape: ", marks.shape)
# Shape:  (2, 3)
print("Size: ", marks.size)
# Size:  6
print("Data Type: ", marks.dtype)
# Data Type:  int64


####### Testing 
# z = np.array([1, "akash"])
# z.dtype
# dtype('<U21')
# z = np.array([1, "akash", "jangid"])
# z.dtype
# dtype('<U21')
# z = np.array(["akash", 1, "jangid"])
# z.dtype
# dtype('<U21')
# z = np.array(["akash", "jangid"])
# z.dtype
# dtype('<U6')
# z = np.array([1.1, "akash", "jangid"])
# z.dtype
# dtype('<U32')
# z = np.array([1, 2, 3])
# z.dtype
# dtype('int64')