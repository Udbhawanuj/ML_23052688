import numpy as np
m = 2
c = -5
x = np.array([1,2,3,4,5])
y_prob = 1 / (1 + np.exp(-(m*x + c)))
y_class = (y_prob >= 0.5).astype(int)
print(y_class)
