import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

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


st.markdown('### Visualisation des données')

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
  
  option = st.selectbox('Choisissez option à afficher', ('battement normal', 'un battement par classe', 'un battement par classe dans le même graphique', 'dizaine de battements par classe' )) 
  if option == 'battement normal':
    fig = plt.figure() 
    plt.plot(df_mit.iloc[0]) 
    plt.xlabel('Durée en ms') 
    plt.ylabel('Valeurs normalisées')
    plt.xticks(range(0,190,25))
    st.pyplot(fig) 

  df_mit_0=df_mit[df_mit.iloc[:,187]==0.0] 
  df_mit_1=df_mit[df_mit.iloc[:,187]==1.0] 
  df_mit_2=df_mit[df_mit.iloc[:,187]==2.0] 
  df_mit_3=df_mit[df_mit.iloc[:,187]==3.0] 
  df_mit_4=df_mit[df_mit.iloc[:,187]==4.0] 

  if option == 'un battement par classe':


    fig = plt.figure(figsize=(12, 12)) 
    plt.subplot(321) 
    plt.title('Normal Beats')
    plt.plot(np.linspace(0, 186, 187), df_mit_0.iloc[0, 0:187], label='Sample 0') 
    plt.legend() 
    plt.subplot(322) 
    plt.title('Supraventricular Ectopy Beats') 
    plt.plot(np.linspace(0, 186, 187), df_mit_1.iloc[0, 0:187], label='Sample 0') 
    plt.legend() 
    plt.subplot(323) 
    plt.title('Ventricular Ectopy Beats') 
    plt.plot(np.linspace(0, 186, 187), df_mit_2.iloc[0, 0:187], label='Sample 0') 
    plt.legend() 
    plt.subplot(324) 
    plt.title('Fusion Beats') 
    plt.plot(np.linspace(0, 186, 187), df_mit_3.iloc[0, 0:187], label='Sample 0') 
    plt.legend() 
    plt.subplot(325) 
    plt.title('Unclassifiable Beats') 
    plt.plot(np.linspace(0, 186, 187), df_mit_4.iloc[0, 0:187], label='Sample 0') 
    plt.legend() 
    st.pyplot(fig) 

  if option == 'un battement par classe dans le même graphique':

    fig, ax = plt.subplots(figsize=(8, 5)) 

    ax.plot(np.linspace(0, 186, 187), df_mit_0.iloc[0, 0:187], label='Normal Beats') 

    ax.plot(np.linspace(0, 186, 187), df_mit_1.iloc[0, 0:187], label='Supraventricular Ectopy Beats') 

    ax.plot(np.linspace(0, 186, 187), df_mit_2.iloc[0, 0:187], label='Ventricular Ectopy Beats') 

    ax.plot(np.linspace(0, 186, 187), df_mit_3.iloc[0, 0:187], label='Fusion Beats') 

    ax.plot(np.linspace(0, 186, 187), df_mit_4.iloc[0, 0:187], label='Unclassifiable Beats') 

 

    ax.set_title('Représentation graphique d\'un battement de chaque catégorie') 

    ax.legend() 

    st.pyplot(fig)

  if option == 'dizaine de battements par classe':

    def plot_graphs(step=10):

       fig, axs = plt.subplots(3, 2, figsize=(12, 12)) 
       for i in range(0, 100, step):
        axs[0, 0].plot(np.linspace(0, 186, 187), df_mit_0.iloc[i, 0:187], label=f'Sample {i}') 
        axs[0, 0].set_title('Normal Beats') 
        axs[0, 0].legend() 
        axs[0, 1].plot(np.linspace(0, 186, 187), df_mit_1.iloc[i, 0:187], label=f'Sample {i}') 
        axs[0, 1].set_title('Supraventricular Ectopy Beats') 
        axs[0, 1].legend()
        axs[1, 0].plot(np.linspace(0, 186, 187), df_mit_2.iloc[i, 0:187], label=f'Sample {i}') 
        axs[1, 0].set_title('Ventricular Ectopy Beats') 
        axs[1, 0].legend() 
        axs[1, 1].plot(np.linspace(0, 186, 187), df_mit_3.iloc[i, 0:187], label=f'Sample {i}') 
        axs[1, 1].set_title('Fusion Beats') 
        axs[1, 1].legend() 
        axs[2, 0].plot(np.linspace(0, 186, 187), df_mit_4.iloc[i, 0:187], label=f'Sample {i}') 
        axs[2, 0].set_title('Unclassifiable Beats') 
        axs[2, 0].legend() 
       fig.delaxes(axs[2, 1])  # Supprimer le subplot vide 

       plt.tight_layout() 

       return fig 

    fig = plot_graphs(step=10) 

    st.pyplot(fig) 

with tabs[1]:

# if choix == 'PTBDB': 
  fig = plt.figure() 
  plt.plot(df_ptb.iloc[0]) 

  plt.xlabel('Durée en ms')
  plt.ylabel('Valeurs normalisées') 

  plt.title('Exemple de Battement Normal') 

  st.pyplot(fig) 


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