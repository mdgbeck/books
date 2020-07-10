import numpy as np

my_arr = np.arange(1e6)
my_list = list(range(1000000))

%time for _ in range(10): my_arr2 = my_arr * 2
%time for _ in range(10): my_list2 = [x * 2 for x in my_list]

data = np.random.randn(2, 3)
data
data * 2
data + data

# creating ndarrays
# can take a list
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

dat2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(dat2)
arr2.ndim
arr2.shape
arr1.dtype
arr2.dtype

np.zeros(10) # creates array of 0s
np.zeros((3, 6)) # array of 0s 3x6
np.empty((2, 3, 2)) # 3d array of "garbage" values

np.arange(15) # numpy range 0 - 14
np.ones_like(arr2) # returns array of same dimension but with all 1s

arr3 = np.array([3.7, -1.2, 0.5, 12.9, 10.1])
arr3
arr3.astype(np.int32) # drops decimal to convert to int
arr4 = np.array(['1.23', '-9.6', '24'], dtype=np.string_)
arr5 = np.array(['1.23', '-9.6', '24', 'abc'], dtype=np.string_)
arr4.astype(float) # converts string numbers to float, be careful with this
arr5.astype(float) # will fail if not possible

# slices of arrays affect array itself
arr = np.arange(10)
arr
arr[5]
arr[5:8]
arr_slice = arr[5:8]
arr_slice[1] = 12
arr_slice
arr

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]
arr2d[0][2] == arr2d[0, 2]
arr2d[:2] # think like first 2 rows
arr2d[2:] # this is saying get 3rd row until end
arr2d[:, :1] # this is like get column 1
arr2d[1, :2] # this is saying 2nd row first two columns

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
names
data
names == 'Bob'
data[names == 'Bob'] # selects rows 1, 4
data[names == 'Bob', 2:] # gets rows from Bob and then cols 3 until the end
data[names != 'Bob'] == data[~(names == 'Bob')]
cond = names == 'Bob'
data[~cond]

mask = (names == "Bob") | (names == "Will")
mask
data[mask]

# set values
data[data < 0] = 0
data
data[names != 'Joe'] = 7 # sets values for entire rows 2, 6, 7 to be 7
data

arr = np.zeros((8, 4))
arr
for i in range(8):
    arr[i] = i
arr
arr[[4, 3, 0, 6]]
arr[[-4, -3, 0]]

arr = np.arange(32).reshape(8, 4)
arr
arr[[1, 5, 7, 2], [0, 3, 1, 2]]
arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]] # this is different and returns subset of arr

# how to do matrix math
arr = np.random.randn(6, 3)
arr
np.dot(arr.T, arr) # where T is transpose

arr = np.arange(16).reshape((2, 2, 4))
arr
arr.T

# 4.2 universal functions
arr = np.arange(10)
np.sqrt(arr)
arr

x = np.random.randn(8)
y = np.random.randn(8)
np.maximum(x, y)

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.arange(2.1, 2.51, step=.1)
cond = np.array([True, False, True, True, False])
yarr
xarr
np.where(cond, xarr, yarr)

arr = np.random.randn(4, 6)
x = np.where(arr > 0, 2, -2)
x
arr
arr.mean()
np.mean(arr)
arr.sum()
np.sum(arr)
arr.mean(axis=1)
arr.mean(axis=0)

names = np.array(['Carl', 'Carl', 'Bob', 'Alex', 'Bob', 'bob'])
np.unique(names) # note that this sorts as well gets unique
sorted(names)
set(names)
sorted(set(names))

# random walk implementations
# first regular python method
import random
import matplotlib.pyplot as plt
%matplotlib
position = 0
walk = [position]
steps = 100000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
plt.plot(walk)

# alternate using arrays
nsteps = 1000
draws = np.random.randint(0, 2, size = nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
# get position first crossed past +- 10
(np.abs(walk) >= 10).argmax()

# do many at once
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size = (nwalks, nsteps))
steps = np.where(draws > 0, -1, 1)
walks = steps.cumsum(1)
walks
walks.max()
walks.min()
walks.min(1).mean()

hits30 = (np.abs(walks) > 30).any(1)
hits30.sum()
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
crossing_times.mean()
