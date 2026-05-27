# ============================================================
# 50 EXERCICES — CLASSES & MODULES PYTHON
# Niveau : Intermédiaire
# Thème  : POO pour le Deep Learning
# ============================================================
# Instructions :
#   - Complète chaque exercice sans regarder les solutions
#   - Soumets tout à la fin pour correction
#   - Les exercices sont progressifs (1 = facile, 50 = avancé)
# ============================================================


import numpy as np

# ============================================================
# PARTIE 1 — BASES DES CLASSES (Exercices 1 à 10)
# ============================================================

# Exercice 1
# Crée une classe Animal avec un attribut `nom` et une méthode `parler()`
# qui affiche "Je suis <nom>"
class Animal:
    def __init__(self,nom):
        self.nom = nom
    def parler(self):
        print(f"je suis {self.nom}")
        
    
mon_Animal = Animal("Roxy")
mon_Animal.parler()
# Exercice 2
# Crée une classe Rectangle avec largeur et hauteur.
# Ajoute une méthode `aire()` qui retourne largeur × hauteur.
class Rectangle:
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    def aire(self):
        print(f"l'aire du rectangle est: {self.largeur*self.hauteur}")

Mon_Rectangle = Rectangle(2,4)
Mon_Rectangle.aire()
        



# Exercice 3
# Crée une classe Cercle avec un attribut `rayon`.
# Ajoute les méthodes `aire()` et `perimetre()`.
# Utilise math.pi
import math
class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon
    def aire(self):
        aire = math.pi*(self.rayon)**2
        print("l'aire du cercle est:",aire)
    def perimetre(self):
        perimetre = math.pi*(self.rayon)*2
        print("l'aire du cercle est:",perimetre)


mon_cercle = Cercle(5.7)
mon_cercle.aire()
mon_cercle.perimetre()

# Exercice 4
# Crée une classe Compteur avec un attribut `valeur = 0`.
# Ajoute les méthodes `incrementer()`, `decrementer()` et `reset()`.
class Compteur:
    def __init__(self,valeur=0):
        self.valeur = valeur
    def incrementer(self):
        self.valeur += 1
        print(f"valeur incrementée est:{self.valeur}")
    def decrementer(self):
        self.valeur -= 1
        print(f"la valeur decrementée est: {self.valeur}")
    def reset(self):
        print(f" la valeur etait: {self.valeur}")

mon_compteur = Compteur()
mon_compteur.incrementer()
mon_compteur.decrementer()
mon_compteur.reset()


# Exercice 5
# Crée une classe Temperature avec un attribut `celsius`.
# Ajoute une méthode `to_fahrenheit()` → F = C × 9/5 + 32
class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius
    def to_fahrenheit(self):
        print(f"la temperature {self.celsius} en celsius donne {(self.celsius*(9/5))+32} en fahrenheit")


ma_temperature = Temperature(36)
ma_temperature.to_fahrenheit()
# Exercice 6
# Crée une classe Etudiant avec `nom`, `note`.
# Ajoute une méthode `mention()` qui retourne :
#   >= 16 → "Très bien" | >= 14 → "Bien" | >= 12 → "Assez bien" | sinon → "Passable"
class Etudiant:
    def __init__(self,nom,note):
        self.nom = nom
        self.note = note
    def mention(self):
        if self.note >=16:
            print("Tres bien")
        elif self.note >=14:
            print("Bien")
        elif self.note >=12:
            print("Assez bien")
        else:
            print("Passable")

etudiant = Etudiant("Joress",16.5)
etudiant.mention()
# Exercice 7
# Crée une classe BankAccount avec `solde = 0`.
# Ajoute `deposer(montant)`, `retirer(montant)` (vérifie que solde >= 0)
# et `afficher_solde()`.
class BankAccount:
    def __init__(self,solde =0):
        self.solde = solde
    def deposer(self,montant):
        self.solde += montant
        print("vous avez deposer:", montant)
        return montant
    def retirer(self,montant):
        if self.solde >= montant:
            self.solde -= montant
            print("vous avez retiré:", montant)
        else:
            print("Solde Insuffisant")
    def afficher_solde(self):
        print("Votre solde est ", self.solde)
    

