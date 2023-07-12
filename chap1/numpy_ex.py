import numpy as np

X = np.array([[51,55],[14,19],[0,4]])
print(X)
X = X.flatten()
print(X)
print(X[np.array([0,2,4])])
print(X>15)
print(X[X>15])