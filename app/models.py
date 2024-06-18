class Alojamiento:
    """
    Representa los datos de cada establecimiento de servicios de hospedaje ubicado en la zona
    y registrado de forma oficial como tal ante la autoridad municipal.
    Se reciben los siguientes atributos de Front:
        'cuit': Cuit del titular. Dato obligatorio y verificado en front.
        'nombre': Nombre comercial del alojamiento. Obligatorio y requiere estandarizar formato.
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
    def __init__(self, dicAlojamientos):
        # Preguntar si parece necesario el if "de Seguridad" por si entra un dato vacio o None en lugar de ""??
        if dicAlojamientos == None:
            self.id = ""
            self.imagenRuta = ""
            self.cuit = ""
            self.nombre = ""
            self.web = ""
            self.telefono = ""
            self.direccion =  ""
            self.latitud = ""
            self.longitud = ""
        else:
            self.id = ""
            self.imagenRuta = ""
            self.cuit = dicAlojamientos['cuit']
            self.nombre = dicAlojamientos['nombre']
            self.web = dicAlojamientos['web']
            self.telefono = dicAlojamientos['telefono']
            self.direccion =  dicAlojamientos['direccion']
            self.latitud = dicAlojamientos['latirud']
            self.longitud = dicAlojamientos['longitud']
        
            