myaccount = BankAccount()
myaccount.deposer(8000)
myaccount.retirer(40000)
myaccount.afficher_solde()

        




# Exercice 8
# Crée une classe Vecteur2D avec `x` et `y`.
# Ajoute une méthode `norme()` → √(x² + y²)
# et `afficher()` → "Vecteur(x, y)"
class Vecteur2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def norme(self):
        norme = (self.x**2 + self.y**2)**(0.5)
        print(f"la norme du vecteur est: {norme}")
    def afficher(self):
        print(f"Vecteur:({self.x},{self.y})")


mon_vecteur = Vecteur2D(4,-9)
mon_vecteur.norme()
mon_vecteur.afficher()


# Exercice 9
# Crée une classe Panier avec une liste `articles = []`.
# Ajoute `ajouter(article)`, `supprimer(article)` et `afficher()`.
class Panier:
    def __init__(self,articles=[]):
        self.articles = articles
    def ajouter(self,article):
        self.articles.append(article)
        print("vous avez ajouté: ",article)
    def supprimer(self,article):
        self.articles.remove(article)
        print("vous avez supprimé: ",article)
    def afficher(self):
        print("Votre liste est: ", self.articles)

monPanier = Panier(["banane","pomme","mangue","fraise"])
monPanier.ajouter("myrtille")
monPanier.supprimer("banane")
monPanier.afficher()
# Exercice 10
# Crée une classe MotDePasse avec `longueur`.
# Ajoute `generer()` qui retourne un mot de passe aléatoire
# de lettres minuscules. (hint: import random, import string)
import random
import string
class MotDePasse:
    def __init__(self,longueur):
        self.longueur = longueur
    def generer(self):
        mdp = ''.join(random.choices(string.ascii_lowercase, k=self.longueur))
        print("mot de passe généré est: ")
        for digit in mdp:
            print(digit,end="")
        

mymdp = MotDePasse(7)
mymdp.generer()


# ============================================================
# PARTIE 2 — HÉRITAGE (Exercices 11 à 20)
# ============================================================

# Exercice 11
# Crée une classe Forme avec une méthode `aire()` qui retourne 0.
# Crée CarreH qui hérite de Forme, avec `cote`, et surcharge `aire()`.
class Forme:
    def aire(self):
        return 0

class CarreH(Forme):
    def __init__(self,cote):
        self.cote = cote

    def aire(self):
        return self.cote * self.cote
    
    


# Exercice 12
# Reprends Animal (ex 1). Crée Chien et Chat qui héritent d'Animal.
# Chaque sous-classe surcharge `parler()` :
#   Chien → "Woof!" | Chat → "Miaou!"
class Chien(Animal):
    def parler(self):
        return f"woof!"

class Chat(Animal):
    def parler(self):
        return f"Miau!"
    
monchien = Chien("max")
print(monchien.parler())

monchat = Chat("max")
print(monchat.parler())

    


# Exercice 13
# Crée une classe Vehicule avec `marque` et `vitesse_max`.
# Crée Voiture et Moto qui héritent de Vehicule.
# Ajoute une méthode `description()` propre à chaque classe.
class Vehicule:
    def __init__(self,marque,vitesse_max):
        self.marque = marque
        self.vitesse_max = vitesse_max

class Voiture(Vehicule):
    def description(self):
        print(f"c'est une voiture de {self.marque} et sa vitesse max est: {self.vitesse_max}") 
    

class Moto(Vehicule):
    def description(self):
        print(f"c'est une Moto de {self.marque} et sa vitesse max est: {self.vitesse_max}") 

mavoiture = Voiture("toyota", 192)
mavoiture.description()
mamoto = Moto("yamaha", 200)
mamoto.description()


# Exercice 14
# Crée une classe Employe avec `nom` et `salaire`.
# Crée Manager qui hérite d'Employe et ajoute `equipe = []`.
# Ajoute `ajouter_membre(nom)` et `afficher_equipe()`.
class Employe:
    def __init__(self,nom,salaire):
        self.nom = nom
        self.salaire = salaire
    

class Manager(Employe):
    def __init__(self, nom, salaire,equipe = []):
        super().__init__(nom, salaire)
        self.equipe = equipe
    def ajouter_membre(self, nom):
        self.equipe.append(nom)
        print("le membre ajouté est:",nom)
    def afficher_equipe(self):
        print("nouvelle equipe:",self.equipe)
    

