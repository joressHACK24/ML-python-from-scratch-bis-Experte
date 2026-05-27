# ============================================================
# 50 EXERCICES — MATPLOTLIB & SEABORN
# Niveau : Intermédiaire
# Thème  : Visualisation pour le Deep Learning
# ============================================================
# Instructions :
#   - Complète chaque exercice sans regarder les solutions
#   - Soumets tout à la fin pour correction
#   - Sauvegarde chaque graphique avec plt.savefig("exN.png")
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# ============================================================
# PARTIE 1 — MATPLOTLIB : BASES (Ex 1 à 10)
# ============================================================

# Exercice 1
# Trace une courbe simple de sin(x) pour x ∈ [0, 2π]
# Ajoute : titre, label x, label y, couleur rouge
# Hint : np.linspace(0, 2*np.pi, 100)

x = np.linspace(0, 2*np.pi,100)
y = np.sin(x)
z = np.cos(x)


plt.title("sinus(x)")

plt.plot(x,y, c="blue")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

# Exercice 2
# Trace sin(x) ET cos(x) sur le même graphique.
# - sin en bleu, cos en orange
# - Ajoute une légende
# - Ajoute un titre "Sin et Cos"


plt.plot(x,z, c="orange", label="sin")
plt.plot(x,y, c="red", label="cos")
plt.legend()
plt.title(" sin et cos")
plt.show()



# Exercice 3
# Crée une figure avec 2 sous-graphiques côte à côte (1 ligne, 2 colonnes) :
# - Gauche : sin(x)
# - Droite : cos(x)
# Hint : plt.subplots(1, 2)
f,(ax1,ax2) = plt.subplots(1, 2)
ax1.plot(x,y, c="blue")
ax2.plot(x,z, c="orange")
plt.show()

# Exercice 4
# Trace un graphique en barres des ventes par trimestre :
trimestres = ["Q1", "Q2", "Q3", "Q4"]
ventes = [15000, 22000, 18000, 27000]
# Ajoute les valeurs au-dessus de chaque barre.

plt.bar(trimestres,ventes)
for i in range(len(ventes)):
    plt.text(i, ventes[i],ventes[i])
plt.show()



# Exercice 5
# Crée un histogramme de 1000 valeurs aléatoires normales (µ=0, σ=1).
# - bins=30
# - Ajoute une ligne verticale rouge à x=0 (hint: plt.axvline)
# - Titre : "Distribution normale"
data = np.random.normal(loc=0, scale =1, size=1000)

plt.hist(data, bins = 30)
plt.axvline(x=0, c="red")
plt.title("Distribution Normale")
plt.show()
# Exercice 6
# Crée un scatter plot (nuage de points) :
x = np.random.randn(200)
y = 2*x + np.random.randn(200)*0.5
# - Colorie les points selon leur valeur y (hint: c=y, cmap="viridis")
# - Ajoute une colorbar

plt.scatter(x,y, c=y,cmap="viridis")
plt.colorbar()
plt.show()

# Exercice 7
# Trace une courbe avec zone ombrée (erreur/incertitude) :
x = np.linspace(0, 10, 100)
y = np.sin(x)
erreur = 0.2
# Hint : 
plt.fill_between(x, y-erreur, y+erreur, alpha=0.3)
plt.show()




# Exercice 8
# Crée un graphique en secteurs (camembert) :
categories = ["Python", "NumPy", "Pandas", "Matplotlib", "Sklearn"]
tailles = [30, 20, 20, 15, 15]
explode = (0.1, 0, 0, 0, 0)  
# - Explode la plus grande part
plt.pie(tailles, labels=categories, explode=explode)
# - Ajoute les pourcentages

plt.pie(tailles, labels=categories)
plt.show()

# Exercice 9
# Crée une figure 2x2 avec 4 sous-graphiques :
# - (0,0) : sin(x)
# - (0,1) : cos(x)
# - (1,0) : tan(x) (limite à [-5, 5] sur y)
# - (1,1) : x²
# Hint : plt.subplots(2, 2)

