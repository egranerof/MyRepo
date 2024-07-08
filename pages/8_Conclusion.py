import streamlit as st




st.markdown('### • Conclusion')

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

st.write("""
Suite aux diverses expériences réalisées pour établir le meilleur modèle capable d’extraire les caractéristiques des signaux cardiaques (très complexes, comme nous avons pu le constater lors de l'étape de visualisation) et de présenter les meilleures performances pour leur classification, on a constaté que :

Parmi les modèles d’apprentissage automatique, **le Random Forest** a démontré une performance supérieure comparée aux autres algorithmes. Ce résultat a sans doute été favorisé par la méthode SMOTE, qui a permis d’équilibrer les classes minoritaires tout en offrant une diversité d’échantillons au sein de ces classes.

Parmi les réseaux de neurones profonds, le modèle **CNN** s’est réellement distingué et a démontré ses capacités puissantes à analyser les aspects complexes du signal ECG, tels que les intervalles RR et les intervalles QRS. Cela lui a conféré une meilleure performance, surpassant les autres modèles en termes de précision, de rappel, et de F1-score.

En résumé, notre étude a démontré que les réseaux de neurones convolutifs sont particulièrement bien adaptés pour l'analyse des signaux ECG, offrant une solution efficace pour la classification des anomalies cardiaques.
""")

st.write("""
### Pour aller plus loin :

Il serait intéressant de tester la combinaison du modèle CNN (très puissant pour l’extraction des caractéristiques) avec d’autres algorithmes de classification, par exemple le Random Forest ou le SVM (modèle hybride).

Il serait également intéressant d’explorer la combinaison du CNN avec le LSTM, qui présente l'avantage supplémentaire de capturer les dépendances temporelles à long terme dans les données séquentielles.
""")

