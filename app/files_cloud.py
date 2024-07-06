import cloudinary
import cloudinary.uploader
import os
from threading import Event
from dotenv import load_dotenv


# Cargar variables de entorno desde el archivo .env para Cloudinary.com
load_dotenv()

cloudinary.config(
        cloud_name = os.getenv('CLOUD_NAME'),
        api_key=os.getenv('API_KEY'),
        api_secret=os.getenv('API_SECRET')
        )

#funcion que envia archivo imagene a cloudinary y recibe (retorna) la ruta
def ruta_nuevo_archivo_imagen(imagen, folder = 'Alojamientos'):
        print('intentando conectar cloudinary')
        result = cloudinary.uploader.upload(imagen)
        print ('**********************************************************************')
        Event().wait(3) # NO SE SI ES NECESARIO
        print (result)
        nueva_ruta = result["secure_url"]
        print (nueva_ruta)
        print ('**********************************************************************')
        return nueva_ruta