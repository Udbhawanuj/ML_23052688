import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([0,0,0,1,1])
m = 0
c = 0
lr = 0.1
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
for i in range(1000):
    z = m*x + c
    y_pred = sigmoid(z)
    dm = np.mean((y_pred - y) * x)
    dc = np.mean(y_pred - y)
    m -= lr * dm
    c -= lr * dc
print(m, c)
x_test = np.array([2.5, 3.5, 4.5])
prob = sigmoid(m*x_test + c)
pred = (prob >= 0.5).astype(int)
print(prob)
print(pred)