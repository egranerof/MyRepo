import streamlit as st
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

html_title = """
<h2 style="text-align: center;"> Remerciement</h2>
"""
st.markdown(html_title, unsafe_allow_html=True)

texte = """
<div style="text-align: center;">
    <span style="font-weight: bold; font-size: 30px;">
        Merci pour votre attention
    </span>
</div>
"""

st.markdown(texte, unsafe_allow_html=True)

image = """
<div style="text-align: center;">
    <img src="https://www.karrieretag.org/wp-content/uploads/2024/02/datascientest-logo.png" alt="Logo DataScientest" width="300">
</div>
"""

st.markdown(image, unsafe_allow_html=True)

st.write("Pour la qualité de la formation, et le suivi tout au long de la formation")  
texte = """
<div style="text-align: center; font-weight: bold; font-size: 30px;">
    Xavier
</div>
"""

st.markdown(texte, unsafe_allow_html=True)
st.write("Pour son accompagnement et ses conseils très pertinents et précieux pour le bon accomplissement du projet")  

texte = """
<div style="text-align: center; font-weight: bold; font-size: 30px;">
Raja
</div>
"""

st.markdown(texte, unsafe_allow_html=True)

st.write("Pour sa présence, sa gentillesse et sa bienveillance")



