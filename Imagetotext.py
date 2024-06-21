import streamlit as st
import requests
from PIL import Image
import io

st.title("Image to text and english to french application")

# API URLs
IMAGE_API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
TRANSLATION_API_URL = "https://api-inference.huggingface.co/models/google-t5/t5-base"

headers = {"Authorization": "Bearer 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"}

def query_image(image_data):
    response = requests.post(IMAGE_API_URL, headers=headers, data=image_data)
    return response.json()

def query_translation(text):
    payload = {
        "inputs": f"translate English to French: {text}"
    }
    response = requests.post(TRANSLATION_API_URL, headers=headers, json=payload)
    return response.json()

uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Image téléchargée', use_column_width=True)
    
    # Convert image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    if st.button('Obtenir la Description en Français'):
        with st.spinner('Analyse de l\'image et traduction en cours...'):
            # Get image description
            result = query_image(img_byte_arr)
            if isinstance(result, list) and len(result) > 0 and 'generated_text' in result[0]:
                description = result[0]['generated_text']
                
                # Translate description to French
                translation_result = query_translation(description)
                if isinstance(translation_result, list) and len(translation_result) > 0:
                    translated_description = translation_result[0]
                elif isinstance(translation_result, dict) and 'generated_text' in translation_result:
                    translated_description = translation_result['generated_text']
                else:
                    st.error("Format de réponse de traduction inattendu. Veuillez réessayer.")
                    st.json(translation_result)  # Afficher la réponse brute pour le débogage
                    st.stop()
                
                st.success(f"Voici la description de l'image : {translated_description}")
            else:
                st.error("Échec de l'obtention de la description. Veuillez réessayer.")
                st.json(result)  # Afficher la réponse brute pour le débogage
