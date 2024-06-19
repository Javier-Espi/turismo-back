from flask import Flask
from app.database import init_app
from app.views import *

# Creo instancia de Flask
app = Flask(__name__)

init_app(app)

# Asocio rutas con views 
app.route('/api/alojamientos',methods=['GET'])(traer_json_alojamientos)

#Permite separa el codigo que se ejecuta cuando se corre el archivo
if __name__=='__main__':
    app.run(debug=True)