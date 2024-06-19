from flask import jsonify
from app.models import Alojamiento

# Funcion para agregar nuevo alojamiento a la BBDD
def alta_nuevo_alojamiento():
        pass

# Funcion que modifica los datos de un Alojamiento en la BBDD
def modificar_alojamiento():
        pass

# Funcion que agrega ruta a la imagen del nuevo alojamiento (quizas dentro de create_alojamiento no se aun)
def completar_ruta_imagen_alojamiento():
        pass

# Funcion que devuelve diccionario con todos los datos de los alojamientos en la BBDD
def dic_alojamientos():
        pass


#funcion que busca todo el listado de las peliculas
def traer_json_alojamientos():
    alojamientos_guardados = Alojamiento.get_all()
    list_alojamientos = [ alojamiento.serialize() for alojamiento in alojamientos_guardados]
    return jsonify(list_alojamientos)

