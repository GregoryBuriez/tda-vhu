import streamlit as st
import pandas as pd
import numpy as np
import os



########################"CHARGEMENT DES DONNEES"################################
# Charger les données
df = pd.read_excel("FINAL.xlsx')
# Charger les données pour la carte
#data = pd.read_excel("Map nb vhu.xlsx')

# Convertir les colonnes en types de données appropriés
df['Vehicule'] = df['Vehicule'].astype(str)  # Convertir la colonne 'Vehicule' en chaîne de caractères
df['Ville'] = df['Ville'].astype(str)        # Convertir la colonne 'Ville' en chaîne de caractères

################################"VIDEO PRESENTATION"################################""

#st.title('Compte rendu inventaire bailleurs sociaux')

# Définir le chemin vers votre vidéo
#video_file_path = "https://drive.google.com/file/d/1o47zz06n_x36wZOIKrz3bERCYJ4dT7C2/view?usp=sharing"

# Lire et afficher la vidéo
#st.title("Lecteur de vidéo Streamlit")
#st.video(video_file_path)


############################## CREATION KPI ####################################
# Calcul du nombre total de lignes dans le dataframe
nombre_total_lignes = df.shape[0]

# Calcul du nombre total de résidences dans le dataframe
nombre_total_residences = data['Résidences'].nunique()
# Calcul du nombre de résidences avec et sans VHU
residences_avec_vhu = data[data['Nombre de VHU'] > 0]['Résidences'].nunique()
residences_sans_vhu = data[data['Nombre de VHU'] == 0]['Résidences'].nunique()

# Calcul des pourcentages
pourcentage_avec_vhu = (residences_avec_vhu / nombre_total_residences) * 100
pourcentage_sans_vhu = (residences_sans_vhu / nombre_total_residences) * 100

# Calcul du nombre de résidences avec et sans VHU
etat_complet = df[df['Etat'] == 'Complet'].shape[0]
etat_incomplet = df[df['Etat'] == 'Incomplet'].shape[0]

# Calcul des pourcentages
pourcentage_complet = (etat_complet / nombre_total_lignes) *100
pourcentage_incomplet = (etat_incomplet / nombre_total_lignes) *100

# Définition des styles CSS pour les cadres KPI
style_kpi_centered = """
    padding: 10px;
    background-color: #f9f9f9;
    border: 1px solid #e6e6e6;
    border-radius: 5px;
    box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
    margin-bottom: 10px;
    width: 100%;
    text-align: center;
"""

# Définir le style pour le conteneur flex
style_container = 'display: flex; width: 100%;'

# Définir le style pour chaque cadre KPI à l'intérieur du conteneur flex
style_kpi_inline = """
    padding: 10px;
    background-color: #f9f9f9;
    border: 1px solid #e6e6e6;
    border-radius: 4px;
    box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
    margin-bottom: 4px;
    width: calc(100% - 5px); /* 50% width minus margin between elements */
    text-align: center;
    margin-right: 10px; /* margin between elements */
"""

# Affichage dans Streamlit avec des cadres KPI personnalisés
st.subheader('Statistiques des Véhicules Hors d\'Usage (VHU)')

# Cadre KPI pour le nombre total de véhicules VHU
st.markdown(f'<div style="{style_kpi_centered}">\
                <h3 style="margin-bottom: 8px;">Nombre total de véhicules VHU</h3>\
                <p style="font-weight: bold; font-size: 24px;">{nombre_total_lignes}</p>\
              </div>', unsafe_allow_html=True)

# Cadre KPI pour le nombre total de résidences recensées
st.markdown(f'<div style="{style_kpi_centered}">\
                <h3 style="margin-bottom: 8px;">Nombre total de résidences recensées</h3>\
                <p style="font-weight: bold; font-size: 24px;">{nombre_total_residences}</p>\
              </div>', unsafe_allow_html=True)

# Création d'un tableau pour afficher les cadres KPI
col1, col2 = st.columns(2)

# Cadre KPI pour le nombre de résidences avec VHU (dans la colonne de gauche)
with col1:
    st.markdown(f"""
        <div style="{style_kpi_inline}">
            <h3 style="margin-bottom: 20px;">Nombre de résidences avec VHU</h3>
            <p style="font-weight: bold;">{residences_avec_vhu} ({pourcentage_avec_vhu:.2f}%)</p>
        </div>
    """, unsafe_allow_html=True)

# Cadre KPI pour le nombre de résidences sans VHU (dans la colonne de droite)
with col2:
    st.markdown(f"""
        <div style="{style_kpi_inline}">
            <h3 style="margin-bottom: 20px;">Nombre de résidences sans VHU</h3>
            <p style="font-weight: bold;">{residences_sans_vhu} ({pourcentage_sans_vhu:.2f}%)</p>
        </div>
    """, unsafe_allow_html=True)


##### TEST COMPLET INCOMPLET########



# Création d'un tableau pour afficher les cadres KPI
col3, col4 = st.columns(2)

# Cadre KPI pour le nombre de résidences avec VHU (dans la colonne de gauche)
with col3:
    st.markdown(f"""
        <div style="{style_kpi_inline}">
            <h3 style="margin-bottom: 20px;">Nombre de voitures complètes</h3>
            <p style="font-weight: bold;">{etat_complet} ({pourcentage_complet:.2f}%)</p>
        </div>
    """, unsafe_allow_html=True)

# Cadre KPI pour le nombre de résidences sans VHU (dans la colonne de droite)
with col4:
    st.markdown(f"""
        <div style="{style_kpi_inline}">
            <h3 style="margin-bottom: 20px;">Nombre de voiture incomplètes</h3>
            <p style="font-weight: bold;">{etat_incomplet} ({pourcentage_incomplet:.2f}%)</p>
        </div>
    """, unsafe_allow_html=True)

# Fermer le conteneur flex
st.markdown('</div>', unsafe_allow_html=True)


####################################"GRAPHIQUE PRESENTATION"###################################""

st.title('Représentation graphique des données')

# Définir le chemin vers votre image
image_path2 = "C:\\Users\\gregm\\OneDrive\\Bureau\\Test theo\\image GRAPHIQUES.png"

# Vérifier si l'image existe
if os.path.exists(image_path2):
    st.title("Graphique")
    st.image(image_path2)
else:
    st.error(f"L'image n'a pas été trouvée à l'emplacement: {image_path2}")



##########################"CREATION SOMMAIRE LATERALE"#############################""

# Ajouter l'expander pour afficher le DataFrame complet avec les filtres à l'intérieur
with st.expander("Détail fiches"):

    # Sommaire latéral pour sélectionner une commune
    communes = df['Ville'].unique()
    selected_commune = st.selectbox("Sélectionnez une commune", ['Toutes'] + list(communes))

    # Sommaire latéral pour sélectionner un bailleur
    bailleurs = df['Bailleur Sociale'].unique()
    selected_bailleur = st.selectbox("Sélectionnez un Bailleur", ['Tous'] + list(bailleurs))

    # Filtrage des données en fonction des sélections
    if selected_commune == 'Toutes' and selected_bailleur == 'Tous':
        filtered_df = df  # Aucun filtrage, toutes les données sont affichées
    elif selected_commune == 'Toutes':
        filtered_df = df[df['Bailleur Sociale'] == selected_bailleur]  # Filtrage par bailleur seulement
    elif selected_bailleur == 'Tous':
        filtered_df = df[df['Ville'] == selected_commune]  # Filtrage par commune seulement
    else:
        filtered_df = df[(df['Ville'] == selected_commune) & (df['Bailleur Sociale'] == selected_bailleur)]  # Filtrage par commune et bailleur

    # Calcul du nombre de VHU (nombre de lignes)
    nombre_vhu = filtered_df.shape[0]

    # Calcul du nombre de résidences avec VHU (nombre unique de valeurs dans la colonne Adresse)
    nombre_residences_vhu = filtered_df['Adresse'].nunique()

    # Afficher les données pour la commune sélectionnée et le bailleur sélectionné
    if selected_commune == 'Toutes' and selected_bailleur == 'Tous':
        st.write(f"### Toutes les données ({nombre_vhu} VHU, {nombre_residences_vhu} résidences avec VHU)")
    else:
        st.write(f"### Données pour la commune : {selected_commune} et le bailleur : {selected_bailleur} ({nombre_vhu} VHU, {nombre_residences_vhu} résidences avec VHU)")

    # Afficher le DataFrame complet filtré avec les colonnes spécifiées
    st.dataframe(filtered_df[['Fiche Numéro', 'Créé le', 'Marque', 'Etat', 'Adresse', 'Ville', 'Bailleur Sociale']])

###############################"CARTE INTERACTIVE##############################

import streamlit.components.v1 as components

st.title('Affichage de la page HTML')
# Définir le chemin vers votre fichier HTML
html_file_path = "C:\\Users\\gregm\\OneDrive\\Bureau\\Test theo\\carte_vhu_martinique.html"
# Lire le contenu du fichier HTML
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()
# Afficher le contenu HTML
components.html(html_content, height=800)  # Ajustez la hauteur selon vos besoins

