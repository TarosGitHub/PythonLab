import numpy as np

## Construction of numpy array
na0 = np.array([1, 2, 3, 4, 5])

na1 = np.array([[i+j for j in range(3)] for i in range(10, 13)])

na2 = np.zeros(10)

na3 = np.ones((1, 4))

na4 = np.full((3, 5), 3.1)

## Attributes

na0.ndim
na0.shape
na0.size
na0.dtype
na0.itemsize
na0.nbytes

## Reshape

grid = np.arange(1, 10).reshape((3, 3))

x = np.array([1, 2, 3]) # shape=(3,)
x[np.newaxis, :] # shape=(1, 3)
x[:, np.newaxis] # shape=(3, 1)

## Concatenate

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y])

grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
np.concatenate([grid, grid]) # axis=0
"""
# Concatenates along rows
array([[1, 2, 3],
       [4, 5, 6],
       [1, 2, 3],
       [4, 5, 6]])
"""
np.concatenate([grid, grid], axis=1)
"""
# Concatenates along columns
array([[1, 2, 3, 1, 2, 3],
       [4, 5, 6, 4, 5, 6]])
"""

## Split

x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])

if __name__ == "__main__":
    #print(np.__version__)
    print(f"{na0=}")
    print(f"{na1=}")
    print(f"{na2=}")
    print(f"{na3=}")
    print(f"{na4=}")
