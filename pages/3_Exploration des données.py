import streamlit as st 

import pandas as pd 

import numpy as np 

import matplotlib.pyplot as plt 

@st.cache_data  # 👈 Add the caching decorator
def load_data():
    
    archivos = [f'parte_{i+1}.csv' for i in range(5)]
    dfs = []

    for archivo in archivos:  
        df_part = pd.read_csv(archivo)
        dfs.append(df_part)

    df_mit = pd.concat(dfs, ignore_index=True)

    return df_mit

df_mit = load_data()

@st.cache_data  # 👈 Add the caching decorator
def load_data2():
    df_normal = pd.read_csv("ptbdb_normal.csv", header = None) 
    df_abnormal = pd.read_csv("ptbdb_abnormal.csv", header = None) 

    df_ptb = pd.concat([df_normal, df_abnormal], ignore_index=True)
    
    return df_ptb

df_ptb = load_data2()

st.markdown('### Exploration des données')

texte = """
Un premier prétraitement des signaux ECG a été réalisé permettant l'extraction des battements. Les étapes sont les suivantes:

1. Séparer le signal ECG continu en fenêtres de 10 secondes et sélectionner une fenêtre de 10 secondes à partir d'un signal ECG.
2. Normaliser les valeurs d'amplitude pour les amener à une plage entre zéro et un.
3. Trouver l'ensemble de tous les maxima locaux en se basant sur les passages par zéro de la première dérivée.
4. Trouver l'ensemble des candidats pour les pics R de l'ECG en appliquant un seuil de 0,9 sur la valeur normalisée des maxima locaux.
5. Trouver la médiane des intervalles de temps R-R comme période nominale des battements cardiaques pour cette fenêtre (T).
6. Pour chaque pic R, sélectionner une partie du signal avec une longueur égale à 1,2T.
7. Compléter chaque partie sélectionnée avec des zéros pour que sa longueur soit égale à une longueur fixe prédéfinie.
"""

st.write(texte)  

option = st.selectbox('Choisissez le DataFrame à afficher', ('MITBIH', 'PTBDB')) 


def check_missing_values(df_mit): 

  if df_mit.isnull().values.any(): 

    return "Oui" 

  else: 

    return "Non" 

def check_missing_values(df_ptb): 

  if df_ptb.isnull().values.any(): 

    return "Oui" 

  else: 

    return "Non" 



if option == 'MITBIH':
  st.write("Le jeu de données MITBIH est téléchargeable sur le [lien Kaggle](https://www.kaggle.com/datasets/shayanfazeli/heartbeat), il se présente sous 2 fichiers csv, un fichier Train et un fichier Test")
  


  st.header('MITBIH')
   
  
  st.dataframe(df_mit.head()) 

  st.write(f"Shape: {df_mit.shape}") 

  st.write(f"Valeurs manquantes: {check_missing_values(df_mit)}") 

else: 
  st.write("Le jeu de données PTBDB est téléchargeable sur le [lien Kaggle](https://www.kaggle.com/datasets/shayanfazeli/heartbeat), il se présente sous 2 fichiers csv fichier Normal et fichier Abnormal")
  st.header('PTBDB')
  st.dataframe(df_ptb.head()) 

  st.write(f"Shape: {df_ptb.shape}") 

  st.write(f"Valeurs manquantes: {check_missing_values(df_ptb)}") 

  