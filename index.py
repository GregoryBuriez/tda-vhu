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

# Remplacer les valeurs "TAUPINIÈRE" par "LE DIAMANT" dans la colonne "NOM"
df.loc[df['Ville'] == 'TAUPINIÈRE', 'Ville'] = 'LE DIAMANT'

df['Vehicule'] = df['Vehicule'].astype(str)  # Convertir la colonne 'Vehicule' en chaîne de caractères
df['Ville'] = df['Ville'].astype(str)        # Convertir la colonne 'Ville' en chaîne de caractères

################################"VIDEO PRESENTATION"################################""

# CSS to center the title
st.markdown(
    """
    <style>
    .center-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Centered title
st.markdown('<div class="center-title">INVENTAIRE BAILLEURS 2024</div>', unsafe_allow_html=True)


# Insérer l'URL de la vidéo YouTube
youtube_url = "https://youtu.be/G2ecW4E72ug"

# Afficher la vidéo YouTube sur Streamlit
st.video(youtube_url)


############################## CREATION KPI ####################################
# Calcul du nombre total de lignes dans le dataframe
nombre_total_lignes = df.shape[0]

# Calcul du nombre total de résidences dans le dataframe
nombre_total_residences = data['Residences'].nunique()
# Calcul du nombre de résidences avec et sans VHU
residences_avec_vhu = data[data['Nombre de VHU'] > 0]['Residences'].nunique()
residences_sans_vhu = data[data['Nombre de VHU'] == 0]['Residences'].nunique()

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
    border-radius: 5px;
    box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
    margin-bottom: 10px;
    width: 100%;
    """


# Cadre KPI pour le nombre total de véhicules VHU
st.markdown(f'<div style="{style_kpi_centered}">\
                <h3 style="margin-bottom: 8px;">Nombre total de VHU recensés</h3>\
                <p style="font-weight: bold; font-size: 30px;">{nombre_total_lignes}</p>\
              </div>', unsafe_allow_html=True)

# Cadre KPI pour le nombre total de résidences recensées
st.markdown(f'<div style="{style_kpi_centered}">\
                <h3 style="margin-bottom: 8px;">Nombre total de résidences recensées</h3>\
                <p style="font-weight: bold; font-size: 30px;">{nombre_total_residences}</p>\
              </div>', unsafe_allow_html=True)

# Création d'un tableau pour afficher les cadres KPI
col1, col2 = st.columns(2)

# Cadre KPI pour le nombre de résidences avec VHU (dans la colonne de gauche)
with col1:
    st.markdown(f"""
        <div style="{style_kpi_inline}; text-align: center; margin: 0 auto;">
            <h3 style="margin-bottom: 20px;">Nombre de résidences avec VHU</h3>
            <p style="font-weight: bold; font-size: 20px;">{residences_avec_vhu} ({pourcentage_avec_vhu:.2f}%)</p>
        </div>
    """, unsafe_allow_html=True)

# Cadre KPI pour le nombre de résidences sans VHU (dans la colonne de droite)
with col2:
    st.markdown(f"""
        <div style="{style_kpi_inline}; text-align: center; margin: 0 auto;">
            <h3 style="margin-bottom: 20px;">Nombre de résidences sans VHU</h3>
            <p style="font-weight: bold; font-size: 20px;">{residences_sans_vhu} ({pourcentage_sans_vhu:.2f}%)</p>
        </div>
    """, unsafe_allow_html=True)


##### TEST COMPLET INCOMPLET########



# Création d'un tableau pour afficher les cadres KPI
col3, col4 = st.columns(2)

# Cadre KPI pour le nombre de résidences avec VHU (dans la colonne de gauche)
with col3:
    st.markdown(f"""
        <div style="{style_kpi_inline}; text-align: center; margin: 0 auto;">
            <h3 style="margin-bottom: 20px;">Nombre de voitures complètes</h3>
            <p style="font-weight: bold; font-size: 20px;">{etat_complet} ({pourcentage_complet:.2f}%)</p>
        </div>
    """, unsafe_allow_html=True)

# Cadre KPI pour le nombre de résidences sans VHU (dans la colonne de droite)
with col4:
    st.markdown(f"""
        <div style="{style_kpi_inline}; text-align: center; margin: 0 auto;">
            <h3 style="margin-bottom: 20px;">Nombre de voiture incomplètes</h3>
            <p style="font-weight: bold; font-size: 20px;">{etat_incomplet} ({pourcentage_incomplet:.2f}%)</p>
        </div>
    """, unsafe_allow_html=True)

# Fermer le conteneur flex
st.markdown('</div>', unsafe_allow_html=True)



####################################"GRAPHIQUE PRESENTATION"###################################""

st.title('Représentation graphique des données')

# Définir le chemin vers votre image
image_path2 = "télécharger.png"

# Vérifier si l'image existe
if os.path.exists(image_path2):
    st.image(image_path2)
else:
    st.error(f"L'image n'a pas été trouvée à l'emplacement: {image_path2}")



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

    # Calcul du nombre de VHU en état complet et incomplet
    nombre_vhu_complet = filtered_df[filtered_df['Etat'] == 'Complet'].shape[0]
    nombre_vhu_incomplet = filtered_df[filtered_df['Etat'] == 'Incomplet'].shape[0]

    # Calcul du nombre de VHU par bailleur si aucune sélection de bailleur
    if selected_bailleur == 'Tous' and selected_commune != 'Toutes':
        nombre_vhu_par_bailleur = filtered_df.groupby('Bailleur Sociale').size()

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

# Affichage des KPI
if selected_commune == 'Toutes' and selected_bailleur == 'Tous':
    st.markdown(f'<div style="{style_kpi_centered}">\
                    <h3 style="margin-bottom: 8px;">Toutes les données</h3>\
                    <p style="font-weight: bold; font-size: 24px;">{nombre_vhu} VHU, {nombre_residences_vhu} résidences avec VHU</p>\
                </div>', unsafe_allow_html=True)
elif selected_bailleur == 'Tous':
    st.markdown(f'<div style="{style_kpi_centered}">\
                    <h3 style="margin-bottom: 8px;">Données pour la commune : {selected_commune}</h3>\
                    <p style="font-weight: bold; font-size: 24px;">{nombre_vhu} VHU, {nombre_residences_vhu} résidences avec VHU</p>\
                </div>', unsafe_allow_html=True)
    # Affichage des VHU par bailleur
    for bailleur, count in nombre_vhu_par_bailleur.items():
        st.markdown(f'<div style="{style_kpi_centered}">\
                        <p style="font-weight: bold; font-size: 18px;">{bailleur} : {count} VHU</p>\
                    </div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div style="{style_kpi_centered}">\
                    <h3 style="margin-bottom: 8px;">Données pour la commune : {selected_commune} et le bailleur : {selected_bailleur}</h3>\
                    <p style="font-weight: bold; font-size: 24px;">{nombre_vhu} VHU, {nombre_residences_vhu} résidences avec VHU</p>\
                </div>', unsafe_allow_html=True)

# Affichage des nouveaux KPI pour état complet et incomplet
st.markdown(f'<div style="{style_kpi_centered}">\
                <h3 style="margin-bottom: 8px;">État des VHU</h3>\
                <p style="font-weight: bold; font-size: 24px;">{nombre_vhu_complet} VHU Complet, {nombre_vhu_incomplet} VHU Incomplet</p>\
            </div>', unsafe_allow_html=True)

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

################################ LIEN BI #################################

# Création de l'encart avec le lien
st.markdown("""
<div style="border:2px solid #0078d7; padding: 20px; text-align: center;">
    <a href="https://app.powerbi.com/groups/me/reports/8e94a596-3110-4c29-8d0a-9edaa239c059/ReportSection?experience=power-bi" 
       style="text-decoration: none; color: #0078d7; font-weight: bold;" target="_blank">
        Lien vers tableau de bord POWERBI
    </a>
</div>
""", unsafe_allow_html=True)

