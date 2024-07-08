import streamlit as st 
import pandas as pd  
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.metrics import classification_report_imbalanced, geometric_mean_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report


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


st.markdown('### Preprocessing des données')

texte = ("Lors de la phase d'exploration, nous avons constaté que les deux bases de données étaient propres, "
        "absence de données manquantes, les valeurs d'amplitude étaient normalisées entre 0 et 1. "
        "Par contre, lorsqu'on s'est intéressé au nombres d'observation par catégorie, "
        "on constate qu'il y a un réel déséquilibre.")
st.write(texte)


show_graph = st.checkbox('Afficher le graphique données déséquilibrées MITBIH')
if show_graph:

    fig = plt.figure(figsize=(7, 7))
    equilibre = df_mit.iloc[:, -1].value_counts()
    plt.pie(equilibre, labels = ['Normal Beats','Supraventricular Ectopy Beats','Supraventricular Ectopy Beats','Fusion Beats','Unclassifiable Beats'], 
        colors=['Blue','Green','Yellow','Skyblue','Orange'],autopct='%1.1f%%', textprops={'color': 'black'}) 
    st.pyplot(fig)
    



show_graph2 = st.checkbox('Afficher le graphique données déséquilibrées PTBDB')
if show_graph2:
    # df_ptb[187].value_counts()
    categorie_counts = df_ptb.iloc[:, -1].value_counts()
    fig = plt.figure()
    categorie_counts.plot(kind='bar', color=['blue', 'orange'])
    plt.title('Count of each category in PTBDB')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.xticks(ticks=[1, 0], labels=['Normal', 'Abnormal'],rotation=0)
    st.pyplot(fig)

st.markdown(" ")
st.markdown(" ")
texte = ("Afin d'y remédier, nous avons choisi la méthode smote **Synthetic Minority Oversampling Technic** pour équilibrer nos 2 Datasets")
         
st.write(texte)


@st.cache_data  # 👈 Add the caching decorator
def show3():
    X_mit = df_mit.iloc[:, :-1]
    y_mit = df_mit.iloc[:, -1]

    smo = SMOTE()
    X_mit_sm,y_mit_sm = smo.fit_resample(X_mit,y_mit)
    equilibre = y_mit_sm.value_counts()
    
    fig = plt.figure(figsize=(7, 7))
    plt.pie(equilibre, labels = ['Normal Beats','Supraventricular Ectopy Beats','Ventricular Ectopy Beats','Fusion Beats','Unclassifiable Beats'], colors=['Blue','Green','Yellow','Skyblue','Orange'],autopct='%1.1f%%', textprops={'color': 'black'}) 
    st.pyplot(fig)
    
    return

@st.cache_data  # 👈 Add the caching decorator
def show4():
    X_ptb = df_ptb.iloc[:, :-1]
    y_ptb = df_ptb.iloc[:, -1]
    smo = SMOTE()
    X_ptb_sm,y_ptb_sm = smo.fit_resample(X_ptb,y_ptb)
    categorie_counts = y_ptb_sm.value_counts()
    fig = plt.figure()
    categorie_counts.plot(kind='bar', color=['blue', 'orange'])
    plt.title('Count of each category in PTBDB')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.xticks(ticks=[1, 0], labels=['Normal', 'Abnormal'],rotation=0)
    st.pyplot(fig)
    
    return


show_graph3 = st.checkbox('Afficher le graphique données équilibrées MITBIH')
if show_graph3:
    show3()
    
show_graph4 = st.checkbox('Afficher le graphique données équilibrées PTBDB')
if show_graph4:
    show4()
        

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
