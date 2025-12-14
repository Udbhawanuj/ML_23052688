import numpy as np
X = np.array([[1,2],[2,1],[3,4],[4,3],[5,5]])
y = np.array([5,6,11,12,15])
X = np.c_[np.ones(len(X)), X]
theta = np.linalg.inv(X.T @ X) @ X.T @ y
print(theta)
