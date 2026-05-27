# ============================================================
# 50 EXERCICES — NUMPY AVANCÉ & PANDAS
# Niveau : Intermédiaire
# Thème  : Manipulation de données pour le Deep Learning
# ============================================================
# Instructions :
#   - Complète chaque exercice sans regarder les solutions
#   - Soumets tout à la fin pour correction
#   - Les exercices sont progressifs (1 = facile, 50 = avancé)
# ============================================================

import numpy as np
import pandas as pd



# ============================================================
# PARTIE 1 — NUMPY : CRÉATION & INDEXING AVANCÉ (Ex 1 à 10)
# ============================================================

# Exercice 1
# Crée un array de 20 zéros, remplace les indices pairs par 1.
# Résultat attendu : [1, 0, 1, 0, 1, 0, ...]


array_zero = np.zeros(20, dtype= int)

array_zero[0::2] = 1

print(array_zero)


# Exercice 2
# Crée une matrice identité 5x5 sans utiliser np.eye().
# Hint : np.zeros + une boucle ou np.diag()

matrice_identite = np.zeros((5, 5), dtype=int)
for i in range(len(matrice_identite)):
    for k in range(len(matrice_identite)):
        if i == k :
            matrice_identite[i][k] = 1


print(matrice_identite)


# Exercice 3
# Crée un array [0, 5, 10, 15, ..., 100] avec np.arange().
# Puis inverse-le sans boucle.

array = np.arange(0,101,5)
print(array[-1::-1])

# Exercice 4
# Crée une matrice 4x4 avec des valeurs de 1 à 16.
# Extrais uniquement les valeurs > 8 avec du boolean indexing.

matrice_nombres = np.arange(1,17).reshape(4,4)

print(matrice_nombres[matrice_nombres>8])
# Exercice 5
# Crée un array 3x3x3 (tenseur 3D) rempli de valeurs aléatoires.
# Affiche sa shape, ndim et dtype.

tenseur = np.random.rand(3, 3, 3)
print(tenseur.shape,tenseur.ndim,tenseur.dtype)


# Exercice 6
# Crée deux arrays A = [1,2,3,4,5] et B = [5,4,3,2,1].
# Sans boucle, retourne un array avec le max élément par élément.
# Hint : np.maximum()

A = np.array([1,2,3,4,5])
B = np.array([5,4,3,2,1])

print(np.maximum(A,B))
# Exercice 7
# Crée une matrice 5x5 aléatoire (entiers entre 0 et 9).
# Remplace toutes les valeurs inférieures à 5 par -1.

matrice = np.random.randint(0, 10, size=(5, 5))
matrice[matrice < 5] = -1  # ✅ une seule ligne

print(matrice)

# Exercice 8
# Crée un array de 10 valeurs équidistantes entre 0 et 1 (inclus).
# Hint : np.linspace()

array = np.linspace(0,1,10)
print(array)

# Exercice 9
# Crée une matrice 3x4. Extrais :
# - La sous-matrice 2x2 du coin supérieur gauche
# - La dernière ligne
# - La diagonale principale (hint: np.diag())

M1 = np.arange(0,12).reshape(3,4)
print(M1)
print(M1[0:2,0:2])
print(M1[2,:])
print(np.diag(M1))
# Exercice 10
# Trie les lignes d'une matrice 3x3 aléatoire par leur somme.
# Hint : np.argsort() + indexing

matrice_nombres = np.arange(1,10).reshape(3,3)


sommes = matrice_nombres.sum(axis=1)     
ordre = np.argsort(sommes)                 
print(matrice_nombres[ordre])






# ============================================================
# PARTIE 2 — NUMPY : OPÉRATIONS AVANCÉES (Ex 11 à 20)
# ============================================================

# Exercice 11
# Normalise un array entre 0 et 1 sans utiliser sklearn.

data = np.array([3, 1, 4, 1, 5, 9, 2, 6])
formule = (data- np.min(data))/(np.max(data)-np.min(data))
print(formule)


