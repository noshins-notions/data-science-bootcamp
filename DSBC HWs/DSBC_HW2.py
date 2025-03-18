import numpy as np
import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

# Part 1 - Numpy
# Problem 1
A = np.array([1, 2, 3, 3, 4, 5])
B = np.array([3, 4, 5, 6, 7, 3])

hAB = np.hstack((A,B))
vAB = np.vstack((A,B))
print("Horizontal Stack:", hAB)
print("Vertical Stack:", vAB)

# Problem 2
common = np.intersect1d(A, B)
print("Common Elements:", common)

# Problem 3
rangeA = A[np.where((A >= 3) & (A <= 4))]
print("Elements between 3 and 4:", rangeA)

# Problem 4
filtered_iris = iris_2d[np.where((iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0))]
print("Filtered Iris Dataset Shape:", filtered_iris.shape)
print("Filtered Iris Dataset:", filtered_iris)

# Part 2 - Pandas
# Problem 1
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

every_twentieth_row = df.loc[::20, ['Manufacturer', 'Model', 'Type']]
print("Every 20th Row:", every_twentieth_row)

# Problem 2
df.loc[df['Min.Price'].isnull(), 'Min.Price'] = df.loc[df['Min.Price'].isnull(), 'Price']
df.loc[df['Max.Price'].isnull(), 'Max.Price'] = df.loc[df['Max.Price'].isnull(), 'Price']
print("Missing Values in Min.Price:", df['Min.Price'].isnull().sum())
print("Missing Values in Max.Price:", df['Max.Price'].isnull().sum())

# Problem 3
df2 = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

rows_over_100 = df2[df2.sum(axis=1) > 100]
print("Rows with Sum > 100:", rows_over_100)