x = np.linspace(-np.pi*2, np.pi*2,500)
x1 = np.linspace(-5, 5,1)
f,((ax1, ax2),(ax3,ax4)) = plt.subplots(2,2)
ax1.plot(x,np.sin(x),c="blue")
ax2.plot(x,np.cos(x),c="red")
ax3.plot(x,np.tan(x),c="yellow")
ax3.set_ylim(-5,5)
ax4.plot(x,x**2,c="green")
plt.show()
# Exercice 10
# Personnalise un graphique au maximum :
# - Change le style : plt.style.use("seaborn-v0_8")
# - Taille de figure : figsize=(10, 5)
# - Grille : plt.grid(True, linestyle="--", alpha=0.7)
# - Spine droit et haut invisibles
# - Trace y = x³ - 3x

x = np.linspace(0, 10**8,10**4)
y = x**3-3*x

plt.style.use("seaborn-v0_8")
plt.figure(figsize=(10,5))
plt.grid(True, linestyle="--", alpha=0.7)
plt.plot(x,y)
ax = plt.gca()
ax.spines["right"].set_visible(False) 
ax.spines["top"].set_visible(False)

plt.show()
# ============================================================
# PARTIE 2 — MATPLOTLIB : VISUALISATIONS AVANCÉES (Ex 11 à 20)
# ============================================================

# Exercice 11
# Trace la fonction de perte (loss) d'un entraînement fictif :
epochs = np.arange(1, 51)
train_loss = 2 * np.exp(-0.1 * epochs) + np.random.randn(50) * 0.05
val_loss   = 2 * np.exp(-0.08 * epochs) + np.random.randn(50) * 0.08
# - Deux courbes sur le même graphique
# - Marque le point de loss minimale avec un point rouge
plt.plot(epochs, train_loss, label="train", color ="red")
plt.plot(epochs, val_loss,label="val", c="green")
min_idx = np.argmin(val_loss)
plt.scatter(epochs[min_idx], val_loss[min_idx], color="red", zorder=5)  # ✅
plt.legend()
plt.show()


# Exercice 12
# Crée un box plot comparant 3 distributions :
data = [np.random.normal(0, 1, 100),
        np.random.normal(2, 1.5, 100),
        np.random.normal(-1, 0.5, 100)]
labels = ["Groupe A", "Groupe B", "Groupe C"]

plt.boxplot(data, labels=labels)
plt.show()

# Exercice 13
# Crée une heatmap d'une matrice de corrélation :
# Génère un DataFrame de 5 colonnes aléatoires corrélées
# Hint : df.corr() puis plt.imshow() ou sns.heatmap()
df = pd.DataFrame({
            "Q1": np.linspace(-5,100,96),
            "Q2": np.linspace(-15,110,96),
            "Q3": np.linspace(-25,120,96),
            "Q4": np.linspace(-35,130,96),
            "Q5": np.linspace(-45,140,96)
})

y = df.corr()

plt.imshow(y)
sns.heatmap(y, annot=True, cmap="coolwarm" )
plt.show()


# Exercice 14
# Visualise la fonction ReLU et Sigmoid sur [-5, 5] :
# - Les deux sur le même graphique
# - Ligne pointillée à x=0 et y=0
# - Légende
x = np.linspace(-5,5)
relu = np.maximum(0, x)
sigmoid = 1/(1+(np.exp(-x)))

plt.plot(x,relu, c="red")
plt.plot(x,sigmoid, c="blue")
plt.axvline(x=0, linestyle="--")
plt.axhline(y=0, linestyle="--")
plt.show()
# Exercice 15
# Crée un graphique de la descente de gradient :
# - Trace la parabole f(x) = x² - 4x + 5
# - Montre 5 étapes de descente de gradient
#   (pars de x=4, lr=0.3, f'(x)=2x-4)
# - Marque chaque étape avec un point

x_vals = [4.0]
for _ in range(5):
    x_new = x_vals[-1] - 0.3 * (2*x_vals[-1] - 4)
    x_vals.append(x_new)
