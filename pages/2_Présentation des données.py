import streamlit as st 


# choix = st.sidebar.radio("Base de données",['MITBIH', 'PTBDB']) 

tabs = st.tabs(["**MITBIH**", "**PTBDB**"])

css = '''
<style>
  button[data-baseweb="tab"] {
  font-size: 24px;
  margin: 0;
  width: 100%;
  }
  .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
  font-size:1.5rem;
  }
  
</style>

'''

st.markdown(css, unsafe_allow_html=True)



with tabs[0]:
    st.markdown('#### Présentation de la base de données MITBIH')
   
    st.write("- Elle est issu d'une collaboration entre le Beth Israel Deaconess Medical Center et le MIT (Massachusetts Institute of Technology) depuis 1975")  

    st.write("- Elle contient 48 extraits d'une demi-heure d'enregistrements ECG ambulatoires à deux canaux, provenant de 47 sujets étudiés entre 1975 et 1979")  

    st.write("- Ils sont numérisés à une fréquence de 360 échantillons par seconde par canal") 
    st.write("- Chaque battement a été annoté par 2 cardiologues , les annotations ont été utilisées pour créer 5 catégories de battements différents en accord avec la norme AAMI EC57")
    
    st.markdown('')
    
    st.write("Classe 0: Normal Beats") 

    st.write("Classe 1: Supraventricular Ectopy Beats") 

    st.write("Classe 2: Ventricular Ectopy Beats") 

    st.write("Classe 3: Fusion Beats") 

    st.write("Classe 4: Unclassifiable Beats") 
    
with tabs[1]:
    st.markdown('#### Présentation de la base de données PTBDB') 
    st.write("- La base de données contient 549 enregistrements de 290 sujets")
    st.write("- Chaque sujet est représenté par un à cinq enregistrements") 

    st.write("- Chaque signal est numérisé à 1000 échantillons par seconde")    

    st.write("- Les classes diagnostiques des 268 sujets sont diverses avec une majorité pour l'infarctus du myocarde avec 148 sujets et 52 sujets sains")
    
    st.markdown('')
    
    table_markdown = """
    | Classe de diagnostic                  | Nombre de sujets |      
    |----------                             |-----             |
    | Infarctus du myocarde                 | <span style="color:red;">148</span>              | 
    | Cardiomyopathie/Insuffisance cardiaque| 18               |
    | Regrouper le bloc de branche          | 15               |
    | Dysrythmie                            | 14               |       
    |Hypertrophie myocardique               |  7               |
    |Cardiopathie valvulaire                |  6               |
    |Myocardite                             |  4               |
    |Divers                                 |  4               |
    |Témoins sains                          | <span style="color:red;">52</span>               |

    """
    st.markdown(table_markdown, unsafe_allow_html=True)


st.sidebar.markdown("<br><br>", unsafe_allow_html=True)


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