monManager = Manager(["jean","luc","bertrand"])
monManager.ajouter_membre("billy")
monManager.afficher_equipe()

# Exercice 15
# Crée une classe Shape3D avec volume() → 0.
# Crée Sphere (rayon) et Cube (cote) qui héritent de Shape3D.
# Sphere : V = (4/3)πr³ | Cube : V = côté³
class Shape3D:
    def __init__(self):
        pass
    def volume(self):
        return 0
    

class Sphere(Shape3D):
    def __init__(self,rayon):
        self.rayon = rayon
    def volume(self):
        print("le volume est ", (4/3)*math.pi*(self.rayon**3))
class Cube(Shape3D):
    def __init__(self,cote_cube):
        self.cote_cube = cote_cube
    def volume(self):
        print("le volume est :", self.cote_cube**3)

ma_sphere = Sphere(3)
ma_sphere.volume()


moncube = Cube(7)
moncube.volume()

# Exercice 16
# Utilise super() : Crée Personne avec `nom` et `age`.
# Crée Etudiant2 qui hérite de Personne et ajoute `universite`.
# Le __init__ d'Etudiant2 doit appeler super().__init__()
class Personne:
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age

class Etudiant2(Personne):
    def __init__(self, nom, age,univ):
        super().__init__(nom, age)
        self.univ = univ


# Exercice 17
# Crée une classe Instrument avec `jouer()` → "..."
# Crée Piano et Guitare qui héritent d'Instrument.
# Crée un orchestre = liste d'instruments et appelle jouer() sur chacun.
class Instrument:
    def jouer(self):
        return "..."

class Piano(Instrument):
    def jouer(self):
        return "Do ré mi"
    pass  # à compléter

class Guitare(Instrument):
    pass  # à compléter

orchestre = [Piano,Guitare]
myInstrument = Instrument
Instrument.jouer()


# Exercice 18
# Crée une classe Operateur avec `appliquer(a, b)` → 0.
# Crée Addition, Soustraction, Multiplication qui héritent d'Operateur
# et surchargent `appliquer()`.
class Operateur:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        pass
    def appliquer(self,a,b):
        return 0
    

class Addition(Operateur):
    def appliquer(self,a,b):
        return a + b
    

class Soustraction(Operateur):
    def appliquer(self):
        return self.a - self.b
    

class Multiplication(Operateur):
    def appliquer(self):
        return self.a * self.b

add = Addition(3,5)
print(add.appliquer())

# Exercice 19
# Crée une classe LogBase avec `log(message)` → affiche le message.
# Crée LogFichier qui hérite de LogBase et écrit aussi dans "log.txt".
class LogBase:
    def __init__(self,message):
        self.message = message
    def log(self):
        print(self.message)

class LogFichier(LogBase):
    def log(self):
        with open("log.txt","w") as datei:
            datei.write(self.message)

monfichier = LogFichier("bonjour")
monfichier.log()

# Exercice 20
# Crée une hiérarchie : Animal → Mammifere → Cheval.
# Chaque niveau ajoute un attribut et une méthode.
# Utilise super() à chaque niveau.
class Mammifere(Animal):
    def __init__(self,type):
        super().__init__(self.nom)
        self.type = type
    def savoir_type(self):
        print("je suis un",self.type)

class Cheval(Mammifere):
    def __init__(self,nom_animal):
        self.nom_animal = nom_animal
        super.__init__(self.type)
    def savoir_type(self):
        print("il s'appelle:", self.nom_animal)


    


# ============================================================
# PARTIE 3 — MÉTHODES SPÉCIALES (Exercices 21 à 30)
# ============================================================

# Exercice 21
# Crée une classe Point avec `x` et `y`.
# Implémente __str__ → "Point(x, y)"
# et __repr__ → "Point(x=x, y=y)"
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f"Point({self.x},{self.y})")

    def __repr__(self):
        print(f"Point(x={self.x},y={self.y})")
        