x_curve = np.linspace(0, 5, 100)
plt.plot(x_curve, x_curve**2 - 4*x_curve + 5)
plt.scatter(x_vals, [x**2 - 4*x + 5 for x in x_vals], color="red", zorder=5)
# Exercice 16
# Crée un graphique avec deux axes y différents (twin axes) :
x = np.arange(12)
temperature = [5, 7, 12, 18, 22, 28, 30, 29, 24, 17, 10, 6]
precipitations = [80, 65, 70, 55, 45, 30, 20, 25, 50, 75, 85, 90]
# Hint : ax2 = ax1.twinx()
f, ax1 = plt.subplots(1,1)
ax2 = ax1.twinx()

ax1.plot(x,temperature)
ax2.plot(x,precipitations)
plt.show()
# Exercice 17
# Visualise une matrice de confusion 2x2 :
conf_matrix = np.array([[85, 15], [10, 90]])
# - Heatmap avec annotations
# - Labels : "Négatif", "Positif"

sns.heatmap(conf_matrix, annot=True, fmt="d",
            xticklabels=["Négatif","Positif"],
            yticklabels=["Négatif","Positif"])
plt.show()


# Exercice 18
# Trace des courbes d'apprentissage avec plusieurs learning rates :
# lr_values = [0.001, 0.01, 0.1]
# Pour chaque lr, simule une loss : 1 / (1 + lr * epochs)
# - Une courbe par lr avec label


lr_values = [0.001, 0.01, 0.1]
for lr in lr_values:
    loss = 1 / (1 + lr * epochs)
    plt.plot(epochs, loss, label =f"lr={lr}")
plt.show()
# Exercice 19
# Crée un graphique de distribution comparant avant/après normalisation :
data_raw = np.random.exponential(scale=2, size=1000)
data_norm = (data_raw - data_raw.mean()) / data_raw.std()
# - Deux histogrammes côte à côte (subplot)

f, (ax1,ax2) = plt.subplots(1,2)
ax1.hist(data_raw)
ax2.hist(data_norm)
plt.show()

# Exercice 20
# Visualise des embeddings 2D avec des couleurs par classe :
np.random.seed(42)
X = np.random.randn(150, 2)
y = np.repeat([0, 1, 2], 50)  # 3 classes
# - Scatter plot coloré par classe
couleurs = ["red", "blue", "green"]
noms = ["Chat", "Chien", "Oiseau"]

for i , nom in enumerate(noms):
    mask = y==i
    plt.scatter(X[mask,0],X[mask,0], label=nom, c=couleurs[i])
plt.legend()
plt.show()

# ============================================================
# PARTIE 3 — SEABORN : BASES (Ex 21 à 30)
# ============================================================

# Exercice 21
# Crée un DataFrame de 200 étudiants avec note_maths, note_info, mention.
# Trace un sns.histplot de note_maths avec kde=True.

df_etudiants = pd.DataFrame({
                "note_maths" : np.random.randint(0,20,200),
                "note_info" : np.random.randint(0,20,200)
})
df_etudiants["mention"] = df_etudiants["note_maths"].apply(lambda x: "Passable" if x<11 else("Assez bien" if x<15 else"bien" )) 
sns.histplot(df_etudiants["note_maths"], kde=True)
plt.show()


# Exercice 22
# Avec le DataFrame de l'ex 21 :
# Trace un sns.boxplot de note_maths par mention.

sns.boxplot(y=df_etudiants["note_maths"],x=df_etudiants["mention"])
plt.show()


# Exercice 23
# Avec le DataFrame de l'ex 21 :
# Trace un sns.scatterplot de note_maths vs note_info
# colorié par mention. (hint: hue="mention")

sns.scatterplot(x=df_etudiants["note_maths"], y=df_etudiants["note_info"], hue=df_etudiants["mention"])  
plt.show()

# Exercice 24
# Utilise le dataset "tips" intégré à Seaborn :
# df = sns.load_dataset("tips")
# Trace un sns.barplot du pourboire moyen par jour.

import seaborn as sns 
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
df.head()
sns.barplot(x=df["day"], y=df["tip"])
plt.show()
# Exercice 25
# Avec le dataset "tips" :
# Trace un sns.violinplot du total_bill par jour.
sns.violinplot(x=df["day"], y=df["total_bill"])
plt.show()


