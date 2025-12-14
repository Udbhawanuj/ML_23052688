import numpy as np
X = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])
X = np.c_[np.ones(len(X)), X]
theta = np.linalg.inv(X.T @ X) @ X.T @ y
print(theta)
