

# Application de Description d'Image en Français

## Description

Cette application Streamlit permet aux utilisateurs de télécharger une image et d'obtenir automatiquement une description de cette image en français. Elle utilise des modèles d'intelligence artificielle pour analyser le contenu de l'image et générer une description textuelle, qui est ensuite traduite en français.

## Fonctionnalités

- Interface utilisateur simple et intuitive
- Téléchargement d'images (formats supportés : JPG, JPEG, PNG)
- Analyse automatique du contenu de l'image
- Génération d'une description en anglais
- Traduction automatique de la description en français
- Affichage de la description en français

## Comment ça marche

1. L'utilisateur télécharge une image via l'interface Streamlit.
2. L'image est envoyée à un modèle de vision par ordinateur (Salesforce/blip-image-captioning-large) qui génère une description en anglais.
3. Cette description est ensuite transmise à un modèle de traduction (google-t5/t5-base) qui la traduit en français.
4. La description traduite est affichée à l'utilisateur.

## Prérequis

- Python 3.7+
- Streamlit
- Requests
- Pillow (PIL)

## Installation

1. Clonez ce dépôt : [Dépôt]().
