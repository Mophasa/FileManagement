# 1) Importer la bibliothèque NumPy
import pandas as pd
import numpy as np
import ssl

# Ignorer la vérification SSL
ssl._create_default_https_context = ssl._create_unverified_context

# 2) Ouvrir le fichier CSV à partir de l'URL
url = 'https://drive.google.com/uc?id=16RjrvW2NG8Rt0AbblsflA8iJdxSXfl5C'
data = pd.read_csv(url)

# 3) Effectuer une analyse statistique de base sur les montants des prêts

# Les montants des prêts se trouvent dans la colonne 9 (index 8)
montants_pret = data.iloc[:, 8]

# Calculer la moyenne et l'écart-type en ignorant les NaN
moyenne = np.nanmean(montants_pret)
print(f'Moyenne des montants de prêt : {moyenne}')

# Calculer la mediane
mediane = np.nanmedian(montants_pret)
print(f'Médiane des montants de prêt : {mediane}')

# Calculer l'ecart type
ecart_type = np.nanstd(montants_pret)
print(f'Écart-type des montants de prêt : {ecart_type}')