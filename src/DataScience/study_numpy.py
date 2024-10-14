import numpy as np

# Construction of numpy array
na0 = np.array([1, 2, 3, 4, 5])

na1 = np.array([[i+j for j in range(3)] for i in range(10, 13)])

na2 = np.zeros(10)

na3 = np.ones((1, 4))

na4 = np.full((3, 5), 3.1)

if __name__ == "__main__":
    #print(np.__version__)
    print(f"{na0=}")
    print(f"{na1=}")
    print(f"{na2=}")
    print(f"{na3=}")
    print(f"{na4=}")
