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


df_train = pd.read_csv("mitbih_train.csv", header = None) 
df_test = pd.read_csv("mitbih_test.csv", header = None) 
df_mit = pd.concat([df_train, df_test], ignore_index=True)  

df_normal = pd.read_csv("ptbdb_normal.csv", header = None) 
df_abnormal = pd.read_csv("ptbdb_abnormal.csv", header = None) 
df_ptb = pd.concat([df_normal, df_abnormal], ignore_index=True)






st.markdown('### • Pre processing des données')

texte = ("Lors de la phase d'exploration, nous avons constaté que les deux bases de données étaient propres, "
        "absence de données manquantes, les valeurs d'amplitude étaient normalisées entre 0 et 1. "
        "Par contre, lorsqu'on s'est intéressé au nombres d'observation par catégorie, "
        "on constate qu'il y a un réel déséquilibre.")
st.write(texte)


show_graph = st.checkbox('Afficher le graphique données déséquilibrées MITBIH')
if show_graph:

    fig = plt.figure(figsize=(7, 7))
    equilibre = df_mit[187].value_counts()
    plt.pie(equilibre, labels = ['Normal Beats','Supraventricular Ectopy Beats','Supraventricular Ectopy Beats','Fusion Beats','Unclassifiable Beats'], 
        colors=['Blue','Green','Yellow','Skyblue','Orange'],autopct='%1.1f%%', textprops={'color': 'black'}) 
    st.pyplot(fig)
    



show_graph = st.checkbox('Afficher le graphique données déséquilibrées PTBDB')
if show_graph:
    df_ptb[187].value_counts()
    categorie_counts = df_ptb.iloc[:, -1].value_counts()
    fig = plt.figure()
    categorie_counts.plot(kind='bar', color=['blue', 'orange'])
    plt.title('Count of each category in PTBDB')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.xticks(ticks=[1, 0], labels=['Normal', 'Abnormal'],rotation=0)
    st.pyplot(fig)

texte = ("Afin d'y remédier, nous avons choisi la méthode smote **Synthetic Minority Oversampling Technic** pour équilibrer nos 2 Datasets")
         

     # Affichage du texte avec Streamlit
st.write(texte)

X_mit= df_mit.drop([187], axis = 1)
y_mit= df_mit[187]

smo = SMOTE()
X_mit_sm,y_mit_sm = smo.fit_resample(X_mit,y_mit)
equilibre = y_mit_sm.value_counts()
show_graph = st.checkbox('Afficher le graphique données équilibrées MITBIH')
if show_graph:

    fig = plt.figure(figsize=(7, 7))
    plt.pie(equilibre, labels = ['Normal Beats','Supraventricular Ectopy Beats','Ventricular Ectopy Beats','Fusion Beats','Unclassifiable Beats'], colors=['Blue','Green','Yellow','Skyblue','Orange'],autopct='%1.1f%%', textprops={'color': 'black'}) 
    st.pyplot(fig)
show_graph = st.checkbox('Afficher le graphique données équilibrées PTBDB')
if show_graph:
    X_ptb= df_ptb.drop([187], axis = 1)
    y_ptb= df_ptb[187]
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
        

