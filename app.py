import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Idiomas por País", page_icon="🌍")

st.title("🌍 ¿Qué idioma se habla en...?")
st.write("Pregúntame por el idioma de un país y te lo diré usando inteligencia artificial 🤖")

# Input del usuario
pregunta = st.text_input("Escribe tu pregunta aquí (ej. ¿Qué idioma se habla en Brasil?)")

# Botón para enviar
if st.button("Responder"):
    if pregunta:
        with st.spinner("Pensando..."):
            prompt = f"""Responde de forma clara y directa la siguiente pregunta:
            
            {pregunta}

            Solo responde con el idioma principal que se habla en ese país."""
            
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3,
                    max_tokens=50
                )
                respuesta = response.choices[0].message.content.strip()
                st.success(respuesta)
            except Exception as e:
                st.error(f"Error al conectar con OpenAI: {e}")
    else:
        st.warning("Por favor, escribe una pregunta primero.")
