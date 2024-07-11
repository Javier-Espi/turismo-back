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
    Se agrega el valor de ID de la imagen para poder borrarla al borrar el item
    """

    def __init__(
        self,
        imagenRuta=None,
        imagenId=None,
        id=None,
        cuit=None,
        nombre=None,
        web=None,
        telefono=None,
        direccion=None,
        latitud=None,
        longitud=None,
        correo=None,
    ):
        self.id = id
        self.imagenRuta = imagenRuta
        self.imagenId = imagenId
        self.cuit = cuit
        self.nombre = nombre
        self.web = web
        self.telefono = telefono
        self.direccion = direccion
        self.latitud = latitud
        self.longitud = longitud
        self.correo = correo

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM crud")
        rows = cursor.fetchall()
        alojamientos_sql = [
            Alojamiento(
                id=row[0],
                imagenRuta=row[1],
                cuit=row[2],
                nombre=row[3],
                web=row[4],
                telefono=row[5],
                direccion=row[6],
                latitud=row[7],
                longitud=row[8],
                correo=row[9],
                imagenId=row[10],
            )
            for row in rows
        ]
        cursor.close()
        return alojamientos_sql

    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM crud WHERE id = '%s'", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Alojamiento(
                id=row[0],
                imagenRuta=row[1],
                cuit=row[2],
                nombre=row[3],
                web=row[4],
                telefono=row[5],
                direccion=row[6],
                latitud=row[7],
                longitud=row[8],
                correo=row[9],
                imagenId=row[10],
            )
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id:
            cursor.execute(
                """
                UPDATE crud SET imagenRuta = %s, imagenID = %s, cuit = %s, nombre = %s, web = %s, telefono = %s, direccion = %s, latitud = %s, longitud = %s, correo = %s
                WHERE id = '%s'
            """,
                (
                    self.imagenRuta,
                    self.imagenId,
                    self.cuit,
                    self.nombre,
                    self.web,
                    self.telefono,
                    self.direccion,
                    self.latitud,
                    self.longitud,
                    self.correo,
                    self.id,
                ),
            )
        else:
            cursor.execute(
                """
                INSERT INTO crud (id, imagenRuta, imagenID, cuit, nombre, web, telefono, direccion, latitud, longitud, correo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
                (
                    None,
                    self.imagenRuta,
                    self.imagenId,
                    self.cuit,
                    self.nombre,
                    self.web,
                    self.telefono,
                    self.direccion,
                    self.latitud,
                    self.longitud,
                    self.correo,
                ),
            )
            self.id = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM crud WHERE id = %s", (self.id,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            "id": self.id,
            "imagenRuta": self.imagenRuta,
            "imagenId": self.imagenId,
            "cuit": self.cuit,
            "nombre": self.nombre,
            "web": self.web,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "correo": self.correo,
        }
