# 1 import numpy as `np` and print the version
np.version.version
# or
np.__version__

# 2 create a 1D array of number from 0 to 9
# output: array([0,1,2,3,4,5,6,7,8,9])
np.array(range(10))
# or
np.arange(10)

# 3 create a 3x3 numpy array of True's
np.array([True]*9).reshape(3,3)
# or
np.full((3,3),True,dtype=bool)
# or 
np.ones((3,3,),dtype=bool)

# 4 extract all odd numbers from a 1D array
np.array([x for x in range(10) if not x%2==0])
# or 
arr = np.array(range(10))
arr[arr%2==1]

# 5 replace all odd values in an array with -1
arr = np.array(range(10))
arr[arr%2==1] = -1

# 6 replace all odd numbers in an arr without modifying the original array
arr = np.array(range(10))
out = np.array([x if x%2==0 else -1 for x in arr])
# or
arr = np.arange(10)
out = np.where(arr%2==1, -1, arr)

# 7 convert a 1x10 1D array into a 2x5 2D array
arr = np.arange(10)
arr.reshape(2,5)
# or 
arr.reshape(2,-1) # setting the dimension to -1 automatically decides the number of cols

# 8 stack arrays a and b vertically where
# a = np.arange(10).reshape(2,-1)
# b = np.arange(1,10).reshape(2,-1)
np.vstack((a,b))
# or
np.concatenate((a,b), axis=0)
# or 
np.r_[a,b]

# 9 stack arrays a and b horizontally where
# a = np.arange(10).reshape(2,-1)
# b = np.arange(1,10).reshape(2,-1)
np.concatenate((a,b),axis=1)
# or
np.hstack((a.b))
# or 
np.c_[a,b]

# 10 given input array a (where a=np.array([1,2,3])
# generate the following pattern
# array([1,1,1,2,2,2,3,3,3,1,2,3,1,2,3,1,2,3])
np.concatenate((a.repeat(3),np.tile(a,3)),axis=0)
# or 
np.r_[np.repeat(a,3),np.tile(a,3)]

# 11 get the common items between two arrays a and b, where
# a = np.arange(0,10)
# b = np.arange(5,15)
np.intersect1d(a,b)

# 12 remove all elements from array a that are in array b
# where:
# a = np.arange(0,10)
# b = np.arange(5,15)
np.setdiff1d(a,b)

# 13
# get positions where elements of a and b match
np.where(a == b)

# 14
# get all elements of  an array a where the element is 
# greater than or equal to 5 and less than or equal it 10
idx = np.where((a >= 5) & (a <=10))
a[idx]
# or 
a[(a > 4) & (a < 11)]

# 15 
# get the elementwise maximum of two arrays
np.maximum(a, b)

# 16
# where arr = np.arange(9).reshape(3,3), swap the first and
# second columns in the array
arr[:,[1,0,2]]

# 17
# where arr = np.arange(9).reshape(3,3), swap the first and
# second rows in the array
arr[[1,0,2],:]

# 18
# where arr = np.arange(9).reshape(3,3), reverse the row order
arr[::-1,:]
# or
arr[::1]

# 19
# where arr = np.arange(9).reshape(3,3), reverse the column order
arr[:,::-1]

# 20 
# create a 5x3 2D array of random floats between 5 and 10
(np.random.randint(5,10,15)+ np.random.random(15)).reshape(5,3)
# or 
np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3))
# or 
np.random.uniform(low=5, high=10, size=(5,3))

# 21 
# print or show only 3 decimal places of a numpy array
np.set_printoptions(precision=3)

# 22
# how do you get numpy to suppress scientific notation and thus pretty 
# print an array?
np.set_printoptions(suppress=True, precision=6)

# 23 
# how do you limit the number of items printed in the output of a numpy array
# to say, 20 items?
np.set_printoptions(threshold=20)

# 24
# how to make numpy print all values in an array no matter how large
np.set_printoptions(threshold=np.nan)

# 25
# import a dataset with both numbers and text while keeping the text intact
# given, url = 'url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