# Exercice 26
# Avec le dataset "tips" :
# Trace un sns.heatmap de la table pivot :
pivot = df.pivot_table(values="tip", index="day", columns="time")
sns.heatmap(pivot)
plt.show()


# Exercice 27
# Utilise le dataset "iris" intégré à Seaborn :
# df = sns.load_dataset("iris")
# Trace un sns.pairplot colorié par species.

df_iris = sns.load_dataset("iris")
sns.pairplot(df_iris, hue="species")
plt.show()


# Exercice 28
# Avec le dataset "iris" :
# Trace un sns.boxplot de sepal_length par species.
# Ajoute les points individuels avec sns.stripplot par dessus.

sns.boxplot(x=df_iris["sepal_length"], y=df_iris["species"])
sns.stripplot(x=df_iris["sepal_length"], y=df_iris["species"])
plt.show()

# Exercice 29
# Trace un sns.regplot (régression linéaire) de :
x = np.random.randn(100)
y = 2*x + np.random.randn(100)*0.5
# Affiche l'intervalle de confiance à 95%.

m = np.mean(x)
u = np.std(x)

sns.regplot(x=x,y=y)
plt.show()
# Exercice 30
# Avec le dataset "titanic" intégré à Seaborn :
# df = sns.load_dataset("titanic")
# Trace un sns.countplot du nombre de survivants par classe (pclass).
# Hint : hue="survived"

df_titanic = sns.load_dataset("titanic")
sns.countplot(data=df_titanic, x="pclass", hue="survived")
plt.show()
# ============================================================
# PARTIE 4 — SEABORN : VISUALISATIONS AVANCÉES (Ex 31 à 40)
# ============================================================

# Exercice 31
# Crée un sns.clustermap avec le dataset "iris" (sans colonne species).
# Observe comment les espèces se regroupent naturellement.
df_iris = sns.load_dataset("iris").drop("species", axis=1)
sns.clustermap(df_iris)
plt.show()



# Exercice 32
# Avec le dataset "tips" :
# Trace un sns.FacetGrid pour montrer la distribution du total_bill
# séparément pour chaque jour (col="day").

df_tips = sns.load_dataset("tips")
g = sns.FacetGrid(data = df_tips, row="total_bill", col="day")
g.map(sns.histplot, "total_bill")
plt.show()

# Exercice 33
# Crée un sns.jointplot de note_maths vs note_info (ex 21)
# avec kind="hex" pour voir la densité.

sns.jointplot(x=df_etudiants["note_maths"], y=df_etudiants["note_info"], kind="hex")
plt.show()
# Exercice 34
# Trace un sns.heatmap de la matrice de corrélation du dataset "iris"
# (sans colonne species).
# - annot=True pour afficher les valeurs
# - cmap="coolwarm"
# - Masque le triangle supérieur (hint: np.triu)

df_iris = sns.load_dataset("iris")
sns.heatmap(df_iris, annot=True, cmap="coolwarm")
plt.show()
# Exercice 35
# Avec le dataset "titanic" :
# Trace un sns.barplot du taux de survie moyen
# par sexe ET par classe (hue="sex").
sns.barplot(df_titanic["survived"], hue="sex")
sns.barplot(df_titanic["survived"], hue="pclass")
plt.show()

# Exercice 36
# Crée un graphique avec sns.kdeplot pour comparer
# la distribution de sepal_length par espèce (iris).
# - fill=True, alpha=0.4
# - Les 3 espèces sur le même graphique

df_iris2 = sns.load_dataset("iris")
for species in df_iris2["species"].unique():
    subset = df_iris2[df_iris2["species"] == species]
    sns.kdeplot(subset["sepal_length"], fill=True, alpha=0.4, label=species)
plt.legend()
plt.show()

# Exercice 37
# Avec le dataset "tips" :
# Trace un sns.lmplot de total_bill vs tip
# séparé par smoker (col="smoker").