# Exercice 12
# Calcule la distance euclidienne entre deux vecteurs
# A = [1, 2, 3] et B = [4, 5, 6] sans scipy.
# Formule : √(Σ(a_i - b_i)²)

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

distance = np.sqrt(np.sum((A - B)**2)) 

print(distance)


# Exercice 13
# Crée une fonction `standardiser(data)` qui centre-réduit un array :
# (x - moyenne) / écart-type
# Vérifie que le résultat a bien moyenne ≈ 0 et std ≈ 1.

def standardiser(data):
    return (data -np.mean(data)) / np.std(data)
        


print(standardiser(np.array([0,1,3,4,5])))
# Exercice 14
# Crée une matrice A (3x3) et calcule :
# - Sa transposée
# - Son inverse (si possible)
# - Le produit A @ A^(-1) — doit donner l'identité

A = np.arange(19,28).reshape(3,3)
print(np.transpose(A))
print(np.linalg.inv(A))
print(A@np.linalg.inv(A))



# Exercice 15
# Crée deux matrices aléatoires A (4x3) et B (3x5).
# Effectue leur produit matriciel.
# Affiche les shapes avant et après.
A = np.arange(0,12).reshape(4,3)
B = np.arange(0,15).reshape(3,5)

Mul = np.dot(A,B)
print(Mul)

print(np.shape(Mul))


# Exercice 16
# Crée un array 2D de shape (6, 4).
# Calcule la somme, moyenne et écart-type :
# - Sur toutes les valeurs (axis=None)
# - Par colonne (axis=0)
# - Par ligne (axis=1)

c = np.arange(0,24).reshape(6,4)
print(c)

print(np.sum(c), np.mean(c), np.var(c))
print(np.sum(c,axis=0), np.mean(c,axis=0), np.var(c,axis=0))
print(np.sum(c,axis=1), np.mean(c,axis=1), np.var(c,axis=1))

# Exercice 17
# Crée un array [1, 2, 3, ..., 12] et reshape-le en :
# - (3, 4)
# - (2, 6)
# - (2, 2, 3)
# Affiche chaque résultat.

D = np.arange(0,12).reshape(3,4)
D1 = np.arange(0,12).reshape(2,6)
D2 = np.arange(0,12).reshape(2,2,3)
print(D,D1,D2)

# Exercice 18
# Applique la fonction ReLU vectorisée sur :
data = np.array([-3, -1, 0, 2, 5, -0.5])
# Sans boucle for. (hint: np.maximum ou np.where)

max_data = np.maximum(data,0)
print(max_data)
# Exercice 19
# Crée une fonction `softmax(x)` qui calcule :
# softmax(x_i) = e^x_i / Σ(e^x_j)

# Vérifie que la somme des sorties = 1.

def softmax(x):
        return  np.exp(x) / np.sum(np.exp(x))

x = np.array([1.0, 2.0, 3.0])
print(softmax(x))

# Exercice 20
# Mesure le temps d'exécution de deux approches pour sommer
# 1 million de nombres :
# 1. Avec une boucle Python
# 2. Avec np.sum()
# Utilise time.perf_counter() et compare.
import time
debut = time.perf_counter()
sum = 0
for i in range(10**6):
    sum += i

fin = time.perf_counter()
n = fin-debut
print(n)

debut1 = time.perf_counter()
np.sum(np.arange(10**6))
fin1 = time.perf_counter()

m =fin1-debut1
print(m)




# ============================================================
# PARTIE 3 — PANDAS : BASES (Ex 21 à 30)
# ============================================================

# Exercice 21
# Crée un DataFrame avec ces données :
# Nom      : ["Alice", "Bob", "Charlie", "Diana", "Eve"]
# Age      : [25, 30, 35, 28, 22]
# Salaire  : [45000, 55000, 65000, 50000, 40000]
# Ville    : ["Paris", "Lyon", "Paris", "Bordeaux", "Lyon"]
# Affiche les 3 premières lignes avec .head()

