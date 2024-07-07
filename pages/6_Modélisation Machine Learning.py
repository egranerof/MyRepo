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
import joblib
import os

@st.cache_data  # 👈 Add the caching decorator
def load_data():
    
    archivos = [f'parte_{i+1}.csv' for i in range(5)]
    dfs = []

    for archivo in archivos:  
        df_part = pd.read_csv(archivo)
        dfs.append(df_part)

    df_mit = pd.concat(dfs, ignore_index=True)

    return df_mit

@st.cache_data  # 👈 Add the caching decorator
def load_data2():
    df_normal = pd.read_csv("ptbdb_normal.csv", header = None) 
    df_abnormal = pd.read_csv("ptbdb_abnormal.csv", header = None) 

    df_ptb = pd.concat([df_normal, df_abnormal], ignore_index=True)
    
    return df_ptb


@st.cache_data
def smotesplit(df_mit, df_ptb):
    smo = SMOTE()
    X_mit = df_mit.iloc[:, :-1]
    y_mit = df_mit.iloc[:, -1]
    X_mit_sm, y_mit_sm = smo.fit_resample(X_mit, y_mit)
    X_train_sm, X_test_sm, y_train_sm, y_test_sm = train_test_split(X_mit_sm, y_mit_sm, test_size=0.3, random_state=42)
    # X_train_red, X_test_red, y_train_red, y_test_red = train_test_split(X_train_sm, y_train_sm, test_size=0.7, random_state=42)
    
    X_ptb = df_ptb.iloc[:, :-1]
    y_ptb = df_ptb.iloc[:, -1]
    smo2 = SMOTE()
    X_ptb_sm, y_ptb_sm = smo2.fit_resample(X_ptb, y_ptb)
    X_train_ptb_sm, X_test_ptb_sm, y_train_ptb_sm, y_test_ptb_sm = train_test_split(X_ptb_sm, y_ptb_sm, test_size=0.2, random_state=42)
    
    return X_train_sm, X_test_sm, y_train_sm, y_test_sm, X_train_ptb_sm, X_test_ptb_sm, y_train_ptb_sm, y_test_ptb_sm

df_mit = load_data()
df_ptb = load_data2()
(X_train_sm, X_test_sm, y_train_sm, y_test_sm, X_train_ptb_sm, X_test_ptb_sm, y_train_ptb_sm, y_test_ptb_sm) = smotesplit(df_mit, df_ptb)

    
st.markdown('### Modèles de Machine Learning')
st.write("Afin de répondre à notre problématique de classification, nous avons dans un premier temps  "
         "choisi des modèles d'apprentissage automatique supervisé tels que le Random forest,  "
         "le Decision Tree, et ce avec les simples paramètres par défaut")


def train_and_save_model(classifier, file_name):
    if classifier == 'Random Forest':
        clf = RandomForestClassifier(n_jobs = -1, random_state = 123)
        clf.fit(X_train_sm, y_train_sm)
        joblib.dump(clf, file_name, compress=('gzip', 2))
        return clf


def train_and_save_model2(classifier, file_name):
    if classifier == 'Decision Tree':
        clf = DecisionTreeClassifier(criterion='gini', random_state=123)
        clf.fit(X_train_ptb_sm, y_train_ptb_sm)
        joblib.dump(clf, file_name, compress=('gzip', 2))
        return clf

# Fonction pour charger un modèle sauvegardé
def load_model(file_name):
    if os.path.exists(file_name):
        return joblib.load(file_name)
    return None

# Fonction pour obtenir les scores
def get_scores(clf, choice):
    global X_test_sm, y_test_sm
    if choice == 'Accuracy':
        return accuracy_score(y_test_sm, clf.predict(X_test_sm))
    elif choice == 'Confusion matrix':
        return confusion_matrix(y_test_sm, clf.predict(X_test_sm))


# Fonction pour obtenir les scores
def get_scores2(clf2, choice):
    global X_test_ptb_sm, y_test_ptb_sm
    if choice == 'Accuracy':
        return accuracy_score(y_test_ptb_sm, clf2.predict(X_test_ptb_sm))
    elif choice == 'Confusion matrix':
        return confusion_matrix(y_test_ptb_sm, clf2.predict(X_test_ptb_sm))

tabs = st.tabs(["**MITBIH**", "**PTBDB**"])

css = '''
<style>
  button[data-baseweb="tab"] {
  font-size: 24px;
  margin: 0;
  width: 100%;
  }
  .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
  font-size:1rem;
  }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

with tabs[0]:
    st.subheader("Le modèle Random Forest")
    # Définir le nom du fichier pour chaque modèle
    Projet = {
        'Random Forest': 'random_forest_model.pkl.gz'
    }
    classifier = 'Random Forest'
    Projet = Projet[classifier]

    # Charger ou entraîner le modèle sélectionné
    clf = load_model(Projet)
    if clf is None:
        clf = train_and_save_model(classifier, Projet)
        st.write('Le modèle a été entraîné et sauvegardé.')
    else:
        st.write('Le modèle a été chargé depuis le fichier.')

    # Choix d'affichage de l'accuracy ou de la matrice de confusion
    display_choice = st.radio('Que souhaitez-vous montrer ?', ('Accuracy', 'Confusion matrix'), key=1)
    if display_choice == 'Accuracy':
        st.write('Accuracy:', get_scores(clf, display_choice))
    elif display_choice == 'Confusion matrix':
        st.write('Confusion matrix:')
        st.dataframe(get_scores(clf, display_choice))
    

with tabs[1]:
    st.subheader("Le modèle Decision Tree")
    # Définir le nom du fichier pour chaque modèle
    Projet = {
        'Decision Tree': 'decision_tree_model.pkl.gz'
    }

    classifier = 'Decision Tree'
    Projet = Projet[classifier]

    # Charger ou entraîner le modèle sélectionné
    clf2 = load_model(Projet)
    if clf2 is None:
        clf2 = train_and_save_model2(classifier, Projet)
        st.write('Le modèle a été entraîné et sauvegardé.')
    else:
        st.write('Le modèle a été chargé depuis le fichier.')

    # Choix d'affichage de l'accuracy ou de la matrice de confusion
    display_choice2 = st.radio('Que souhaitez-vous montrer ?', ('Accuracy', 'Confusion matrix'), key=2)
    if display_choice2 == 'Accuracy':
        st.write('Accuracy:', get_scores2(clf2, display_choice2))
    elif display_choice2 == 'Confusion matrix':
        st.write('Confusion matrix:')
        st.dataframe(get_scores2(clf2, display_choice2))




    
    