sns.lmplot(data=df_tips, x="total_bill", y="tip", col="smoker")
plt.show()
# Exercice 38
# Crée un "ridgeline plot" simulé avec plusieurs kdeplot :
# Génère 5 groupes de données normales avec des moyennes différentes.
# Décale verticalement chaque courbe pour l'effet ridgeline.




# Exercice 39
# Avec le dataset "iris" :
# Crée un graphique combiné :
# - sns.scatterplot sepal_length vs sepal_width
# - colorié par species
# - Ajoute les ellipses de confiance pour chaque classe
# Hint : utilise matplotlib.patches.Ellipse
dataset_iris = sns.load_dataset("iris")
sns.scatterplot(x=dataset_iris["sepal_length"],y=dataset_iris["sepal_width"], color="species")
matplotlib.patches.Ellipse()

# Exercice 40
dataset_tips = sns.load_dataset("tips")
# Crée un dashboard de 4 graphiques sur le dataset "tips" :
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
sns.hisplot(dataset_tips["total_bill"], ax=axes[0,0])
sns.boxplot(y=dataset_tips["total_bill"], x=dataset_tips["day"], ax=axes[0,1])
sns.scatterplot(x=dataset_tips["total_bill"], y=dataset_tips["tip"],ax=axes[1,0])
sns.barplot(x=dataset_tips["day"],y=dataset_tips["tip"], ax=axes[0,1])
# - (0,1) : total_bill par jour (boxplot)
# - (1,0) : total_bill vs tip (scatterplot)
# - (1,1) : taux survie par jour (barplot)
fig.suptitle("Analyse Tips Dataset")
plt.show()

# ============================================================
# PARTIE 5 — VISUALISATION APPLIQUÉE AU ML (Ex 41 à 50)
# ============================================================

# Exercice 41
# Visualise la courbe de loss ET d'accuracy pendant l'entraînement :
# Simule 100 epochs :
epochs = np.arange(1,101)
loss     = 1 / (1 + 0.1*epochs) + np.random.randn(100)*0.01
accuracy = 1 - loss + np.random.randn(100)*0.01
# - 2 sous-graphiques verticals (2 lignes, 1 colonne)


fig,(a1,a2) = plt.subplots(2,1, figsize=(50,50))

a1.plot(loss)
a2.plot(accuracy)
plt.show()
plt.plot

# Exercice 42
# Visualise la frontière de décision d'un classifieur linéaire :
np.random.seed(42)
X = np.random.randn(100, 2)
y = (X[:,0] + X[:,1] > 0).astype(int)
y = (X[:,0] + X[:,1] > 0).astype(int)



plt.scatter(X[:,0],X[:,1], c=y, cmap="bwr")
x_line = np.linspace(-3, 3, 100)
plt.plot(x_line, -x_line, "k--", label="x1+x2=0")
plt.show()
# - Scatter plot coloré par classe
# - Trace la droite de séparation x1 + x2 = 0





# Exercice 43
# Visualise une matrice de confusion complète avec :
y_true = np.array([0,0,1,1,0,1,0,1,1,0])
y_pred = np.array([0,1,1,0,0,1,0,1,0,0])
# - Heatmap annotée
# - Calcule accuracy, precision, recall à la main
# - Affiche-les dans le titre

sns.heatmap(y_true,y_pred, annot=True)



# Exercice 44
# Trace une courbe ROC simplifiée :
# Génère des scores de probabilité aléatoires pour 100 exemples.
# - Trie par score décroissant
# - Calcule TPR et FPR à chaque seuil
# - Trace TPR vs FPR
# - Trace la diagonale (classifieur aléatoire)



# Exercice 45
# Visualise l'effet du learning rate sur la convergence :
# Pour lr ∈ [0.001, 0.01, 0.1, 0.5] :
# Simule 50 steps de descente de gradient sur f(x)=x²
# (x_new = x - lr * 2*x, départ x=5)
# - Une courbe de convergence par lr
lrs = [0.001, 0.01, 0.1, 0.5]
x = np.linspace(5,54,50)


