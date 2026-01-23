#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import os


# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r", encoding='utf-8') as fichier:
    contenu = pd.read_csv(fichier)

# Mettre dans un commentaire le numéro de la question
# Question 6 : affichage de la variable contenu dans le terminal
print(contenu)

# Question 7 : Calcul du nombre de lignes et de colonnes
col_lignes = len(contenu) #création d'une variable qui contient le nombre de lignes et de colonnes
print(col_lignes) #Affichage de la variable 

# Question 8 : 
# Les données fournies concernent les résultats du premier tour des éléctions présidentielles
# en fonction des départements et des candidats. 
# Affichage du type/de la classe des variables (on crée une liste qui pour chaque variable renvoie son type) : 
types_colonnes = [(col, str(contenu[col].dtype)) for col in contenu.columns]
for nom, type_ in types_colonnes:
    print(f"{nom} → {type_}")
    
# Nous obtenons une liste qui pour chaque variable nous indique son type pandas (que nous devons retranscrire en type python pour qu'ils soient
# interprétables.
# Nous avons des variables de deux types object et float64. 
# La correspondance python de float64 est float : ce sont des variables quantitatives continues. Ainsi les variables numériques tels que 
# le nombre de votants, le nombre de voix par candidats etc sont en float. 
# La correspondance python de object est str (string) : ce sont les variables qui prennent la forme de chaînes de caractères. Les variables descriptives
# telles que le département, le code de département, le nom des candidats etc.. sont en str. 

# Question 9 : affichage du nom des colonnes
print(contenu.head())

# Question 10 : 
print(contenu["Inscrits"].head())

# initialisation de la liste qui stockera nos valeurs. 
sum_col = []

# On fait une boucle qui vérifie chaque colonne du dataset une par une :
# Si la variable est numérique on calcule la somme de cette variable pour tous les départements (on obtient une somme au niveau
# national), que l'on stocke dans la liste préalablement initialisée.
# Si la variable n'est pas numérique on passe à la prochaine colonne. 

for col in contenu.columns:
    if contenu[col].dtype in ["int64", "float64"]: 
        total = contenu[col].sum()
        sum_col.append((col, total)) 
        

for nom, total in sum_col:
    print(f"{nom} : {total}")
    
    

# Question 11 : 
os.makedirs("./images", exist_ok=True)

grouped = contenu.groupby("Libellé du département")[["Inscrits", "Votants"]].sum().reset_index()

for i, row in grouped.iterrows():
    departement = row["Libellé du département"]
    inscrits = row["Inscrits"]
    votants = row["Votants"]

    plt.figure()
    plt.bar(["Inscrits", "Votants"], [inscrits, votants], color=["skyblue", "lightgreen"])
    plt.title(f"{departement} — Inscrits vs Votants")
    plt.ylabel("Nombre de personnes")

    filename = f"./images/{departement.replace('/', '_').replace(' ', '_')}.png"
    plt.savefig(filename, format="png")
    plt.close()  


