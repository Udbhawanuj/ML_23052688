import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 6, 8, 10])
model = LinearRegression()
model.fit(x, y)
x_test = np.array([6, 7, 8]).reshape(-1, 1)
y_pred = model.predict(x_test)
print("Predicted values:", y_pred)
plt.scatter(x, y)
plt.plot(x, model.predict(x))
plt.show()