import streamlit as st 

import pandas as pd 

import numpy as np 

import matplotlib.pyplot as plt 



image_url = "data:image/jpeg;base64,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EAREQBERAEREAREQEiHiu3SHQLhw8V2qQ6BAb6sAxSD9R33K5YNgNXmrs5wzDKSWCOelxmaXaqC8MDGySbQ8wE3tJcafeqfUWLPQvpXZJIXZcxCI8YcYqABzs6CB380BUO1CaOLGsDw6I/BYXg9PGB0c9ztLeDWqsUlbs2BKlZ+qzWZuzDJe7YahlI0dPJo2QkesFVxshHNAWCrfHUtbILb1gsD84dCua95AJUcVDupWt8xdzUUqlJ7N+nOsqrcP9jzK65JWpZJWFLrRot7e2EREMBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAbojYhdikPBcWM2K6dM8CyA6E7vMV/7IZmiizPE42ENbTzOJ5B8bxf8Aur5zLIC3jyXRyxmemy7S5ygljndPitC2KhMQaWsna2ZgMhJFh59+fBAVjEKk1ldiNYTc1VXUVJP/AMsjn/ioqFEAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQHppspEUpFlFWQUBPdPcHVRZHXJWvaK83JQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQH/2Q=="  # Remplacez par l'URL de votre image ou le chemin de l'image

# Titre personnalisé avec une image à côté
title_with_image = f"""
<div style="display: flex; align-items: center; background-color: lightblue; padding: 10px;">
  <img src="{image_url}" alt="Logo" style="width:70px; height:70px; margin-right:15px;">
  <h1 style="color: black; font-size: 2em;">Classement des battements cardiaques</h1>
</div>
"""

# Afficher le titre personnalisé avec l'image
st.markdown(title_with_image, unsafe_allow_html=True)



st.header("• Introduction") 

st.subheader("Contexte du projet")
 

texte = """
Dans notre projet, on s’intéresse à l’activité électrique du cœur, responsable du rythme cardiaque (contraction: systole et relaxation: diastole). Cette activité est mesurée grâce à un appareil nommé électrocardiogramme(ECG). Il permet d’enregistrer une succession de séquences de l’activité électrique du cœur, représentée par des ondes : 

- **P** : l’activation des oreillettes
- **Complexe QRS** : correspond à la contraction des ventricules
- **Onde T** : correspond à la repolarisation des ventricules (retour au repos)

Lorsque la formation ou la conduction de l’excitation électrique sont perturbées, on parle alors d’arythmie (ou trouble du rythme).

Ces perturbations sont alors visibles sur les tracés ECG et permettent donc le diagnostic de certaines maladies cardiovasculaires : les arythmies cardiaques, les infarctus du myocarde...
"""
st.write(texte)
choix = ['OIP.jpg', 'cvs_ecg_reading_fr.gif'] 

option = st.selectbox('Choix image', choix) 

st.image (option)

texte = """
Cependant, le diagnostic des arythmies est très complexe car chez certains patients, les symptômes peuvent se présenter de façon sporadique, tandis que d’autres peuvent être asymptomatiques.

Ces dernières années, plusieurs applications ont vu le jour, par exemple dans les montres connectées, les holters implantables, etc. Ces outils représentent une aide précieuse dans le diagnostic de ces pathologies qui peuvent être très dangereuses.
"""
st.write(texte)

show_image = st.checkbox('Afficher un example holter implantable')

# Condition pour afficher l'image en fonction de la case à cocher
if show_image:
    
    st.image("RMS_476_1192_fig01_i1200.jpg")

st.subheader("Problématique du projet")

texte = """
Grâce aux différences des caractéristiques des signaux cardiaques observés sur les tracés d’ECG entre les différentes arythmies, notre objectif est de développer un modèle capable de capter ces caractéristiques et ainsi pouvoir classifier les différents battements dans les classes correspondantes.

Pour ce faire, nous avons eu à notre disposition deux bases de données très connues : MITBIH et PTBDB.
"""

st.write(texte)