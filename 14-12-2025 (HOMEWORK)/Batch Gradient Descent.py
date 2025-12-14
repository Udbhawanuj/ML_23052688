import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])
m = 0
c = 0
lr = 0.01
for i in range(1000):
    y_pred = m*x + c
    m -= lr*np.mean(x*(y_pred-y))
    c -= lr*np.mean(y_pred-y)
print(m, c)