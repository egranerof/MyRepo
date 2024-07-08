import streamlit as st
# st.markdown('### Modèles Deep Learning')
html_text = """
<div class="custom-html-container" style="position: fixed; bottom: 10px; width: 15%; border: 2px solid blue; padding: 10px; border-radius: 5px;">
    <p style="font-size: 16px; text-align: center;"><strong>Projet DS</strong></p>
    <p style="font-size: 14px; text-align: center;">Promotion Avril 2024</p>
    <p style="font-size: 14px;">
        <a href="https://linkedin.com/in/soraya-merbah/" target="_blank">Soraya MERBAH</a>
    </p>
    <p style="font-size: 14px;">
        <a href="https://linkedin.com/in/emanuelgf/" target="_blank">Emanuel FERNANDEZ GRANERO</a>
    </p>
</div>
"""

# Afficher le texte encadré dans la barre latérale
st.sidebar.markdown(html_text, unsafe_allow_html=True)

import streamlit as st


# Diapositive 1: Introduction aux Réseaux Neuronaux
st.header("Introduction aux Réseaux Neuronaux")
st.write("""
Les réseaux neuronaux artificiels (ANN) sont des modèles d'apprentissage automatique inspirés du cerveau humain. 
Ils sont composés de neurones artificiels organisés en couches.
         """)
st.image('./images/ANN.png')
st.write("")
st.subheader("Analyse exploratoire:")  
st.write("""
La correcte prédiction du type de battements est donc un problème de **classification**. Le defi se trouve dans la capacité de notre modèle à reconnaitre les caracteristiques des series temporelles.
Pour cela, on a choici trois types principaux de ANN comme candidats dans la phase exploratoire :
- **DNN (Deep Neural Networks)**: plusieurs couches de neurones, chacune appliquant une transformation non linéaire aux données pour apprendre des représentations complexes.
- **LSTM (Long Short-Term Memory)**: un type de Réseaux de Neurones Récurrents, possèdant des connexions cycliques qui permettent de conserver une mémoire des informations précédentes au sein de la séquence.
- **CNN (Convolutional Neural Networks)**: sls utilisent des couches de convolution pour extraire des caractéristiques locales pertinentes.
""")
st.markdown("---")

st.subheader("Modèle CNN 1 Dimension :")
col1, col2 = st.columns([2.5, 1])

    # Dans col1 (colonne de gauche), mettre le texte descriptif
with col1:
    st.write("""
Pour notre projet, le modèle qui a montré les meilleures performances est un réseau de neurones convolutionnel 1D. 
Ce modèle est particulièrement bien adapté à notre problème de classification multiple car il peut extraire efficacement 
des caractéristiques locales des données séquentielles. Voici l'architecture du modèle que nous avons utilisé :
- Couches de convolution 1D
- Couches de pooling
- Couches fully connected
- Avantages: extraction de caractéristiques locales et bonne performance sur données séquentielles.

Pour l'optimisation des paramètre du modèle CNN 1D on a testé different cantités des filtres (16, 32, 64 et 128), asi que de taille de noyeau (kernel 3 et 5) et de fonction d'activation (Relu, Elu).

Les meilleurs résultats ont été obtenus avec **32 et 64 filtres pour les couches Convolutionelles 1 et 2 respectivement, un kernel de taille 3, et une fonction Relu**.

Cependant les performances entres les differentes conditions ont été très similaires, exceptionellement bonnes dans tous les cas. La difference plus significative se trouvant dans le temps d'execution.
""")

    # Charger et afficher l'image dans col2 (colonne de droite)
with col2:
    image = open('./images/model_cnn_plot2.png', 'rb').read()
    st.image(image, caption='Représentation graphique du modèle CNN', use_column_width=True)

st.markdown("---")
st.subheader("Résultats : History, Classification Report et Matrice de Confusion")
st.write("""
L'évolution de la précision et de la fonction de perte au cours des époques montre que de hautes performances (>98%) sont 
atteintes assez rapidement (<10 époques). Cependant, avec les itérations successives, nous continuons à améliorer les résultats (notamment le F1-score), 
jusqu'à ce que les performances stagnent très près de 100%, peu après 50 époques.
""")
image2 = open('./images/history.png', 'rb').read()
st.image(image2, caption="History d'evolution de l'accuracy et la fonction de perte", use_column_width=True)
st.write("")
st.write("")
st.write("")
st.write("""
Les indicateurs statistiques montrent tous des performances très élevées, tant pour les données équilibrées ('test SMOTE') que pour le jeu de test non-équilibré ('NO-SMOTE').
""")
st.write("")
image3 = open('./images/ClassReport.png', 'rb').read()
st.image(image3, caption="Classification Report MITBIH du modèle avec le jeu test équilibré (SMOTE) ", use_column_width=True)
st.write("")
st.write("")
col3, col4 = st.columns([1, 1])
with col3:
    image4 = open('./images/confmatrix.png', 'rb').read()
    st.image(image4, caption='Matrice de Confusion MITBIH : test SMOTE', use_column_width=True)

with col4:
    image5 = open('./images/confmatrixNS.png', 'rb').read()
    st.image(image5, caption='Matrice de Confusion MITBIH : test NO-SMOTE', use_column_width=True)

st.markdown("---")
st.subheader("Résultats sur jeu PTBDB :")
st.write("""
La même méthodologie a été appliquée à la base de données PTB, à l'exception du type de classification : pour MITBIH, il s'agit d'une classification multiple, tandis que pour PTBDB, il s'agit d'une classification binaire. Dans le modèle, nous ajustons la fonction d'activation de la dernière couche (de softmax à sigmoid) ainsi que l'algorithme de calcul de la fonction de perte (de categorical_crossentropy à binary_crossentropy).

Les résultats restent néanmoins très positifs pour les deux types de jeux de données (SMOTE et NO-SMOTE) :
""")
image6 = open('./images/historyptb.png', 'rb').read()
st.image(image6, caption="History d'evolution de l'accuracy et la fonction de perte", use_column_width=True)
st.write("")
st.write("")
image7 = open('./images/ClassReportptb.png', 'rb').read()
st.image(image7, caption="Classification Report PTBDB du modèle avec le jeu test équilibré (SMOTE) ", use_column_width=True)
st.write("")
st.write("")
col5, col6 = st.columns([1, 1])
with col5:
    image4 = open('./images/confmatrixptb.png', 'rb').read()
    st.image(image4, caption='Matrice de Confusion PTBDB: test SMOTE', use_column_width=True)

with col6:
    image5 = open('./images/confmatrixptbNS.png', 'rb').read()
    st.image(image5, caption='Matrice de Confusion PTBDB: test NO-SMOTE', use_column_width=True)