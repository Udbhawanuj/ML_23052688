import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])
m = 0
c = 0
lr = 0.01
n = len(x)
for i in range(1000):
    y_pred = m*x + c
    dm = (-2/n)*np.sum(x*(y-y_pred))
    dc = (-2/n)*np.sum(y-y_pred)
    m = m - lr*dm
    c = c - lr*dc
print(m, c)