data = pd.DataFrame({"nom":["Alice", "Bob", "Charlie", "Diana", "Eve"],
                    "Age":[25, 30, 35, 28, 22],
                    "Salaire":[45000, 55000, 65000, 50000, 40000],
                    "Ville": ["Paris", "Lyon", "Paris", "Bordeaux", "Lyon"]})

print(data.head())

# Exercice 22
# Avec le DataFrame de l'ex 21 :
# - Affiche les infos générales (.info())
# - Affiche les statistiques descriptives (.describe())
# - Affiche uniquement la colonne "Salaire"

print(data.info())
print(data.describe())
print(data['Salaire'])



# Exercice 23
# Avec le DataFrame de l'ex 21 :
# - Sélectionne les personnes de plus de 27 ans
# - Sélectionne les personnes de Paris avec salaire > 50000
# - Affiche le nom et salaire des personnes de Lyon

condition1 = data['Age'] > 27
print(data[condition1])


condition2 = (data['Ville'] == "Paris") & (data['Salaire'] > 50000)
print(data[condition2])

condition3 = data.loc[data['Ville'] == "Lyon",['nom','Salaire']]
print(condition3)
# Exercice 24
# Avec le DataFrame de l'ex 21 :
# - Ajoute une colonne "Salaire_mensuel" = Salaire / 12
# - Ajoute une colonne "Senior" = True si Age >= 30, sinon False
# - Supprime la colonne "Ville"

data["Salaire_mensuel"] = data["Salaire"]/12

data["Senior"] = data["Age"]

data.drop("Ville", axis=1, inplace=True)

print(data.head())
# Exercice 25
# Crée un DataFrame avec des valeurs manquantes (NaN) :
# data = {"A": [1, None, 3], "B": [4, 5, None], "C": [None, 8, 9]}
# - Détecte les NaN avec .isnull()
# - Remplace les NaN par la moyenne de chaque colonne
# - Supprime les lignes qui ont au moins un NaN (sur le df original)

df = pd.DataFrame({"a": [1, None, 3],
                    "B":[4, 5, None],
                    "C":[None, 8, 9],
                    })


print(df.isnull())
print(df.fillna(df.mean()))
print(df.dropna())

# Exercice 26
# Avec le DataFrame de l'ex 21 :
# - Trie par Salaire décroissant
# - Trie par Ville puis par Age croissant
# - Réinitialise l'index après le tri


print(data.sort_values("Salaire",ascending=False))
tri_2 = data.sort_values(by=['Ville', 'Age'], ascending=True)
print (tri_2)

print(data.reset_index(drop="True"))
# Exercice 27
# Avec le DataFrame de l'ex 21 :
# - Calcule le salaire moyen par ville (.groupby())
# - Calcule l'âge max et min par ville
# - Compte le nombre de personnes par ville

print(data.groupby("Ville")["Salaire"].mean())
print(data.groupby("Ville")["Age"].agg([min, max]))
print(data.groupby("Ville")["nom"].count())

# Exercice 28
# Renomme les colonnes du DataFrame de l'ex 21 :
# "Nom" → "name", "Age" → "age", "Salaire" → "salary"
# Puis change l'index pour que ce soit le nom des personnes

new_data = data.rename(columns={"nom":"name", "Age":"age","Salaire":"salary"})
print(new_data)
new_data = new_data.set_index("name")

print(new_data.head())

import seaborn as sns

sns.pairplot(new_data)

print(sns.pairplot(new_data))

# Exercice 29
# Crée deux DataFrames et fusionne-les :
# df1 : ID=[1,2,3], Nom=["Alice","Bob","Charlie"]
# df2 : ID=[2,3,4], Score=[85, 90, 78]
# Fusionne avec pd.merge() — teste inner, left et outer join.

df1 = pd.DataFrame({
    "ID": [1,2,3],
    "Nom": ["Alice","Bob","Charlie"]
})