for lr in lrs:
    x_val, historique = 5.0,[]
    for _ in range(50):
        x_val = x_val - lr * 2 * x_val  # ✅ step gradient
        historique.append(x_val**2)
    plt.plot(historique, label=f"lr={lr}")
plt.legend()
plt.show()




# Exercice 46
# Visualise la distribution des poids d'un réseau de neurones :
# Génère 3 couches avec des poids aléatoires normaux :
layer1 = np.random.randn(64, 32)
layer2 = np.random.randn(32, 16)
layer3 = np.random.randn(16, 1)
# - Histogramme 

fig, ((A,B,C))= plt.subplots(1,3)
A.hist(layer1.flatten(), bins=30)
B.hist(layer2)
C.hist(layer3)
plt.show()


# Exercice 47
# Visualise l'overfitting :
epochs = np.arange(1, 51)
train_loss = 0.5*np.exp(-0.1*epochs) + 0.05
val_loss   = 0.5*np.exp(-0.05*epochs) + 0.3*np.exp(0.02*epochs)
# - Marque le point où val_loss commence à remonter
# - Zone rouge après ce point (overfitting)
overfitting_start = np.argmin(val_loss)
plt.axvspan(overfitting_start, len(epochs), color="red", alpha=0.1) 
plt.show()



# Exercice 48
# Visualise des feature importances (importance des variables) :
features = ["age", "salaire", "experience", "diplome", "ville"]
importances = np.array([0.35, 0.25, 0.20, 0.12, 0.08])
# - Barplot horizontal trié par importance décroissante
# - Colorbar selon l'importance

idx = np.argsort(importances)[::-1]
plt.barh([features[i] for i in idx], importances[idx]) 
plt.show()



# Exercice 49
# Crée un graphique d'analyse en composantes principales (PCA visuelle) :
# Génère 3 clusters de données 2D.
# - Scatter plot coloré par cluster
# - Trace les axes principaux (vecteurs propres)
# - Hint : np.linalg.eig sur la matrice de covariance



# Exercice 50 — Boss Final 🎯
# Crée un rapport visuel complet sur le dataset "iris" :
# fig avec 6 sous-graphiques (2 lignes x 3 colonnes) :
# - (0,0) : Distribution sepal_length par espèce (kdeplot)
# - (0,1) : Matrice de corrélation (heatmap)
# - (0,2) : Pairwise scatter sepal_length vs petal_length (scatterplot)
# - (1,0) : Boxplot de toutes les features par espèce
# - (1,1) : Barplot des moyennes par espèce
# - (1,2) : Scatter 2D coloré par espèce avec ellipses
# Titre global : "Rapport d'analyse — Dataset Iris"
# Sauvegarde en PNG : plt.savefig("rapport_iris.png", dpi=150)


data_final_iris = sns.load_dataset("iris")

fig, axes= plt.subplots(2,3)

A= axes[0,0]
B= axes[0,1]
C= axes[1,0]
D= axes[0,2]
E= axes[1,1]
F= axes[1,2]
print(data_final_iris.head())
data_final_iris2 = sns.load_dataset("iris")
data_final_iris2.drop("species", axis=1, inplace=True)

A.plot(data_final_iris["sepal_length"], data_final_iris["species"])
sns.heatmap(data_final_iris2.corr(), ax=B)
C.scatter(x=data_final_iris["sepal_length"], y=data_final_iris["petal_length"])
moy = (data_final_iris["sepal_length"] + data_final_iris["petal_length"])/2
D.bar(height=moy, x=data_final_iris["species"])
sns.boxplot(x= data_final_iris2["sepal_length"], y = data_final_iris["species"], ax=E)
sns.boxplot(x= data_final_iris2["petal_length"], y = data_final_iris["species"], ax=E)
sns.boxplot(x= data_final_iris2["sepal_width"], y = data_final_iris["species"], ax=E)
sns.boxplot(x= data_final_iris2["petal_width"], y = data_final_iris["species"], ax=E)
sns.scatterplot(x=data_final_iris["sepal_length"], y=data_final_iris["petal_length"], style=Ellipsis,palette="red", ax=F)

plt.savefig("rapport_iris.png", dpi=150)
plt.show()