# Exercice 22
# Reprends Point. Implémente __add__ pour additionner deux points :
# Point(1,2) + Point(3,4) → Point(4,6)
class Point2(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    def __add__(self,other):
        return Point2(self.x + other.x, self.y + other.y) 

mon_point = Point2(1,2)
mon_point1 = Point2(1,2)

mon_point.__add__(mon_point1)
# Exercice 23
# Crée une classe Fraction avec `num` et `den`.
# Implémente __str__, __add__ et __mul__ pour les fractions.
# Simplifie avec math.gcd.
class Fraction:
    def __init__(self,num,den):
        self.num = num
        self.den = den
    
    def __str__(self):
        print(f"Ma fraction est {self.num}/{self.den}")
    
    def __add__(self,other):
        if self.den == other.den:
            nouveau_numerateur = self.num + other.num
            nouveau_denominateur = self.den
        else:
            nouveau_numerateur = self.num*other.den + self.den*other.num
            nouveau_denominateur = self.den * other.den

        print(f"la somme des deux fraction est : {nouveau_numerateur}/{nouveau_denominateur}")
    def __mul__(self,other):
        nouveau_numerateur = self.num * other.num
        nouveau_denominateur = self.den * other.den

        print(f"le produit des deux fraction est : {nouveau_numerateur}/{nouveau_denominateur}")
    

fraction1 = Fraction(1,2)
fraction2 = Fraction(2,7)


fraction1.__add__(fraction2)
fraction1.__mul__(fraction2)
fraction1.__str__()
# Exercice 24
# Crée une classe Pile (stack) avec `elements = []`.
# Implémente __len__, `push(item)`, `pop()` et __str__.
class Pile:

    def __init__(self,elements = []):
        self.elements = elements
    
    def __len__(self):
        print("la longueur des elements est:", len(self.elements))
    
    def push(self, item):
        self.elements.append(item)

    def pop(self):
        self.elements.pop()

    def __str__(self):
        print("la liste actuelisée est:", self.elements)
    

maPile = Pile(["Bonjour","mon","petit"])
maPile.push("Jason")
maPile.__str__()

# Exercice 25
# Crée une classe MatriceSimple avec un tableau numpy 2D.
# Implémente __add__ et __mul__ (multiplication matricielle).
# et __str__ pour afficher proprement.
class MatriceSimple:
    def __init__(self, A):
        self.A = A

''' def __add__(self,other):
            c = np.add(self.A, np.array(other.A))
            print("la matrice est",c)'''


matrice_1 = MatriceSimple(np.array([[1,3],[4,5]]))
matrice_2 = [[1,3],[4,5]]


#matrice_1.__add__(matrice_2)


# Exercice 26
# Crée une classe Intervalle avec `debut` et `fin`.
# Implémente __contains__ pour tester si un nombre est dans l'intervalle :
# 5 in Intervalle(1, 10) → True
class Intervalle:
    def __init__(self,debut,fin):
        self.debut = debut
        self.fin = fin
    
    def __contains__(self,nombre):
        if (nombre > self.debut & nombre < self.fin):
            print (True)


mon_intervalle = Intervalle(4,15)
mon_intervalle.__contains__(8)
# Exercice 27
# Crée une classe Chronometre avec `temps = 0`.
# Implémente __enter__ et __exit__ pour l'utiliser avec `with` :
# with Chronometre() as c: ...
import time
class Chronometre:
    def __enter__(self):
        self.debut = time.time()
        return self
    def __exit__(self, *args):
        print(f"Durée : {time.time() - self.debut:.4f}s")
    pass  # à compléter


# Exercice 28
# Crée une classe Config avec un dictionnaire interne.
# Implémente __getitem__, __setitem__ pour accéder comme un dict :
# config["lr"] = 0.01 | config["lr"] → 0.01
class Config:
    def __init__(self,dict ={}):
        self.dict = dict
    def __getitem__(self, key):
        print(f"config[{key}] = {self.dict[key]}")
    def __setitem__(self, key, value):
        print(f"config[{key}] -> {value}")
        

Maconfig = Config({"Bonjour": 23, "bb":56, "cameleon":67})
Maconfig.__getitem__("bb")
Maconfig.__setitem__("Bonjour",23)


# Exercice 29
# Crée une classe Sequence avec une liste.
# Implémente __iter__ et __next__ pour la rendre itérable :
# for item in Sequence([1,2,3]): print(item)
class Sequence:
    def __init__(self, liste):
        self.liste = liste
        self.index = 0
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index >= len(self.liste):
            raise StopIteration
        val = self.liste[self.index]
        self.index += 1
        return val



Masequence = Sequence([1,3,4,5,78,9])
Masequence.__iter__()




# Exercice 30
# Crée une classe Singleton — une classe dont on ne peut créer
# qu'une seule instance. (hint: surcharge __new__)
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# ============================================================
# PARTIE 4 — MODULES & ORGANISATION (Exercices 31 à 40)
# ============================================================

# Exercice 31
# Importe le module `collections` et utilise `Counter`
# pour compter les occurrences de chaque lettre dans "deep learning".
# Affiche les 3 lettres les plus fréquentes.

from collections import Counter

c = Counter("deep learning")
print(c)

frequente = c.most_common()
print(frequente)

# Exercice 32
# Utilise `itertools.combinations` pour générer toutes les paires
# possibles depuis la liste ["A", "B", "C", "D"].

from itertools import combinations

possible_liste = (list(combinations(["A", "B", "C", "D"], 2)))

print(possible_liste)


# Exercice 33
# Utilise `functools.reduce` pour calculer le produit de tous les
# éléments de [1, 2, 3, 4, 5] sans boucle for.


from functools import reduce

sans_boucle = reduce(lambda x,y: x*y,[1, 2, 3, 4, 5])

print(sans_boucle)
# Exercice 34
# Utilise `datetime` pour calculer combien de jours
# il reste jusqu'au 31 décembre 2025.from datetime
from datetime import date

date_ = date(2025,12,31)

date_today = date.today()

reste = date_ - date_today
print(reste)
# Exercice 35
# Crée un décorateur `timer` qui mesure le temps d'exécution
# d'une fonction et l'affiche.




# j'ai genere malheuresement avec l'IA
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Enregistrer l'heure de début
        debut = time.perf_counter()
        
        # 2. Exécuter la fonction d'origine
        resultat = func(*args, **kwargs)
        
        # 3. Enregistrer l'heure de fin
        fin = time.perf_counter()
        
        # 4. Calculer et afficher la durée
        duree = fin - debut
        print(f"Temps d'exécution de '{func.__name__}': {duree:.4f} secondes")
        
        # 5. Retourner le résultat de la fonction
        return resultat
    
    return wrapper




# Exercice 36
# Crée un décorateur `logger` qui affiche le nom de la fonction
# et ses arguments à chaque appel.
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Ma fonction est: '{func.__name__}': et ses arguments sont:{args,kwargs} ")

    return wrapper


# Exercice 37
# Crée une fonction `memoize` qui met en cache les résultats
# d'une fonction. Teste avec fibonacci.
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

# Exercice 38
# Utilise `dataclasses` pour créer une dataclass `Neurone`
# avec les attributs : poids (list), biais (float), activation (str).
from dataclasses import dataclass

@dataclass
class Neurone:
    poids: list
    biais: float
    activation: str

# Exemple d'utilisation :
mon_neurone = Neurone(poids=[0.5, -0.2, 0.1], biais=0.01, activation="ReLU")

print(mon_neurone)

# à compléter


# Exercice 39
# Utilise `typing` pour ajouter des annotations de type à une fonction
# `normaliser(data: list[float]) -> list[float]`
# qui normalise une liste entre 0 et 1.
def normaliser(data: list[float]) -> list[float]:
    min_v, max_v = min(data), max(data)
    return [(x - min_v) / (max_v - min_v) for x in data]

    pass  # à compléter + ajouter les annotations de type


# Exercice 40
# Crée une classe abstraite `Modele` avec les méthodes abstraites
# `entrainer()` et `predire()`. Crée `ModeleLineaire` qui l'implémente.
'''class Modele("ABC"):
    @ABC
    def entrainer(self): pass
    @ABC
    def predire(self): pass

class ModeleLineaire(Modele):
    def entrainer(self): print("Entraînement...")
    def predire(self): print("Prédiction...")'''


# ============================================================
# PARTIE 5 — POO APPLIQUÉE AU DEEP LEARNING (Exercices 41 à 50)
# ============================================================

# Exercice 41
# Crée une classe Neurone avec `poids` (array numpy) et `biais`.
# Ajoute `activer(x)` → retourne np.dot(poids, x) + biais
class Neurone:
    def __init__(self, poids,biais):
        self.poids = poids
        self.biais = biais
    
    def activer(self,x):
        return np.dot(self.poids, x) + self.biais

mon_neurone = Neurone(np.array([1,3,4,6]), 0.09)
mon_neurone.activer(np.array([1,3,4,90]))

# Exercice 42
# Crée une classe ActivationReLU
# Ajoute `forward(x)` → max(0, x) appliqué élément par élément sur un array.
class ActivationReLU:
    def forward(self,x):
        return np.maximum(0, x)
    
monactivation = ActivationReLU
monactivation.forward(np.array([1,-3,4,0]))

# Exercice 43
# Crée une classe ActivationSigmoid.
# Ajoute `forward(x)` → 1 / (1 + e^(-x)) sur un array numpy.
class ActivationSigmoid:
    def forward(x):
        for i in x:
            print(1 / (1 + (math.exp(-i))))


monAS = ActivationSigmoid
monAS.forward(np.array([1,-3,4,0]))


# Exercice 44
# Crée une classe CoucheDense avec `n_entrees` et `n_sorties`.
# Initialise `poids` (matrice numpy aléatoire) et `biais` (vecteur de zéros).
# Ajoute `forward(x)` → np.dot(x, poids) + biais

#j'ai generé
class CoucheDense:
    def __init__(self, n_entrees, n_sorties):
        self.poids = np.random.randn(n_entrees, n_sorties) * 0.01
        self.biais = np.zeros((1, n_sorties))

    def forward(self, x):
        # x est le vecteur ou la matrice de données en entrée
        self.entree = x
        self.sortie = np.dot(x, self.poids) + self.biais
        return self.sortie


# Exercice 45
# Crée une classe LossMSE.
# Ajoute `calculer(y_pred, y_true)` → moyenne de (y_pred - y_true)²
class LossMSE:
    def calculer(y_pred, y_true):

        return np.mean((y_pred-y_true)**2)

meinMSE = LossMSE()
# Exercice 46
# Crée une classe Normaliseur avec `mean` et `std`.
# Ajoute `fit(data)` qui calcule mean et std depuis data.
# Ajoute `transform(data)` → (data - mean) / std
class Normaliseur:
    def fit(self,data):
        self.mean = np.mean(data)
        self.std = np.std(data)
        
    def transform(self,data):
        return (data - self.mean) / self.std
        



# Exercice 47
# Crée une classe Dataset avec `X` et `y`.
# Ajoute `__len__` → nombre d'exemples
# Ajoute `__getitem__(i)` → retourne (X[i], y[i])
# Ajoute `batch(taille)` → retourne des sous-groupes de taille fixe
class Dataset:
    def __init__(self,X,y):
        self.x = X
        self.y = y

    def __len__(self):
        return len([self.x])

    def __getitem__(self, i):
            return (self.x[i], self.y[i])
    
    def batch(taille):
        pass

    

# Exercice 48
# Crée une classe GradientDescent avec `lr` (learning rate).
# Ajoute `step(poids, gradient)` → poids - lr × gradient
class GradientDescent:
    def __init__(self,lr):
        self.lr = lr
    def step(self,poids, grandient):
        return poids - (self.lr *grandient)    # à compléter


# Exercice 49
# Crée une classe Pipeline qui enchaîne des transformations.
# Ajoute `ajouter_etape(etape)` et `executer(data)` qui applique
# chaque étape dans l'ordre.
# Teste avec Normaliseur + une fonction lambda.
class Pipeline:

    pass  # à compléter


# Exercice 50 — Boss Final 🎯
# Crée un mini réseau de neurones avec :
#   - Une classe ReseauNeuronal avec une liste de couches
#   - `ajouter_couche(couche)` pour empiler des CoucheDense
#   - `forward(x)` qui fait passer x à travers toutes les couches
#   - `predire(x)` qui applique forward puis ActivationSigmoid
# Teste avec :
#   X = np.array([1.0, 2.0, 3.0])
#   reseau = ReseauNeuronal()
#   reseau.ajouter_couche(CoucheDense(3, 4))
#   reseau.ajouter_couche(CoucheDense(4, 1))
#   print(reseau.predire(X))
class ReseauNeuronal:
    def __init__(self):
        self.couches = []
    
    def ajouter_couche(self,couche):
        self.couches.append(couche)

    def forward(self,x):
        for couche in self.couches:
            x = couche.forward(x)
        return x
        

    def predire(self,x):
        x = self.forward(x)
        return ActivationSigmoid.forward(x)



# ============================================================
# TESTS — Décommente pour tester chaque exercice
# ============================================================

# --- Partie 1 ---
a = Animal("Lion") ; 
a.parler()
r = Rectangle(3, 4) ; print(r.aire())
c = Cercle(5) ; print(c.aire(), c.perimetre())
# cpt = Compteur() ; cpt.incrementer() ; cpt.incrementer() ; print(cpt.valeur)
# t = Temperature(100) ; print(t.to_fahrenheit())
# e = Etudiant("Alice", 15) ; print(e.mention())
# b = BankAccount() ; b.deposer(100) ; b.retirer(30) ; b.afficher_solde()
# v = Vecteur2D(3, 4) ; print(v.norme()) ; v.afficher()
# p = Panier() ; p.ajouter("pomme") ; p.ajouter("pain") ; p.afficher()
# mp = MotDePasse(12) ; print(mp.generer())

# --- Partie 2 ---
# carre = CarreH(5) ; print(carre.aire())
# chien = Chien("Rex") ; chien.parler()
# chat = Chat("Mimi") ; chat.parler()
# v = Voiture("Toyota", 180) ; v.description()
# m = Manager("Alice", 5000) ; m.ajouter_membre("Bob") ; m.afficher_equipe()
# s = Sphere(3) ; print(s.volume())
# e2 = Etudiant2("Bob", 20, "MIT") ; print(e2.nom, e2.universite)
# orchestre = [Piano(), Guitare()] ; [i.jouer() for i in orchestre]
# ops = [Addition(), Soustraction(), Multiplication()]
# [print(op.appliquer(10, 3)) for op in ops]
# cheval = Cheval() ; cheval.galoper()

# --- Partie 3 ---
# p = Point(1, 2) ; print(p)
# p1, p2 = Point2(1,2), Point2(3,4) ; print(p1 + p2)
# f = Fraction(1,2) ; g = Fraction(1,3) ; print(f + g)
# pile = Pile() ; pile.push(1) ; pile.push(2) ; print(pile.pop())
# m = MatriceSimple(np.eye(3)) ; print(m)
# print(5 in Intervalle(1, 10))
# with Chronometre() as c: time.sleep(0.1)
# cfg = Config() ; cfg["lr"] = 0.01 ; print(cfg["lr"])
# for x in Sequence([10,20,30]): print(x)
# s1, s2 = Singleton(), Singleton() ; print(s1 is s2)

# --- Partie 4 ---
# (décommente les lignes des exercices 31-40 directement)

# --- Partie 5 ---
# n = Neurone(np.array([0.5, -0.3]), 0.1)
# print(n.activer(np.array([1.0, 2.0])))
# relu = ActivationReLU() ; print(relu.forward(np.array([-1, 0, 2])))
# sig = ActivationSigmoid() ; print(sig.forward(np.array([0, 1, -1])))
# couche = CoucheDense(3, 2) ; print(couche.forward(np.array([1,2,3])))
# loss = LossMSE() ; print(loss.calculer(np.array([1,2]), np.array([1.5,1.8])))
# norm = Normaliseur() ; norm.fit(np.array([1,2,3,4,5]))
# print(norm.transform(np.array([1,2,3,4,5])))
# ds = Dataset(np.eye(3), np.array([0,1,0])) ; print(ds[1])
# gd = GradientDescent(lr=0.01)
# print(gd.step(np.array([1.0, 2.0]), np.array([0.1, 0.2])))
# X = np.array([1.0, 2.0, 3.0])
# reseau = ReseauNeuronal()
# reseau.ajouter_couche(CoucheDense(3, 4))
# reseau.ajouter_couche(CoucheDense(4, 1))
# print(reseau.predire(X))
