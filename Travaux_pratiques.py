import numpy as np


A = np.array([[2, 1, 3],
              [0, 4, 1],
              [1, 2, 5]])

b = np.array([1, 2, 3])


# zeigen wir die Shape von A an

print(np.shape(A))

# extrahieren die zweite Spalte von A

print(A[:,1])

#berechnen wir der Determinant von A
det = np.linalg.det(A)
print(det)


if det != 0:
    print("gibt es eine Lösung")
    print("Diese Lösung ist :")
    x = np.linalg.solve(A,b)
    print(x)


#Jetzt soll ich meine Lösung prüfen

print(np.dot(A,x))


# Problem 2 — Matrizen multiplizieren

A = np.array([[1, 2, 3],
              [4, 5, 6]])        # shape (2, 3)

B = np.array([[1, 0],
              [0, 1],
              [1, 1]])           # shape (3, 2)

def multiply_matrices(A, B):
    lignes_A = A.shape[0]
    colonnes_B = B.shape[1]
    colonnes_A = A.shape[1]

    C = np.zeros((lignes_A, colonnes_B))

    for i in range(lignes_A):
        for j in range(colonnes_B):
            for k in range(colonnes_A):
                C[i][j] += A[i][k] * B[k][j]  #
    return C

crash = multiply_matrices(A,B)
print(crash)

mitFunktion = np.dot(A,B)
print(mitFunktion)

print(" DA SIND DIE ZWEI ERGEBNISSE : ",crash, mitFunktion)

# Was ich von B beobachte, die einige Daten sind 0 und 1..



#Problème 3 — Calcul différentiel

#f(x) = x⁴ - 3x³ + 2x - 7

# f'(x) = 4x³ - 9x² + 2

def f(x):
    return x**4 - 3*x**3 + 2*x - 7
def gradient_numerisch(f, x, h=1e-5):
    abt_f = (f(x+h)-f(x-h))/(2*h)
    return abt_f


punkten = np.array([0, 1, 2, 3])
for x in punkten:
    grad = gradient_numerisch(f, x)
    f_= 4*x**3 - 9*x**2 +2
    print([f"f'({x}) ≈ {grad:.4f}",f"f'({x}) ≈ {f_:.4f}"])


#f(x) = (x³ + 1)²
# f'(x) = 2(x³ + 1)(3x²)



#Problème 4 — Statistiques & Probabilités

data = np.array([12, 15, 14, 10, 18, 22, 13, 17, 16, 11])


# berechne ich die Mittelwert

m = np.mean(data)


#berechne ich die Abweichung

o = (np.var(data))**0.5


print("moyenne:", m, "ecart-type:",o)


Pourcentage = (np.sum((data>=(m-o)) & (data<=(m+o)))/len(data))*100
print(Pourcentage,"%")



set = np.random.normal(loc=m, scale=o, size=5000)
Pourcentage = (np.sum((set>=(m-o)) & (set<=(m+o)))/len(set))*100
print(Pourcentage,"%")


## Problème 5 — Bayes + Espérance 🎯

'''P(fraude)              = 0.02
P(alerte | fraude)     = 0.95
P(alerte | normal)     = 0.08'''

#je calcule P(alerte)

p_alerte = 0.95*0.020+.08*0.98

print(p_alerte)


#Calcule P(fraude | alerte) — quelle est la probabilité que la transaction
#soit vraiment frauduleuse quand une alerte est déclenchée ?


P_fraude_alerte = (0.95*0.02)/p_alerte

print(P_fraude_alerte)

#Calcule l'espérance du coût avec NumPy

esperanz = 0.10*500 + 0.05*2000

print("L'esperance :", esperanz)