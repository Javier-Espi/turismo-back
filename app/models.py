from app.database import get_db

class Alojamiento:
    """
    Representa los datos de cada establecimiento de servicios de hospedaje ubicado en la zona
    y registrado de forma oficial como tal ante la autoridad municipal.
    Se reciben los siguientes atributos de Front:
        'cuit': Cuit del titular. Dato obligatorio y verificado en front.
        'nombre': Nombre comercial del alojamiento. Obligatorio y requiere estandarizar formato.
        'correo': Correo Electronico para comunicarse con el alojamiento.
        'web': Pagina Web del Alojamiento se la posee. Dato no obligatorio.
        'telefono': Teléfono de contacto comercial. Obligatorio con formato ya estandarizado. (entero 10 posiciones)
        'direccion': Dirección comercial del alojamiento. Obligatorio y requiere estandarizar formato.
        'latitud': Posición geográfica, Latitud del Alojamiento. Obligatorio.
        'longitud': Posición geográfica, Longitud del Alojamiento. Obligatorio.
    Al ingresar un alta, se guardará el archivo de la imagen del establecimiento y se asignaran
    valores durante el proceso de alta 'id' y a 'imagenRuta'
    """

    # creo que es mas prolijo disparar el constructor desde un diccionario donde se guarden los datos recibidos del Front
    # Fede pone directamente las claves VER QUE ES MEJOR
    def __init__(self, imagen_ruta=None, id=None, cuit=None, nombre=None, web=None, telefono=None, direccion=None, latitud=None, longitud=None, correo=None):
            self.id = id
            self.imagen_ruta = imagen_ruta
            self.cuit = cuit
            self.nombre = nombre
            self.web = web
            self.telefono = telefono
            self.direccion =  direccion
            self.latitud = latitud
            self.longitud = longitud
            self.correo = correo
            

    @staticmethod    
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM alojamientos.`crud`")
        rows = cursor.fetchall()
        alojamientos_sql = [Alojamiento(id=row[0], imagen_ruta=row[1], cuit=row[2], nombre=row[3], web=row[4], telefono=row[5], direccion=row[6], latitud=row[7], longitud=row[8], correo=row[9]) for row in rows]
        cursor.close()
        return alojamientos_sql

    def save(self):
        #logica para INSERT/UPDATE en base datos
        pass

    def delete(self):
        #logica para hacer un DELETE en la BASE
        pass
    
    def serialize(self):
        return {
            'id': self.id,
            'imagen_ruta': self.imagen_ruta,
            'cuit': self.cuit,
            'nombre': self.nombre,
            'web': self.web,
            'telefono': self.telefono,
            'direccion':self.direccion, 
            'latitud': self.latitud,
            'longitud': self.longitud,
            'correo': self.correo,
        }
    

