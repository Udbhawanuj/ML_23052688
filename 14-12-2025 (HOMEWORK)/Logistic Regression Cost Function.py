import numpy as np
y = np.array([0,1,1,0])
y_hat = np.array([0.1,0.8,0.9,0.2])
loss = -np.mean(y*np.log(y_hat) + (1-y)*np.log(1-y_hat))
print(loss)