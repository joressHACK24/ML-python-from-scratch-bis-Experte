import numpy as np

A = np.array([[2, 1], [1, 3]])
b = np.array([5, 10])

#lösen wir Ax=b

lösung = np.linalg.solve(A,b)
print(lösung)

#rechnen wir die Determinante

print(np.linalg.det(A))

# calculons la norme du vecteur x

print(np.linalg.norm(lösung))