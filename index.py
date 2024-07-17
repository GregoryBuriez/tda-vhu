import streamlit as st
import pandas as pd
import numpy as np
import os



########################"CHARGEMENT DES DONNEES"################################
# Charger les données
df = pd.read_csv('FINALtda.csv', delimiter=';')
# Charger les données pour la carte
data = pd.read_csv("Mapnbvhu.csv", delimiter=';')

# Convertir les colonnes en types de données appropriés
df['Vehicule'] = df['Vehicule'].astype(str)  # Convertir la colonne 'Vehicule' en chaîne de caractères
df['Ville'] = df['Ville'].astype(str)        # Convertir la colonne 'Ville' en chaîne de caractères

################################"VIDEO PRESENTATION"################################""

st.title('INVENTAIRE BAILLEURS 2024')

# Ajouter un sous-titre avec Markdown
st.markdown('Inventaire 2024')
# Insérer l'URL de la vidéo YouTube
youtube_url = "https://www.youtube.com/watch?v=QkF3oxziUI4"

# Afficher la vidéo YouTube sur Streamlit
st.video(youtube_url)


############################## CREATION KPI ####################################
# Liste des communes et bailleurs uniques pour les menus déroulants
communes_uniques = data['Commune'].unique()
bailleurs_uniques = data['Bailleur'].unique()

# Widget pour sélectionner la commune dans la barre latérale
selected_commune = st.sidebar.selectbox('Sélectionner une commune', communes_uniques)

# Widget pour sélectionner le bailleur dans la barre latérale
selected_bailleur = st.sidebar.selectbox('Sélectionner un bailleur', bailleurs_uniques)

# Filtrage des données en fonction des sélections
filtered_data = data[(data['Commune'] == selected_commune) & (data['Bailleur'] == selected_bailleur)]

# Calcul des nouveaux KPI basés sur les données filtrées
nombre_total_residences_filtre = filtered_data['Residences'].nunique()
residences_avec_vhu_filtre = filtered_data[filtered_data['Nombre de VHU'] > 0]['Residences'].nunique()
residences_sans_vhu_filtre = filtered_data[filtered_data['Nombre de VHU'] == 0]['Residences'].nunique()
etat_complet_filtre = filtered_data[filtered_data['Etat'] == 'Complet'].shape[0]
etat_incomplet_filtre = filtered_data[filtered_data['Etat'] == 'Incomplet'].shape[0]

# Calcul des pourcentages basés sur les données filtrées
pourcentage_avec_vhu_filtre = (residences_avec_vhu_filtre / nombre_total_residences_filtre) * 100
pourcentage_sans_vhu_filtre = (residences_sans_vhu_filtre / nombre_total_residences_filtre) * 100
pourcentage_complet_filtre = (etat_complet_filtre / filtered_data.shape[0]) * 100
pourcentage_incomplet_filtre = (etat_incomplet_filtre / filtered_data.shape[0]) * 100

# Affichage des KPI mis à jour
st.subheader('Statistiques des Véhicules Hors d\'Usage (VHU)')

# Cadre KPI pour le nombre total de résidences recensées (basé sur les données filtrées)
st.markdown(f'<div style="{style_kpi_centered}">\
                <h3 style="margin-bottom: 8px;">Nombre total de résidences recensées (Filtré)</h3>\
                <p style="font-weight: bold; font-size: 24px;">{nombre_total_residences_filtre}</p>\
              </div>', unsafe_allow_html=True)

# Cadre KPI pour le nombre de résidences avec VHU (basé sur les données filtrées)
st.markdown(f"""
    <div style="{style_kpi_inline}">
        <h3 style="margin-bottom: 20px;">Nombre de résidences avec VHU (Filtré)</h3>
        <p style="font-weight: bold;">{residences_avec_vhu_filtre} ({pourcentage_avec_vhu_filtre:.2f}%)</p>
    </div>
""", unsafe_allow_html=True)

# Cadre KPI pour le nombre de résidences sans VHU (basé sur les données filtrées)
st.markdown(f"""
    <div style="{style_kpi_inline}">
        <h3 style="margin-bottom: 20px;">Nombre de résidences sans VHU (Filtré)</h3>
        <p style="font-weight: bold;">{residences_sans_vhu_filtre} ({pourcentage_sans_vhu_filtre:.2f}%)</p>
    </div>
""", unsafe_allow_html=True)

# Cadre KPI pour le nombre de véhicules complets (basé sur les données filtrées)
st.markdown(f"""
    <div style="{style_kpi_inline}">
        <h3 style="margin-bottom: 20px;">Nombre de véhicules complets (Filtré)</h3>
        <p style="font-weight: bold;">{etat_complet_filtre} ({pourcentage_complet_filtre:.2f}%)</p>
    </div>
""", unsafe_allow_html=True)

# Cadre KPI pour le nombre de véhicules incomplets (basé sur les données filtrées)
st.markdown(f"""
    <div style="{style_kpi_inline}">
        <h3 style="margin-bottom: 20px;">Nombre de véhicules incomplets (Filtré)</h3>
        <p style="font-weight: bold;">{etat_incomplet_filtre} ({pourcentage_incomplet_filtre:.2f}%)</p>
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
image_path2 = "image GRAPHIQUES.png"

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
html_file_path = "carte_vhu_martinique.html"
# Lire le contenu du fichier HTML
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()
# Afficher le contenu HTML
components.html(html_content, height=800)  # Ajustez la hauteur selon vos besoins

