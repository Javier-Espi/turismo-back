import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env para Cloudinary.com
load_dotenv()

cloudinary.config(
        cloud_name = os.getenv('CLOUD_NAME'),
        api_key=os.getenv('API_KEY'),
        api_secret=os.getenv('API_SECRET'),
        secure = True
        )

#funcion que envia archivo de imagen a cloudinary y recibe (retorna) la ruta y el Id (para borrarlo o gestionarlo)
def datos_nuevo_archivo_imagen(imagen):
        result = cloudinary.uploader.upload(
                imagen,
                asset_folder = 'Alojamientos',
                transformation=[
                {"width": 500, "height": 500, "crop": "fill", "gravity": "auto"},
                {"quality": "auto", "fetch_format": "auto"}
                ]
        )
        return {'imagenRuta': result["secure_url"], 'imagenId': result['public_id']}

#funcion para borrar un archivo de cloudinary pasandole el public_id
def borrar_de_cloudinary_por_id(public_id):
        resultado = cloudinary.uploader.destroy(public_id)
        print('************************************************************')
        print(resultado)
        print('************************************************************')
