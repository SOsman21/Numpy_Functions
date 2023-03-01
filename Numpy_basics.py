import numpy as np

# one dimensional array
a = np.array([1,2,3])
print(f'1 Dimesional Array:{a}')

# two dimensional array
b = np.array([[1,2,3],[4,5,6]])
print(f'2 Dimesional Array:{b}')

# get dimension of array
getDim = a.ndim
print(f'Dimensions of array a:{getDim}')

# get shape of array (number of rows, number of values per row)
getShape = b.shape
print(f'Get shape of array b:{getShape}')

# get data type and memory size
getDataType = a.dtype
print(f'Data tyoe of array a:{getDataType}')

# get size of 1 (number of bytes)
getSize = a.itemsize
print(f'Size of 1 item in array a:{getSize} bytes')

# get total size of array
getTotalSize = a.nbytes
print(f'Size of array a:{getTotalSize} bytes')