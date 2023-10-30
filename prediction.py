# En-tete ---------------------------------------------------------------------
# # Author: Gabaut Garance 
# # Date: septembre - octobre 2022
# # tite : Exploitation de notre jeu de données precedemment recolté

#packages ---------------------------------------------------------------------

import pandas as pd # permet d importer, de lire, de manipuler notre jeu de données
from sklearn.linear_model import LinearRegression # permet de faire la regresison linéaire
import matplotlib.pyplot as plt  # permet la visualisation des resultats
import numpy as np
#jeu de données ---------------------------------------------------------------
dataset = pd.read_csv('08Nov.csv' , sep=";") 

#on choisit l'entreprise pour laquelle on souhaite faire l'étude
NameCompagny="VINCI"
for i in range(len(dataset.columns.values)):
    if dataset.columns.values[i] == NameCompagny:
        NumbCompagny=i
        
#on extrait les colonnes de notre entreprise dans la table principale et celle avec les heures   
dataEchantillon=dataset.iloc[:, [0,NumbCompagny]]



# 1er methode de prediction----------------------------------------------------
# Regression Linéaire, avec le packagessklearn---------------------------------

TotEnt=1400 #nombre de valeurs d'entrainements
TotVal=1670 #nombre de valeurs totales selectionnées
X=dataEchantillon.iloc[0:TotVal, 1:2]
Y=dataEchantillon.iloc[1:TotVal+1,1:2]

#X et Y d'entrainements
X_train = X.iloc[0:TotEnt,:].values 
Y_train = Y.iloc[0:TotEnt,:].values

#X et Y pour verifier si notre prediction est bonne
X_test = X.iloc[TotEnt:TotVal,:].values 
Y_test = Y.iloc[TotEnt:TotVal,:].values
 
# on entraine notre régression
reg = LinearRegression()
reg.fit(X_train,Y_train)
Y_pred = reg.predict(X_test)

x=np.arange(TotEnt, TotVal)

# Representation des resultats
plt.figure()
plt.plot(x,Y_pred, color="green", label="Valeurs estimées par le modèle")
plt.plot(x,Y_test , color="red", label="valeurs récoltées")
plt.legend(loc = 'upper right')
plt.title("Répresentation de nos valeurs prédites par le modèle et les veritables valeurs")


#representation de la difference absolue
plt.figure()
diff=abs(Y_pred-Y_test)
mean_diff=np.mean(diff) 
A=np.arange(1,len(diff)+1)
vect_mean=np.ones(len(diff))*mean_diff
plt.plot(diff, label="difference absolue entre notre modèle et la réalité", color="darkblue")
plt.plot(vect_mean, label="Moyenne des differnces absolue", color="red")
plt.title("Representation de la difference absolue entre les valeurs estimées et les veritables valeurs")
plt.legend(loc = 'upper left')





#2eme methode de prediction----------------------------------------------------
# La moyenne mobile -----------------------------------------------------------

MM30=X.rolling(30).mean() #permet de faire une moyenne mobile sur 30 valeurs
plt.figure()
plt.plot(X, color="green", label="Représentation des valeurs récoltés")
plt.plot(MM30, color="red",label="Moyenne mobile sur 30 valeurs")
plt.legend()
plt.title("Representation de la moyenne moyenne")


# Superposition de deux moyennes mobiles
MM20=X.rolling(20).mean() 
MM50=X.rolling(50).mean() 
plt.figure()
plt.plot(X, color="green", label="Représentation des valeurs récoltés")
plt.plot(MM20, color="red",label="Moyenne mobile sur 20 valeurs")
plt.plot(MM50, color="blue",label="Moyenne mobile sur 50 valeurs")
plt.legend()
plt.title("Representation de la moyenne moyenne")


# Zoom sur une portion de la representation
MM20e=MM20[50:250]
MM50e=MM50[50:250]
Xe=X[50:250]
plt.figure()
plt.plot(Xe, color="green", label="Représentation des valeurs récoltés")
plt.plot(MM20e, color="red",label="Moyenne mobile sur 20 valeurs")
plt.plot(MM50e, color="blue",label="Moyenne mobile sur 50 valeurs")
plt.legend()
plt.title("Representation de la moyenne moyenne")


# Zoom sur une portion de la representation
MM20e=MM20[500:750]
MM50e=MM50[500:750]
Xe=X[500:750]
plt.figure()
plt.plot(Xe, color="green", label="Représentation des valeurs récoltés")
plt.plot(MM20e, color="red",label="Moyenne mobile sur 20 valeurs")
plt.plot(MM50e, color="blue",label="Moyenne mobile sur 50 valeurs")
plt.legend()
plt.title("Representation de la moyenne moyenne")


