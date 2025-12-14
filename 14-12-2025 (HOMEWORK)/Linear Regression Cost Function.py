import numpy as np
y = np.array([2,4,6,8,10])
y_hat = np.array([2.1,3.9,6.2,7.8,10.1])
mse = np.mean((y - y_hat)**2)
print(mse)
