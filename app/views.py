from flask import jsonify
from flask import request
from app.models import Alojamiento
from app.files_cloud import ruta_nuevo_archivo_imagen


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

def eliminar_alojamiento(id):
        alojamiento = Alojamiento.get_by_id(id)
        if not alojamiento:
                return jsonify({'message': 'Alojamiento no encontrado en la Base de Datos'}), 404
        alojamiento.delete()
        return jsonify({'message': 'Alojamiento eliminado con exito'})

#funcion para cargar a la BBDD un Alojamiento Nuevo POR FORM
def alta_nuevo_alojamiento_form():
        data = request.form
        nuevo_alojamiento = Alojamiento(imagenRuta=data['imagenRuta'], cuit=data['cuit'], nombre=data['nombre'], web=data['web'], telefono=data['telefono'], direccion=data['direccion'], latitud=data['latitud'], longitud=data['longitud'], correo=data['correo'])
        files = request.files
        imagen = files['imagen']
        if imagen:
                nuevo_alojamiento.imagenRuta = ruta_nuevo_archivo_imagen(imagen)
        nuevo_alojamiento.save()
        return jsonify({'message': 'Alojamiento dado de alta con exito'}), 201

#Funcion para modificar un alojamiento de la BBDD por FORM
def modificar_alojamiento_form(id):
        alojamiento = Alojamiento.get_by_id(id)
        if not alojamiento:
                return jsonify({'message': 'Alojamiento no encontrado'}), 404
        data = request.form
        files = request.files
        imagen = files['imagen']
        if imagen:
                alojamiento.rutaImagen = ruta_nuevo_archivo_imagen(imagen)
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

# NO SE ESTAN USANDO PERO LOS DEJO PARA TENER UN EJEMPLO RECIBIR POR JSON

#funcion para cargar a la BBDD un Alojamiento Nuevo por JSON
def alta_nuevo_alojamiento():
        data = request.json
        nuevo_alojamiento = Alojamiento(imagenRuta=data['imagenRuta'], cuit=data['cuit'], nombre=data['nombre'], web=data['web'], telefono=data['telefono'], direccion=data['direccion'], latitud=data['latitud'], longitud=data['longitud'], correo=data['correo'])
        nuevo_alojamiento.save()
        return jsonify({'message': 'Alojamiento dado de alta con exito'}), 201

#Funcion para modificar un alojamiento de la BBDD por JSON
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
