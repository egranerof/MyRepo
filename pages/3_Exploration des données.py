import streamlit as st 

import pandas as pd 

import numpy as np 

import matplotlib.pyplot as plt 

 

 

df_train = pd.read_csv("mitbih_train.csv", header = None) 

df_test = pd.read_csv("mitbih_test.csv", header = None) 

df_mit = pd.concat([df_train, df_test], ignore_index=True)  


 

df_normal = pd.read_csv("ptbdb_normal.csv", header = None) 

df_abnormal = pd.read_csv("ptbdb_abnormal.csv", header = None) 

df_ptb = pd.concat([df_normal, df_abnormal], ignore_index=True)  

 

st.write("### Exploration des données")      

option = st.selectbox('Choisissez le DataFrame à afficher', ('df_mit', 'df_ptb')) 

 

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

if option == 'df_mit': 

  st.header('df_mit') 
  
  st.dataframe(df_mit.head()) 

  st.write(f"Shape: {df_mit.shape}") 

  st.write(f"Valeurs manquantes: {check_missing_values(df_mit)}") 

else: 

  st.header('df_ptb')
  st.dataframe(df_ptb.head()) 

  st.write(f"Shape: {df_ptb.shape}") 

  st.write(f"Valeurs manquantes: {check_missing_values(df_ptb)}") 

  