df2 = pd.DataFrame({
    "ID": [2,3,4],
    "Score": [85,90,78]
})

print(pd.merge(df1,df2,how="inner"))
print(pd.merge(df1,df2,how="left"))
print(pd.merge(df1,df2,how="right"))
print(pd.merge(df1,df2,how="outer"))

# Exercice 30
# Crée un DataFrame de 100 lignes avec des données aléatoires :
# - Colonne "valeur" : entiers entre 0 et 100
# - Colonne "categorie" : choix aléatoire entre []
# Calcule la moyenne de "valeur" par "categorie".


data_100 = pd.DataFrame({
    'valeurs': np.random.randint(0, 100, size=100),
    'Categorie' : np.random.choice(["A", "B", "C"], size=100)
})

N = data_100.groupby("Categorie")["valeurs"].mean()
print(N)




# ============================================================
# PARTIE 4 — PANDAS : MANIPULATION AVANCÉE (Ex 31 à 40)
# ============================================================

# Exercice 31
# Crée un DataFrame avec une colonne "date" de 10 dates consécutives
# à partir du 01/01/2024, et une colonne "ventes" aléatoires.
# Hint : pd.date_range()

data_date = pd.date_range("2024-01-01", periods= 10, freq="D")
print(data_date)

df_date = pd.DataFrame({
                    "date": data_date,
                    "ventes": np.random.random(size=10)
                    })
print(df_date)
# Exercice 32
# Avec le DataFrame de l'ex 21 :
# - Applique une fonction lambda sur "Salaire" pour ajouter 10%
# - Applique .apply() pour créer une colonne "Categorie_age" :
#   < 25 → "Junior" | 25-32 → "Mid" | > 32 → "Senior"
# 'x' représente chaque valeur individuelle de la colonne
new_data["salary"] = new_data["salary"].apply(lambda x:x *1.1)
new_data["categorie_age"] = new_data["age"].apply(lambda x: "Junior" if x<25 else("Mid" if x<=32 else"Senior" )) 
new_data.head()

# Exercice 33
# Crée un DataFrame "large" avec des colonnes A, B, C, D.
# Transforme-le en format "long" avec pd.melt().
# Puis retransforme en format "wide" avec .pivot().

large = pd.DataFrame({
    "A" : "",
    "B" : "",
    "c" : "",
    "d" : ""
})
long = pd.melt(large, id_vars="id", var_name="variable", value_name="valeur")
print(long)
wide = long.pivot(index="id", columns="variable", values="valeur")
print(wide)

# Exercice 34
# Crée un DataFrame avec des doublons :
# data = {"Nom": ["Alice","Bob","Alice","Charlie","Bob"],
#         "Score": [85, 90, 85, 78, 95]}
# - Détecte les doublons avec .duplicated()
# - Supprime les doublons avec .drop_duplicates()

data = pd.DataFrame({"Nom": ["Alice","Bob","Alice","Charlie","Bob"],
                    "Score": [85, 90, 85, 78, 95]})

print(data.duplicated())
print(data.drop_duplicates())

# Exercice 35
# Avec le DataFrame de l'ex 21 :
# - Utilise .loc[] pour sélectionner par label
# - Utilise .iloc[] pour sélectionner par position
# - Quelle est la différence entre les deux ?


new_data.loc["Alice"]
new_data.iloc[0]
# Exercice 36
# Crée un DataFrame de ventes mensuelles sur 2 ans.
# Calcule la moyenne mobile sur 3 mois avec .rolling(3).mean()
# et affiche les résultats.

dates = pd.date_range(start='2024-01-01', periods=24, freq='MS')
ventes = np.random.randint(10000, 50000, size=24) + np.arange(24) * 500

# 3. Assemblage du DataFrame
df_ventes = pd.DataFrame({
    'Mois': dates,
    'Chiffre_Affaire': ventes,
})

