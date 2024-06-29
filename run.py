from flask import Flask
from flask_cors import CORS
from app.database import init_app
from app.views import *

# Creo instancia de Flask
app = Flask(__name__)

init_app(app)

#permitir solicitudes desde cualquier origen
#Si no se instala bien el flask_cors en el entorno, mover desde el general al venv/
# global esta en c:\users\usuario\appdata\local\programs\python\python310\lib\site-packages
cors = CORS(app)
#cors = CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500/*"}})
#cors = CORS(app, resources={r"/api/*": {"origins": "https://javier-espi.github.io/turismo/*"}})

# Asocio rutas con views 
app.route('/api/alojamientos',methods=['GET'])(traer_json_alojamientos)
app.route('/api/alojamientos/<int:id>',methods=['GET'])(traer_por_id_json_un_alojamiento)
app.route('/api/alojamientos',methods=['POST'])(alta_nuevo_alojamiento)
app.route('/api/alojamientos/<int:id>',methods=['PUT'])(modificar_alojamiento)
app.route('/api/alojamientos/<int:id>',methods=['DELETE'])(eliminar_alojamiento)

#Permite separa el codigo que se ejecuta cuando se corre el archivo
if __name__=='__main__':
    app.run(debug=True)