from flask import jsonify
from flask import request
from app.models import Alojamiento

#funcion que busca todo el listado de alojamientos
def traer_json_alojamientos():
        alojamientos_guardados = Alojamiento.get_all()
        list_alojamientos = [ alojamiento.serialize() for alojamiento in alojamientos_guardados]
        return jsonify(list_alojamientos)

#funcion que busca un unico alojamiento por ID
def traer_por_id_json_un_alojamiento(id):
        alojamiento = Alojamiento.get_by_id(id)
        if not alojamiento:
                return jsonify({'message': 'Alojamiento no encontrado'}), 404
        return jsonify(alojamiento.serialize())

#funcion para cargar a la BBDD un Alojamiento Nuevo
def alta_nuevo_alojamiento():
        data = request.json
        nuevo_alojamiento = Alojamiento(imagenRuta=data['imagenRuta'], cuit=data['cuit'], nombre=data['nombre'], web=data['web'], telefono=data['telefono'], direccion=data['direccion'], latitud=data['latitud'], longitud=data['longitud'], correo=data['correo'])
        
        nuevo_alojamiento.save()
        return jsonify({'message': 'Alojamiento dado de alta con exito'}), 201

#Funcion para modificar un alojamiento de la BBDD
def modificar_alojamiento(id):
        alojamiento = Alojamiento.get_by_id(id)
        if not alojamiento:
                return jsonify({'message': 'Alojamiento no encontrado'}), 404
        data = request.json
        alojamiento.cuit = data['cuit']
        alojamiento.nombre = data['nombre']
        alojamiento.web = data['web']
        alojamiento.telefono = data['telefono']
        alojamiento.direccion = data['direccion']
        alojamiento.latitud = data['latitud']
        alojamiento.longitud = data['longitud']
        alojamiento.correo = data['correo']
        alojamiento.save()
        return jsonify({'message': 'Alojamiento modificado con exito'})

def eliminar_alojamiento(id):
        alojamiento = Alojamiento.get_by_id(id)
        if not alojamiento:
                return jsonify({'message': 'Alojamiento no encontrado en la Base de Datos'}), 404
        alojamiento.delete()
        return jsonify({'message': 'Alojamiento eliminado con exito'})