print(df_ventes.rolling(3).mean()) 
# Exercice 37
# Crée un DataFrame avec une colonne texte "description".
# Utilise les méthodes str de Pandas pour :
# - Mettre en majuscules
# - Extraire les mots contenant "data"
# - Compter la longueur de chaque chaîne

un_Dataframe = pd.DataFrame({
    "description" : ""
})
print(un_Dataframe["description"].str.upper())
print(un_Dataframe["description"].str.contains("data"))
print(un_Dataframe["description"].str.len())
# Exercice 38
# Charge un DataFrame depuis un dictionnaire, puis :
# - Exporte-le en CSV avec .to_csv()
# - Recharge-le depuis le CSV avec pd.read_csv()
# - Vérifie que les deux DataFrames sont identiques

dict = {}

data_dict = pd.DataFrame(dict)
data_dict_csv = data_dict.to_csv("data.csv", index=False)

dict_frame = pd.read_csv("data.csv")
print(data_dict, dict_frame)
# Exercice 39
# Crée un DataFrame avec MultiIndex :
# Index niveau 1 : ["2023", "2024"]
# Index niveau 2 : ["Q1", "Q2", "Q3", "Q4"]
# Colonne "chiffre_affaires" avec des valeurs aléatoires.
# Accède aux données de 2024 Q2.

index = pd.MultiIndex.from_product([["2023","2024"],["Q1","Q2","Q3","Q4"]])
df_multi = pd.DataFrame({"chiffre_affaires": np.random.randint(1000,9999,8)}, index=index)
print(df_multi.loc["2024","Q2"])  
# Exercice 40
# Crée deux Series Pandas et effectue des opérations :
# s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
# s1 = pd.Series([1, 2, 3], index=["b", "c", "d"])
# - Addition (observe ce qui se passe avec les index manquants)
# - Remplis les NaN avec 0
s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
s2 = pd.Series([1, 2, 3], index=["b", "c", "d"])

s3 = s1 + s2
print(s3)
s3.fillna(0)
# ============================================================
# PARTIE 5 — NUMPY + PANDAS APPLIQUÉS AU ML (Ex 41 à 50)
# ============================================================

# Exercice 41
# Charge ce dataset "maison" en DataFrame :
# surface=[50,60,70,80,90,100], prix=[150,180,210,230,270,300]
# - Normalise la colonne "surface" entre 0 et 1
# - Affiche la corrélation entre surface et prix (.corr())




Maison = pd.DataFrame({
    "surface" :[50,60,70,80,90,100],
    "prix"    :[150,180,210,230,270,300]
})

Maison["surface_norm"] = (Maison["surface"] - Maison["surface"].min()) / (Maison["surface"].max() - Maison["surface"].min())
print(Maison.corr())  # 




# Exercice 42
# Avec le dataset de l'ex 41 :
# - Convertis en arrays NumPy
# - Ajoute une colonne de biais (ones) à X
# - Résous la régression linéaire avec l'équation normale

Surface_numpy = np.array([50,60,70,80,90,100])
prix_numpy = np.array([150,180,210,230,270,300])


X = np.column_stack(Surface_numpy,np.ones(shape=6))
w = np.linalg.inv(X.T @ X) @ X.T @ prix_numpy
print(w)

# Exercice 43
# Crée un DataFrame de 200 étudiants avec :
# - "note_maths" et "note_info" : entiers entre 0 et 20
# - "admis" : 1 si moyenne >= 10, sinon 0
# Calcule le taux d'admission et la note moyenne par statut.

etudiants = pd.DataFrame({
    "note_maths" : np.random.randint(0,20, size=200),
    "note_info" : np.random.randint(0,20, size=200)
})

etudiants["admis"] = ((etudiants["note_maths"]+etudiants["note_info"])/2 >= 10).astype(int)


# Exercice 44
# Avec le DataFrame de l'ex 43 :
# - Crée X (les deux notes) et y (admis) en NumPy
# - Normalise X avec ta fonction standardiser()
# - Vérifie les shapes de X et y

