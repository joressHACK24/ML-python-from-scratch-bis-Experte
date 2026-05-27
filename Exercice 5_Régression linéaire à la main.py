import numpy as np
import matplotlib.pyplot as plt


######################################################################################################


#___________________________________-1. DESCENTE DE GRADIENT______________________________________


#####################################################################################################

x = np.array([0.1, 0.3, 0.5, 0.6, 0.8, 0.9, 0.2, 0.4])
y = np.array([0.2, 0.4, 0.5, 0.7, 0.8, 0.9, 0.3, 0.4])
n = len(x)

w = 0.0
b = 0.0

epochs = 1000
learning_rate = 0.1

for i in range(epochs):
    
    y_pred = w * x + b
    dw = (2/n) * np.sum(x*(y_pred - y))
    db = (2/n) * np.sum(y_pred - y)


    w = w - learning_rate*dw
    b = b - learning_rate*db


print(f"l'equation de la regression est : y_pred = {w:.4f}*x {b:.4f}")


######################################################################################################


#___________________________________2. Equation Normale_____________________________________________


#####################################################################################################



x1 = x.reshape(-1,1)
y1 = y.reshape(-1,1)



X = np.c_[np.ones((len(x1),1)),x1]


#appliquons cette formules theta = (X^T * X)^-1 * X^T * y

theta = np.linalg.inv((X.T.dot(X))).dot((X.T.dot(y1)))


b = theta[0][0]
w = theta[1][0]


print(f"l'equation de la regression est : y_pred = {w:.4f}*x {b:.4f}")