import streamlit as st 

import pandas as pd 

import numpy as np 

import matplotlib.pyplot as plt 



image_url = "https://github.com/egranerof/MyRepo/blob/main/images/heart.jpg?raw=true"  # Remplacez par l'URL de votre image ou le chemin de l'image

# Titre personnalisé avec une image à côté
title_with_image = f"""
<div style="display: flex; align-items: center; background-color: lightblue; padding: 10px;">
  <img src="{image_url}" alt="Logo" style="width:70px; height:70px; margin-right:15px;">
  <h1 style="color: black; font-size: 2em;">Classification des battements cardiaques</h1>
</div>
"""

# Afficher le titre personnalisé avec l'image
st.markdown(title_with_image, unsafe_allow_html=True)



st.header("Introduction") 

st.subheader("Contexte du projet")
 

texte = """
Dans notre projet, on s’intéresse à l’activité électrique du cœur, responsable du rythme cardiaque (contraction: systole et relaxation: diastole). Cette activité est mesurée grâce à un appareil nommé électrocardiogramme (ECG). Il permet d’enregistrer une succession de séquences de l’activité électrique du cœur, représentée par des ondes : 

- **P** : l’activation des oreillettes
- **Complexe QRS** : correspond à la contraction des ventricules
- **Onde T** : correspond à la repolarisation des ventricules (retour au repos)

Lorsque la formation ou la conduction de l’excitation électrique sont perturbées, on parle alors d’arythmie (ou trouble du rythme).

Ces perturbations sont alors visibles sur les tracés ECG et permettent donc le diagnostic de certaines maladies cardiovasculaires : les arythmies cardiaques, les infarctus du myocarde...
"""
st.write(texte)
choix = ['Examen.jpg', 'LectureECG.gif'] 

option = st.selectbox('Choix image', choix) 

st.image(option)

st.markdown(" ")
st.markdown(" ")


texte = """
Cependant, le diagnostic des arythmies est très complexe car  certains patients, peuvent présenter des symptômes de façon sporadique, tandis que d’autres peuvent être asymptomatiques.

Ces dernières années, plusieurs applications ont vu le jour, par exemple dans les montres connectées, les holters implantables, etc. Ces outils représentent une aide précieuse dans le diagnostic de ces pathologies qui peuvent être très dangereuses.
"""
st.write(texte)

show_image = st.checkbox('Afficher un example holter implantable')

# Condition pour afficher l'image en fonction de la case à cocher
if show_image:
    
    st.image("images\RMS_476_1192_fig01_i1200.jpg")

st.markdown(" ")
st.subheader("Problématique du projet")

texte = """
Grâce aux différences des caractéristiques des signaux cardiaques observés sur les tracés d’ECG entre les différentes arythmies, notre objectif est de développer un modèle capable de capter ces caractéristiques et ainsi pouvoir classifier les différents battements dans les classes correspondantes.

Pour ce faire, nous avons eu à notre disposition deux bases de données très préstigieuses : 
 - MITBIH
 - PTBDB
"""

st.write(texte)


html_text = """
<div class="custom-html-container" style="position: fixed; bottom: 10px; width: 15%; border: 2px solid blue; padding: 10px; border-radius: 5px;">
    <p style="font-size: 16px; text-align: center;"><strong>Projet DS</strong></p>
    <p style="font-size: 14px; text-align: center;">Promotion Avril 2024</p>
    <p style="font-size: 14px;">
        <a href="https://linkedin.com/in/soraya-merbah/" target="_blank">Soraya MERBAH</a>
    </p>
    <p style="font-size: 14px;">
        <a href="https://linkedin.com/in/emanuelgf/" target="_blank">Emanuel GRANERO-FERNANDEZ</a>
    </p>
</div>
"""

# Afficher le texte encadré dans la barre latérale
st.sidebar.markdown(html_text, unsafe_allow_html=True)  