X = etudiants["note_maths"], etudiants["note_info"]
Y = np.array(etudiants["admis"])

standardiser(X)

print(np.shape(X))
print(np.shape(Y))
# Exercice 45
# Implémente un train/test split sans sklearn :
# Prends le dataset de l'ex 43.
# 80% train, 20% test — mélange aléatoire avec np.random.shuffle().
def train_test_split(X, y, ratio=0.8):
    indices = np.arange(len(X))
    np.random.shuffle(indices)
    coupure = int(len(indices) * 0.8)
    
    X_train = X[indices[:coupure]]
    X_test  = X[indices[coupure:]]
    y_train = y[indices[:coupure]]
    y_test  = y[indices[coupure:]]
    
    return X_train, X_test, y_train, y_test

# Exercice 46
# Crée une fonction `confusion_matrix_manuelle(y_true, y_pred)`
# qui retourne un DataFrame Pandas avec :
# - Vrais positifs, faux positifs, vrais négatifs, faux négatifs

def confusion_matrix_manuelle(y_true, y_pred):
    dataFrame = pd.DataFrame({
        "Vrais positifs" : y_true,
        "faux positifs" : y_true or y_pred,
        "Vrais negatifs" : y_true & y_pred,
        "faux negatifs" : y_pred,
    })
    return dataFrame

# Exercice 47
# Crée un DataFrame de séries temporelles :
# - 365 jours de données
# - Colonne "temperature" : valeurs aléatoires normales (µ=20, σ=5)
# - Resample par mois et calcule la température moyenne mensuelle
# Hint : .resample("ME").mean() avec un DatetimeIndex
# Créer 365 jours de dates
dates = pd.date_range(start="2024-01-01", periods=365, freq="D")

# DataFrame avec températures aléatoires
df = pd.DataFrame({
    "temperature": np.random.normal(loc=20, scale=5, size=365)
}, index=dates)  # ← l'index c'est les dates !

print(df.head())
# Regroupe par mois et calcule la moyenne
df_monthly = df.resample("ME").mean()
print(df_monthly)

pd.Series()
# Exercice 48
# Crée une fonction `batch_generator(X, y, batch_size)` qui :
# - Prend un array NumPy X et y
# - Retourne des mini-batches de taille batch_size
# - Utilise yield (générateur Python)
def batch_generator(X, y, batch_size):
    n = len(X)
    for debut in range(0, n, batch_size):
        fin = min(debut + batch_size, n)
        yield X[debut:fin], y[debut:fin]
# Exercice 49
# Crée un pipeline de prétraitement complet :
# 1. Charger un DataFrame avec des NaN et des doublons
# 2. Supprimer les doublons
# 3. Remplir les NaN par la médiane
# 4. Normaliser toutes les colonnes numériques
# 5. Retourner un array NumPy prêt pour un modèle ML
df_brut = pd.DataFrame({
    "A": [1, 2, None, 2, 5],
    "B": [3, None, 5, 3, 8],
    "C": [2, 4, 6, 4, 10]
})

def pipeline(df):
    df = df.drop_duplicates()
    df = df.fillna(df.median())
    df = (df - df.min()) / (df.max() - df.min())
    return df.values  # .values retourne l'array NumPy 


# Exercice 50 — Boss Final 🎯
# Implémente une régression linéaire complète de A à Z :
#
# Données :
np.random.seed(42)
X = np.random.randn(100, 2)   # 100 exemples, 2 features
y = 3*X[:,0] - 2*X[:,1] + np.random.randn(100)*0.1
#
# Étapes :
# 1. Mets les données dans un DataFrame Pandas avec colonnes ["x1","x2","y"]

donnees = pd.DataFrame({
                        "x1": X[:,0],
                        "x2": X[:,1],
                        "y": y
})
# 2. Analyse exploratoire : .describe(), corrélations
donnees.describe()
donnees.corr()
# 3. Convertis en NumPy, ajoute colonne de biais
donnees_numpy = donnees.values()


