import openai
from django.conf import settings

openai.api_key = settings.OPEN_API_KEY

def obtener_recomendacion(mensaje):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Recomienda contenido basado en preferencias de usuario."}, {"role": "user", "content": mensaje}]

    )

    return response['choice'][0]['message']['content']