import numpy as np

A = np.array([[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9, 10, 11, 12]])

# 1. Quel est le shape de A?
# 2. Extraire la deuxieme ligne 
# 3. Extrais la 3ème colonne entière (résultat attendu : [3, 7, 11])

print(np.shape(A))
print (A[1])
print(A[:,2])

