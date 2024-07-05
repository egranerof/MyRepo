import streamlit as st 

choix = st.sidebar.radio("Base de données",['MITBIH', 'PTBDB']) 

if choix == 'MITBIH': 

  st.write("### Présentation de la base de données MITBIH") 

  st.write("Elle est issu d'une collaboration entre le Beth Israel Deaconess Medical Center et le MIT depuis 1975")  

  st.write("Elle contient 48 extraits de demi-heure d'enregistrements ECG ambulatoires à deux canaux, provenant de 47 sujets étudiés entre 1975 et 1979")  

  st.write("Ils sont numérisés à une fréquence de 360 échantillons par seconde par canal, avec une résolution de 11 bits sur une plage de 10 mV, ils totalisent environ 25 heures de données ECG") 

  st.write("L'analyse de chaque battement, structurée en une matrice de données de 109 446 lignes et 188 colonnes ")          

  st.write("Chaque ligne représente un battement enregistré,la dernière colonne de cette base de données contient le type de battement, codé sous forme de chiffre de 0 à 4")          

  st.write("Classe 0: Normal Beats") 

  st.write("Classe 1: Supraventricular Ectopy Beats") 

  st.write("Classe 2: Ventricular Ectopy Beats") 

  st.write("Classe 3: Fusion Beats") 

  st.write("Classe 4: Unclassifiable Beats") 

 

if choix == 'PTBDB': 

  st.write("### Présentation de la base de données PTBDB") 

  st.write("La base de données contient 549 enregistrements de 290 sujets")
  st.write("Chaque sujet est représenté par un à cinq enregistrements") 

  st.write(" Chaque signal est numérisé à 1000 échantillons par seconde, avec une résolution de 16 bits sur une plage de ± 16,384 mV")    

  st.write("Les classes diagnostiques des 268 sujets sont diverses avec une majorité pour l'infarctus du myocarde avec 148 sujets")

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