# 4. Train/test split 80/20
indices = np.arange(len(donnees))
np.random.shuffle(indices)
coupure = int(len(indices)*0.8)

x_train = donnees[indices[:coupure]]
x_test = donnees[indices[coupure:]]
# 5. Entraîne avec l'équation normale sur le train set
x = np.column_stack([np.ones(100), x_train])
X_train, X_test, y_train, y_test = train_test_split(x, y, 0.8)

# Étape 5 : Équation normale
w = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ y_train

# Étape 6 : Prédiction
y_pred = X_test @ w

# Étape 7 : MSE et R²
mse = np.mean((y_pred - y_test)**2)
ss_res = np.sum((y_pred - y_test)**2)
ss_tot = np.sum((y_test - np.mean(y_test))**2)
r2 = 1 - ss_res/ss_tot
# 6. Prédit sur le test set

# 7. Calcule MSE et R² sur le test set
#    R² = 1 - SS_res/SS_tot où SS_res = Σ(y-ŷ)², SS_tot = Σ(y-ȳ)²
# 8. Affiche les coefficients trouvés — sont-ils proches de [3, -2] ?


# ============================================================
# TESTS RAPIDES — Décommente pour vérifier au fur et à mesure
# ============================================================

# Partie 1
# print(arr)                    # Ex 1
# print(identite)               # Ex 2
# print(arr_inv)                # Ex 3
# print(grandes_valeurs)        # Ex 4
# print(tenseur.shape)          # Ex 5
# print(max_elem)               # Ex 6
# print(matrice_modif)          # Ex 7
# print(linspace_arr)           # Ex 8
# print(sous_matrice, diag)     # Ex 9
# print(matrice_triee)          # Ex 10

# Partie 2
# print(data_norm)              # Ex 11
# print(distance)               # Ex 12
# print(np.mean(std_data), np.std(std_data))  # Ex 13
# print(A @ np.linalg.inv(A))   # Ex 14
# print(C.shape)                # Ex 15
# print(moyennes_col)           # Ex 16
# print(arr_3d.shape)           # Ex 17
# print(relu_result)            # Ex 18
# print(softmax_result.sum())   # Ex 19
# (affiche les temps)           # Ex 20

# Partie 3
# print(df.head())              # Ex 21
# print(df.describe())          # Ex 22
# print(df_paris_riche)         # Ex 23
# print(df.columns)             # Ex 24
# print(df_filled)              # Ex 25
# print(df_sorted)              # Ex 26
# print(df.groupby("Ville")["Salaire"].mean())  # Ex 27
# print(df.index)               # Ex 28
# print(df_merged)              # Ex 29
# print(df_alea.groupby("categorie")["valeur"].mean())  # Ex 30

# Partie 4
# print(df_dates.head())        # Ex 31
# print(df["Categorie_age"])    # Ex 32
# print(df_long)                # Ex 33
# print(df.drop_duplicates())   # Ex 34
# (affiche les sélections)      # Ex 35
# print(rolling_mean)           # Ex 36
# print(df["description"].str.upper())  # Ex 37
# print(df_reload.equals(df))   # Ex 38
# print(df_multi.loc["2024","Q2"])  # Ex 39
# print(s1.add(s2, fill_value=0))   # Ex 40

# Partie 5
# print(df_maison.corr())       # Ex 41
# print(w)                      # Ex 42
# print(taux_admission)         # Ex 43
# print(X_std.shape, y.shape)   # Ex 44
# print(X_train.shape, X_test.shape)  # Ex 45
# print(confusion)              # Ex 46
# print(df_monthly)             # Ex 47
# for xb, yb in batch_generator(X, y, 32): print(xb.shape)  # Ex 48
# print(X_ready.shape)          # Ex 49
# print(f"MSE={mse:.4f}, R²={r2:.4f}, w={w}")  # Ex 50
