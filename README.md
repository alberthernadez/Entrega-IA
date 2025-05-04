🌍 Aplicación Web: ¿Qué idioma se habla en...? (IA + Streamlit)
Este proyecto es una aplicación web interactiva construida con Streamlit que permite a los usuarios hacer preguntas sobre qué idioma se habla en diferentes países. Utiliza la API de OpenAI para responder de forma directa y precisa, integrando inteligencia artificial para ofrecer una experiencia conversacional simple pero efectiva.

🧠 Descripción del Proyecto
La aplicación tiene como objetivo responder a la pregunta:
"¿Qué idioma se habla en [nombre del país]?"

El usuario solo debe escribir la pregunta en un cuadro de texto y, al hacer clic en un botón, recibirá una respuesta generada por la inteligencia artificial usando el modelo gpt-3.5-turbo de OpenAI.

🚀 Características Principales
✅ Entrada de Preguntas: Campo interactivo para escribir preguntas como “¿Qué idioma se habla en Italia?”

🤖 Procesamiento con IA: Uso de OpenAI para interpretar y responder de manera precisa.

🌐 Diseño Intuitivo: Interfaz amigable desarrollada con Streamlit.

📡 Carga de API Key: Uso de archivo .env para proteger y gestionar tu clave API.

📊 Análisis de Costo
Recurso	Costo estimado	Detalles
Streamlit	Gratis	Framework open source para crear apps interactivas.
Python y Librerías	Gratis	Incluye streamlit, openai, python-dotenv.
Visual Studio Code	Gratis	Editor de código.
API de OpenAI	Desde $0 según uso	Incluye crédito gratuito. Uso típico: $0.002 por respuesta corta.
Tiempo de Desarrollo	Trabajo personal	Horas invertidas en código, pruebas y ajustes.

💡 Una pregunta simple como “¿Qué idioma se habla en México?” cuesta menos de 1 centavo por token, ideal para proyectos educativos.

🛠️ Requisitos
Python 3.7 o superior

pip (gestor de paquetes)

Clave API de OpenAI válida

⚙️ Instalación y Configuración
Clona el repositorio o descarga el código

bash
Copiar
Editar
git clone https://github.com/tuusuario/nombre-del-repo
cd nombre-del-repo
Crea y activa un entorno virtual (opcional pero recomendado)

bash
Copiar
Editar
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Instala las dependencias

bash
Copiar
Editar
pip install -r requirements.txt
Configura tu archivo .env
Crea un archivo .env en la raíz del proyecto con este contenido:

env
Copiar
Editar
OPENAI_API_KEY=sk-tu-clave-aquí
🧪 Cómo Usar la Aplicación
Ejecuta la app:

bash
Copiar
Editar
streamlit run app.py
En el navegador, escribe una pregunta como:

¿Qué idioma se habla en Alemania?

La IA responderá directamente el idioma principal de ese país.

📌 Notas Finales
Esta aplicación es un ejemplo básico de integración de IA en la web usando Python.

Puede expandirse a otros usos: capitales, monedas, costumbres, etc.

Ideal para estudiantes, docentes o proyectos educativos.
